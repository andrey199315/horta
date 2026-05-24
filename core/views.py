from django.shortcuts import render
from django.db.models import Sum
from .models import RegistroIrrigacao

def dashboard(request):
    dados = RegistroIrrigacao.objects.filter(fim__isnull=False)
    total_acionamentos = dados.count()
    total_segundos = sum(d.duracao_segundos for d in dados)
    total_consumo = dados.aggregate(Sum('consumo_estimado'))['consumo_estimado__sum'] or 0

    context = {
        'acionamentos': total_acionamentos,
        'tempo_total': round(total_segundos / 60, 2),
        'consumo': round(total_consumo, 2),
        'historico': dados.order_by('-inicio')[:10] # Últimos 10 acionamentos
    }
    return render(request, 'dashboard.html', context)
from django.shortcuts import render

from django.http import JsonResponse
from .models import RegistroIrrigacao
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.db.models import Sum, Count

@csrf_exempt
def atualizar_status(request):
    status = request.GET.get('motor') # 1 ligado, 0 desligado
    
    if status == '1':
        # Cria novo registro
        RegistroIrrigacao.objects.get_or_create(fim__isnull=True)
    elif status == '0':
        # Finaliza 
        aberto = RegistroIrrigacao.objects.filter(fim__isnull=True).last()
        if aberto:
            aberto.fim = timezone.now()
            aberto.calcular_consumo()
            
    return JsonResponse({'status': 'ok'})

def dashboard(request):
    dados = RegistroIrrigacao.objects.filter(fim__isnull=False)
    total_acionamentos = dados.count()
    total_segundos = sum(d.duracao_segundos for d in dados)
    total_consumo = dados.aggregate(Sum('consumo_estimado'))['consumo_estimado__sum'] or 0

    context = {
        'acionamentos': total_acionamentos,
        'tempo_total': round(total_segundos / 60, 2),
        'consumo': round(total_consumo, 2),
        'historico': dados.order_by('-inicio')[:10]
    }
    return render(request, 'dashboard.html', context)
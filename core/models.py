from django.db import models
from django.utils import timezone

class RegistroIrrigacao(models.Model):
    inicio = models.DateTimeField(default=timezone.now)
    fim = models.DateTimeField(null=True, blank=True)
    consumo_estimado = models.FloatField(default=0.0) # Em litros

    @property
    def duracao_segundos(self):
        if self.fim:
            return (self.fim - self.inicio).total_seconds()
        return 0

    def calcular_consumo(self, vazao_por_minuto=5.0):
        if self.fim:
            minutos = self.duracao_segundos / 60
            self.consumo_estimado = minutos * vazao_por_minuto
            self.save()
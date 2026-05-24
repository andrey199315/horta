from django.core.management.base import BaseCommand
from django.utils import timezone
import serial
import time

from core.models import RegistroIrrigacao 

class Command(BaseCommand):
    help = 'Lê os dados do Arduino via USB e salva direto no banco de dados'

    def handle(self, *args, **kwargs):
        #CONFIGURAÇÃO DA PORTA USB
        PORTA = 'COM3'
        BAUD_RATE = 9600
        
        try:
            arduino = serial.Serial(PORTA, BAUD_RATE, timeout=1)
            self.stdout.write(self.style.SUCCESS(f'Conectado ao Arduino na porta {PORTA}!'))
            time.sleep(2)
            
            while True:
                if arduino.in_waiting > 0:
                    mensagem = arduino.readline().decode('utf-8').strip()
                    
                    if mensagem == "LIGAR_MOTOR":
                        #Cria o registro se não houver um em aberto
                        RegistroIrrigacao.objects.get_or_create(fim__isnull=True)
                        self.stdout.write(self.style.WARNING(f'[{timezone.now().strftime("%H:%M:%S")}] Motor LIGADO - Registro criado!'))
                        
                    elif mensagem == "DESLIGAR_MOTOR":
                        #finaliza registro aberto
                        aberto = RegistroIrrigacao.objects.filter(fim__isnull=True).last()
                        if aberto:
                            aberto.fim = timezone.now()
                            aberto.calcular_consumo()
                            self.stdout.write(self.style.SUCCESS(f'[{timezone.now().strftime("%H:%M:%S")}] Motor DESLIGADO - Consumo calculado: {aberto.consumo_estimado:.2f}L'))
                            
        except serial.SerialException:
            self.stdout.write(self.style.ERROR(f'Erro: Não foi possível conectar na porta {PORTA}. A IDE do Arduino está fechada?'))
        except KeyboardInterrupt:
            self.stdout.write(self.style.ERROR('\nLeitura do USB encerrada pelo usuário.'))
            if 'arduino' in locals() and arduino.is_open:
                arduino.close()
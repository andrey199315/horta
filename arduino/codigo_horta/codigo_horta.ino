#include <LiquidCrystal.h>

// CONFIGURAÇÃO DO LCD 
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

// DEFINIÇÃO DOS PINOS
#define PIN_UMID A0 
#define PIN_MOTOR 6  

// LIMITES (%)
#define UMID_BAIXA 30
#define UMID_ALTA 70

bool motorLigado = false;

void setup() {
  // Inicializa a comunicação Serial via USB
  Serial.begin(9600); 
  
  lcd.begin(16, 2);
  
  pinMode(PIN_UMID, INPUT);
  pinMode(PIN_MOTOR, OUTPUT);
  digitalWrite(PIN_MOTOR, LOW);
  
  lcd.print("Horta Pronta!");
  delay(1500);
  lcd.clear();
}

void loop() {
  int umidadeRaw = analogRead(PIN_UMID);
  
  int porcentagem = map(umidadeRaw, 0, 1023, 0, 100);

  // DISPLAY LCD
  lcd.setCursor(0, 0);
  lcd.print("Umidade: ");
  lcd.print(porcentagem);
  lcd.print("%   ");
  lcd.setCursor(0, 1);

  // LÓGICA DO MOTOR E ENVIO SERIAL
  if (porcentagem <= UMID_BAIXA) {
    lcd.print("Irrigando...   ");
    digitalWrite(PIN_MOTOR, HIGH);
    
    if (!motorLigado) {
      motorLigado = true;
      Serial.println("LIGAR_MOTOR");
    }
  } 
  else if (porcentagem >= UMID_ALTA) {
    lcd.print("Solo Molhado   ");
    digitalWrite(PIN_MOTOR, LOW);
    
    if (motorLigado) {
      motorLigado = false;
      Serial.println("DESLIGAR_MOTOR");
    }
  } 
  else {
    lcd.print("Umidade OK     ");
    if (motorLigado) {
        digitalWrite(PIN_MOTOR, LOW);
        motorLigado = false;
        Serial.println("DESLIGAR_MOTOR");
    }
  }

  delay(2000);
}
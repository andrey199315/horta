# Horta

Projeto Django para gerenciar dados de horta e acompanhar o cultivo de plantas.

## 📋 Pré-requisitos

- Python 3.9 ou superior
- pip (gerenciador de pacotes Python)
- Git

## 🚀 Instalação

### 1. Clonar o repositório

```bash
git clone <seu-repositorio-url>
cd horta
```

### 2. Criar e ativar ambiente virtual

**No Windows:**
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

## ⚙️ 1. Configuração do Arduino

1. Abra a [Arduino IDE](https://www.arduino.cc/en/software).
2. Vá em **Ferramentas > Gerenciar Bibliotecas** e instale a biblioteca **LiquidCrystal** (by Arduino).
3. Abra o arquivo `arduino/codigo_horta/codigo_horta.ino`.
4. Conecte o Arduino via USB e faça o upload do código.
5. **Importante:** Anote o nome da porta que o Arduino está usando (ex: `COM3` no Windows ou `/dev/ttyUSB0` no Linux/Mac) e feche o Serial Monitor da IDE.

## ⚙️ Configuração

### 1. Executar migrações do banco de dados
```bash
python manage.py makemigrations
python manage.py migrate
```

## 🏃 Executar o projeto
Sera necessario o uso de dois terminais

Terminal 1:
```bash
python manage.py runserver
```
O servidor estará disponível em: `http://localhost:8000/`

Terminal 2:
```bash
python manage.py ler_arduino
```

## 📌 Notas

- se ocorrer "Erro Access is denied" ou "Porta Ocupada", O Serial Monitor do Arduino IDE provavelmente está aberto. Feche-o antes de rodar o comando ler_arduino.

- Os dados não aparecem no gráfico: Atualize a página da web. O gráfico é atualizado a cada refresh da página quando novos dados são salvos pelo comando do terminal 2.

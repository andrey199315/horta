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

**No macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

## ⚙️ Configuração

### 1. Executar migrações do banco de dados

```bash
python manage.py migrate
```

### 2. Criar superusuário (admin)

```bash
python manage.py createsuperuser
```

Siga as instruções na tela para definir username, email e senha.

## 🏃 Executar o projeto

```bash
python manage.py runserver
```

O servidor estará disponível em: `http://localhost:8000/`

## 📱 Acessar a administração

1. Acesse: `http://localhost:8000/admin/`
2. Faça login com as credenciais do superusuário criado

## 📂 Estrutura do projeto

```
horta/
├── core/                 # App principal
│   ├── migrations/       # Migrações do banco de dados
│   ├── templates/        # Templates HTML
│   ├── models.py         # Modelos do banco de dados
│   ├── views.py          # Lógica das views
│   ├── urls.py           # Rotas da app
│   └── admin.py          # Configurações do admin
├── horta_pi/             # Configurações do projeto
│   ├── settings.py       # Configurações do Django
│   ├── urls.py           # Rotas principais
│   └── wsgi.py           # Configuração WSGI
├── manage.py             # Script de gerenciamento
├── requirements.txt      # Dependências do projeto
└── .gitignore            # Arquivos ignorados no Git
```

## 🔧 Comandos úteis

```bash
# Criar nova app
python manage.py startapp <nome-da-app>

# Criar migrações
python manage.py makemigrations

# Ver migrações pendentes
python manage.py showmigrations

# Executar testes
python manage.py test

# Limpar cache
python manage.py clear_cache
```

## 📝 Dependências

- Django 6.0.4
- asgiref 3.11.1
- sqlparse 0.5.5
- tzdata 2026.2

Ver `requirements.txt` para mais detalhes.

## 🛡️ Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto para configurações sensíveis (não será versionado):

```
SECRET_KEY=sua-chave-secreta
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

## 📌 Notas

- O arquivo `.gitignore` já está configurado para ignorar ambiente virtual, arquivos de cache e banco de dados.
- Nunca faça commit do arquivo `db.sqlite3` em produção.
- Sempre crie um novo ambiente virtual para cada projeto.

## 📞 Suporte

Para dúvidas ou issues, abra uma issue no repositório.

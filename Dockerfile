# ============================================
# DOCKERFILE - Aplicação Django Financeira
# ============================================
# Este arquivo define como construir a "imagem" da sua aplicação.
# Uma imagem é como um "molde" que será usado para criar containers.

# --------------------------------------------
# 1. IMAGEM BASE
# --------------------------------------------
# Usamos Python 3.12 versão "slim" (mais leve, sem extras desnecessários)
# O Docker vai baixar essa imagem do Docker Hub automaticamente
FROM python:3.12-slim

# --------------------------------------------
# 2. VARIÁVEIS DE AMBIENTE
# --------------------------------------------
# PYTHONDONTWRITEBYTECODE=1: Não criar arquivos .pyc (economia de espaço)
# PYTHONUNBUFFERED=1: Logs aparecem em tempo real (importante para debug)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# --------------------------------------------
# 3. DIRETÓRIO DE TRABALHO
# --------------------------------------------
# Define /app como pasta principal dentro do container
# Todos os comandos serão executados a partir daqui
WORKDIR /app

# --------------------------------------------
# 4. DEPENDÊNCIAS DO SISTEMA
# --------------------------------------------
# Instala bibliotecas necessárias para o psycopg2 (driver PostgreSQL)
# - libpq-dev: bibliotecas do PostgreSQL
# - gcc: compilador C (necessário para compilar algumas libs Python)
# O "rm -rf" no final limpa cache para manter a imagem pequena
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# --------------------------------------------
# 5. DEPENDÊNCIAS PYTHON
# --------------------------------------------
# Primeiro copiamos só o requirements.txt (otimização de cache)
# Se o requirements.txt não mudar, o Docker reutiliza o cache dessa etapa
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --------------------------------------------
# 6. CÓDIGO DA APLICAÇÃO
# --------------------------------------------
# Agora copiamos todo o resto do código
# O "." significa "diretório atual" (onde está o Dockerfile)
COPY . .

# --------------------------------------------
# 7. ARQUIVOS ESTÁTICOS
# --------------------------------------------
# Coleta todos os arquivos CSS, JS, imagens em uma única pasta
# Necessário para servir arquivos estáticos em produção
RUN python manage.py collectstatic --noinput

# --------------------------------------------
# 8. PORTA
# --------------------------------------------
# Informa que o container vai escutar na porta 8000
# (isso é apenas documentação, não abre a porta de verdade)
EXPOSE 8000

# --------------------------------------------
# 9. COMANDO DE INICIALIZAÇÃO
# --------------------------------------------
# Gunicorn é o servidor WSGI de produção para Django
# --bind 0.0.0.0:8000: aceita conexões de qualquer IP na porta 8000
# config.wsgi:application: aponta para o arquivo wsgi.py
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]

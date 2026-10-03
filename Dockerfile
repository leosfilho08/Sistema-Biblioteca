FROM python:3.13-slim

WORKDIR /app

# 1. Atualizar pacotes do sistema operacional
RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

# 2. Copiar dependências da aplicação
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3. Hardening: Forçar atualização dos pacotes vulneráveis para as versões corrigidas
RUN pip install --no-cache-dir --upgrade \
    "urllib3>=2.8.0" \
    "msgpack>=1.2.1" \
    "setuptools>=83.0.0"

# 4. Criar usuário não-root (appuser) para garantir execução segura
RUN useradd -m -u 1000 appuser && \
    mkdir -p /app/dados && \
    chown -R appuser:appuser /app

COPY --chown=appuser:appuser . .

USER appuser

CMD ["python", "main.py"]

FROM python:3.13

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requeriments.txt

CMD ["python", "main.py"]
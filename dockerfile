FROM python:alpine

WORKDIR /app

COPY . .

CMD ["python", "Main.py"]
FROM python:3

RUN apt-get update && apt-get install -y libpq-dev build-essential
RUN pip install --upgrade pip
RUN pip freeze > requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app

COPY . .

CMD ["python", "Main.py"]
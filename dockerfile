FROM python:3.10-alpine

WORKDIR /app

COPY . .
RUN pip install --upgrade pip && pip install customtkinter \
    pip install selenium && pip install webdriver_manager \
    pip install wintoast

RUN wget -q "https://chromedriver.storage.googleapis.com/2.35/chromedriver_linux64.zip" -O /tmp/chromedriver.zip \
    && unzip /tmp/chromedriver.zip -d /usr/bin/ \
    && rm /tmp/chromedriver.zip


CMD ["python", "Main.py"]

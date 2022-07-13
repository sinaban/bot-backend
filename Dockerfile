FROM tradingapp/ubuntu:latest

WORKDIR /bot-backend

COPY . .

RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install --upgrade setuptools && \
    python3 -m pip install -r requirements.txt

COPY . .

CMD ["python3", "app.py"]
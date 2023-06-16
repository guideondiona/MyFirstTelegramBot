FROM python:3.11-alpine
WORKDIR /code

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY bot bot
COPY misc misc
COPY config.py .
COPY main.py .
COPY .env .
COPY cur.json .

CMD [ "python", "main.py" ]
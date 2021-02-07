FROM python:3.6-slim

WORKDIR /usr/src/app

RUN apt-get update
RUN apt-get install -y git
RUN pip install holdup

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app .

EXPOSE 8000

CMD ["sh", "-c", "holdup -v tcp://$POSTGRES_HOST:$POSTGRES_PORT -- python manage.py runserver 0.0.0.0:8000"]

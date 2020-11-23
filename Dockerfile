FROM python:3.8.4

WORKDIR /app

ADD . /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app
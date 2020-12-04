FROM python:3.8.4

ENV PYTHONUNBUFFERED 1

WORKDIR /web_app

ADD . /web_app/

COPY ./requirements.txt /web_app/requirements.txt

RUN pip install -r requirements.txt

COPY . /web_app/
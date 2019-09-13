FROM python:3.5-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk upgrade && pip install -U pip && pip3 install --upgrade pip setuptools && apk add libpq


RUN apk add --virtual .build-deps gcc python3-dev musl-dev postgresql-dev


RUN mkdir /updater
RUN mkdir /updater/common

COPY ./updater updater/
COPY ./common updater/common

RUN python3 -m pip install psycopg2
RUN pip3 install --no-cache-dir -r updater/requirements.pip

RUN apk del .build-deps

WORKDIR /updater


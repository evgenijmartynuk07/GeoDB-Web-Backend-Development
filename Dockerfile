FROM python:3.10.8-slim

LABEL maintainer="evgenijmartynuk07@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y postgis
RUN apt-get install -y postgis postgresql-13-postgis-3
RUN apt-get install -y libgeos-dev
RUN apt-get install -y binutils libproj-dev gdal-bin
RUN apt-get install -y python3-gdal
RUN apt-get install -y libffi-dev

COPY . .

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

USER django-user

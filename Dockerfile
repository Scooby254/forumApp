FROM python:3

MAINTAINER Scooby

ENV PYTHONUNBUFFERED 1

RUN mkdir /woni

WORKDIR /woni

ADD . /woni

COPY ./requirements.txt /woni/requirements.txt

RUN pip install -r requirements.txt

COPY . .
FROM python:3.9-buster

ENV PYTHONUNBUFFERED=1

# copy source and install dependencies
RUN mkdir -p /forum

WORKDIR /forum

#ADD . /forum

COPY  . .
# install dependencies
RUN pip install -r /forum/requirements.txt

EXPOSE 8000

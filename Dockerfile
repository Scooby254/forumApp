FROM python:3.9-buster

ENV PYTHONUNBUFFERED=1

# install nginx
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

# copy source and install dependencies
RUN mkdir -p /forum

WORKDIR /forum

#ADD . /forum

#COPY ./requirements.txt /forum/

COPY  . .
RUN pip install -r app/forum/requirements.txt
RUN chown -R www-data:www-data /app

EXPOSE 8000
STOPSIGNAL SIGTERM
CMD ["/forum/start-server.sh"]
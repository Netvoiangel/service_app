FROM python:3.9-alpine3.16

COPY requirements.txt /temp/requirements.txt
COPY service /service
WORKDIR /service 
EXPOSE 8000 

RUN apk add postgresql-client build-base postgresql-dev
# Открываем порт 

RUN pip install -r /temp/requirements.txt
# RUN adduser --disabled-password service-user 
# RUN chown service-user:service-user -R /service/

# USER service-user
# Чтобы не происходило под root'ом


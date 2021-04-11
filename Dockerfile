FROM python:3.8-slim-buster

MAINTAINER Barbel Thierry "barbel.thierry@gmail.com"

RUN apt update && apt upgrade

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install rasa

COPY gilfoyle /app/gilfoyle
COPY chatbot /app/chatbot
COPY .env /app/.env
COPY entrypoint.sh /app/entrypoint.sh
COPY setup.py /app/setup.py

RUN python3 -m pip install -e .

EXPOSE 5055

ENTRYPOINT [ "./entrypoint.sh" ]

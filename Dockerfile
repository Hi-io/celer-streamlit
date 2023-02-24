FROM python:3.8-slim-buster

WORKDIR /app

COPY ./mail_viewer/* /app/

RUN pip install -r requirements.txt

EXPOSE 80

CMD [ "python", 'main.py' ]
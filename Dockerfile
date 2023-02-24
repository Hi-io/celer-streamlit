FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

COPY ./API/app/ /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt
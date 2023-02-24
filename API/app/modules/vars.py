import os

API_KEY = os.getenv('API_KEY')
DEPARTMENTS = os.getenv('DEPARTMENTS').split(',')

CONFIG = {
    'user': os.getenv('USER'),
    'password': os.getenv('PASSWORD'),
    'host': os.getenv('HOST_DB'),
    'db': os.getenv('DB')
}
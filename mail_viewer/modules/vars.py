import os

CONFIG = { 
    'username': os.getenv('USERNAME'),
    'password': os.getenv('PASSWORD'),
    'server': os.getenv('SERVER'),
    'port': os.getenv('PORT'),
    'folder': os.getenv('FOLDER')
}

API_URL = os.getenv('URL')

CRITERIA = os.getenv('CRITERIA')
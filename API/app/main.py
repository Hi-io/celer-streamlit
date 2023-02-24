from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import openai
from modules.modules import *


app = FastAPI()
openai.api_key = ''

@app.get("/")
async def root():
    return RedirectResponse(url="/redocs/")

@app.post("/data_load/")
async def data_load(data:dict, api_key:str):

    api_key = openai.api_key

    timestamp = data['timestamp']
    user = data['user']
    message = data['msg']
    platform = data['platform']

    department = identify_department(message, api_key)
    resumed_message = resume_message(message, api_key)

    row = {'user': user, 'message': message, 'resumed_message': resumed_message, 'department': department, 'platform': platform, 'timestamp': timestamp}

    


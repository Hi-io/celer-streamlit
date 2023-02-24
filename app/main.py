from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import openai
from modules.modules import *


app = FastAPI()
api_key = ''


@app.get("/")
async def root():
    return RedirectResponse(url="/docs/")


@app.get("/resume_messages/")
async def message_resume(message:str, api_key:str):
    result = resume_message(message, api_key)
    return result


@app.get("/department_identifier/")
async def department_identifier(message:str, api_key:str):
    result = identify_department(message, api_key)
    return result


@app.post("/data_load/")
async def data_load(data:dict, api_key:str):
    timestamp = data['timestamp']
    user = data['user']
    message = data['msg']
    platform = data['platform']
    department = department_identifier(message, api_key)
    resumed_message = resume_message(message, api_key)
    result = {'user': user, 'message': message, 'resumed_message': resumed_message, 'department': department, 'platform': platform, 'timestamp': timestamp}


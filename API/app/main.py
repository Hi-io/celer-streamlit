from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import openai
from modules.modules import *

app = FastAPI()

@app.get("/")
async def root():
    return RedirectResponse(url="/redoc/")

@app.post("/solution_load/")
async def solution_load(data:dict):

    timestamp = data['timestamp']
    user = data['user']
    message = data['msg']
    platform = data['platform']

    department = identify_department(message)
    resumed_message = resume_message(message)

    row = {'user': user, 'message': message, 'resumed_message': resumed_message, 'department': department, 'platform': platform, 'timestamp': timestamp}

    load_solution(row)


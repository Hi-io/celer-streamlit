from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from modules import *


app = FastAPI()


@app.get("/")
async def root():
    return RedirectResponse(url="/docs/")


@app.post("/message_load/")
async def message_load(data:dict):

    timestamp = data['timestamp']
    user = data['user']
    message = data['msg']
    platform = data['platform']

    department = modules.identify_department(message)
    resumed_message = modules.resume_message(message)

    row = {'user': user, 'message': message, 'resumed_message': resumed_message, 'department': department, 'platform': platform, 'timestamp': timestamp}

    modules.load_message(row)


@app.post("/pending_message/")
async def pending_message():
    pending = modules.pending_message()
    return pending


@app.post("/pending_solution/")
async def pending_solution():
    pending = modules.pending_solution()
    return pending


@app.post("/respond_email/")
async def respond_email(data:str, API_KEY:str):
    result = modules.response_email(data, API_KEY)
    return result
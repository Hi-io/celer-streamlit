from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from modules import modules

app = FastAPI()

@app.get("/")
async def root():
    return RedirectResponse(url="/docs/")

@app.post("/solution_load/")
async def solution_load(data:dict):

    timestamp = data['timestamp']
    user = data['user']
    message = data['msg']
    platform = data['platform']

    department = modules.identify_department(message)
    resumed_message = modules.resume_message(message)

    row = {'user': user, 'message': message, 'resumed_message': resumed_message, 'department': department, 'platform': platform, 'timestamp': timestamp}

    modules.load_solution(row)


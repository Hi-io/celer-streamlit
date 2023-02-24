import mysql.connector
import openai
from modules.vars import API_KEY, DEPARTMENTS, CONFIG
import os


def identify_department(msg:str):
    # Categorizar el departamento
    openai.api_key = API_KEY
    result = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"Classify the following ticket into one of the following departments: {DEPARTMENTS}\n\nmessage: {msg}\nDepartment:",
    max_tokens=4,
    stop=None,
    )
    return result.choices[0].text.strip()


def resume_message(msg:str):

    openai.api_key = API_KEY
    result = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"Summarize the following message: {msg}\nSummary:",
    max_tokens=400,
    stop=None,
    )
    return result.choices[0].text.strip()

def load_solution(data):

    conn = mysql.connector.connect(**CONFIG)

    cursor = conn.cursor()

    insert_query = ("INSERT INTO solutions (user, platform, msg, resume, timestamp) values (%s, %s, %s, %s, %s)")
    data = (data['user'], data['platform'], data['msg'], data['resume'], data['timestamp'])

    cursor.execute(insert_query, data)

    conn.commit()

    cursor.close()
    conn.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
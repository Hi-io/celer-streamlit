import mysql.connector
import openai


api_key = ''


def identify_department(mensaje:str, API_KEY:str):
    # Categorizar el departamento
    openai.api_key = API_KEY
    categorias = ["IT", "Marketing", "RRHH", "Legales"]
    resultado = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"Clasificar el siguiente ticket en una de las siguientes categorías: {categorias}\n\nmensaje: {mensaje}\nCategoría:",
    max_tokens=4,
    stop=None,
    )
    return resultado.choices[0].text.strip()


def resume_message(mensaje:str, API_KEY:str):
    # Categorizar el departamento
    openai.api_key = API_KEY
    categorias = ["IT", "Marketing", "RRHH", "Legales"]
    resultado = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"Resume el siguiente mensaje: {mensaje}\nResumen:",
    max_tokens=400,
    stop=None,
    )
    result = resultado.choices[0].text.strip()
    return result

def load_solution(data, user, password, host, db):

    conn = mysql.connector.connect(
        user = user,
        password = password,
        host = host,
        db = db
    )

    cursor = conn.cursor()

    insert_query = ("INSERT INTO solutions (user, platform, msg, resume, timestamp) values (%s, %s, %s, %s, %s)")
    data = (data['user'], data['platform'], data['msg'], data['resume'], data['timestamp'])

    cursor.execute(insert_query, data)

    conn.commit()

    cursor.close()
    conn.close()

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
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


def get_info_message(message_info:dict, API_KEY:str):
    user = message_info['user']
    message = message_info['message']
    platform = message_info['platform']
    date = message_info['date']
    department = identify_department(message, API_KEY)
    resumed_message = resume_message(message, API_KEY)
    return {'user': user, 'message': message, 'resumed_message': resumed_message, 'department': department, 'platform': platform, 'date': date}



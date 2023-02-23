import discord
from discord.ext import commands,tasks
import datetime
#import requests
import openai

# Token del bot de discord
token_discord = 'MTA0OTQ1OTE2ODA0NzgxMjc0OA.GDfkMM.3Mlhy_qagw3fxaIDdEDMCchwzZFcI3_OZW3tn0'

# API de GPT
api_key = "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"

# De nuestra API
api_url = ''

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def msg_ans(mensaje: str, API_KEY: str):
  openai.api_key = API_KEY
  resultado = openai.Completion.create(
      model="text-davinci-003",
      prompt=f"Client: {mensaje}\nContext: first Tell the client that we have registered his message and will receive a response ASAP.then give him a little advice if possible. \nCustom response to the client:",
      max_tokens=2000,
      stop=None,
  )
  return resultado.choices[0].text.strip()

def gpt_miku(mensaje: str, API_KEY: str):
  openai.api_key = API_KEY
  resultado = openai.Completion.create(
      model="text-davinci-003",
      prompt=f"Contexto: Eres una Miku Nakano y estás ligando conmigo\nmensaje: {mensaje}\nRespuesta:",
      max_tokens=500,
      stop=None,
  )
  return resultado.choices[0].text.strip()

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if 'message:' in message.content.lower() or 'message :' in message.content.lower():
    data = {'date': datetime.datetime.now().timestamp(),
            'sender': message.author.id,
            'body': message.content[8:]
            }
    # response = requests.post(api_url, json=data)
    async with message.channel.typing():
      # Clasifica el departamento del ticket
      # Luego enviar a la API el siguiente mensaje: message.content[8:]
      try:
        respuesta = msg_ans(message.content[8:], api_key)
        await message.channel.send(respuesta)
      except:
        await message.channel.send('Error 👺')
  
  
  if 'todo bien?' in message.content.lower():
    await message.channel.send('ID:')
    await message.channel.send(message.author.id)
    await message.channel.send('<@' + str(message.author.id) + '>')
    await message.channel.send('CHANNEL:')
    await message.channel.send(message.channel.id)
    await message.channel.send('Todo piola👺')
  
  if 'miku' in message.content.lower():
        async with message.channel.typing():
          # Clasifica el departamento del ticket
          respuesta = gpt_miku(message.content, api_key)
          await message.channel.send(respuesta)

@tasks.loop(minutes=2)
async def revisar_respuestas():
  channel = tasks.get_channel(1032770186656354397)
  await channel.send("Revisando respuestas de la API.")
# Inicia el bot
client.run(token_discord)

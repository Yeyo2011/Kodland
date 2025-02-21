import discord
import random
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)
def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""
@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('contrasena'):
        
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    else:
        await message.channel.send(message.content)

client.run("8f79414207ab4b9b5a5edb428a6951c13e7a0e5cc6e8722319796f4bb820e5b1")

import discord
from discord.ext import commands

# Configurar los privilegios del bot
intents = discord.Intents.default()
intents.message_content = True

# Crear el bot con el prefijo "!"
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    content = message.content.lower()  # Convertir el mensaje a minúsculas

    if content.startswith('hello'):
        await message.channel.send("Hi! 👋")
    elif content.startswith('bye'):
        await message.channel.send("Goodbye! 😊")
    elif content.startswith("send cat"):
        try:
            with open("images/image.png", "rb") as f:
                picture = discord.File(f)
                await message.channel.send("Aquí tienes un gato 🐱", file=picture)
        except FileNotFoundError:
            await message.channel.send("¡No encontré la imagen del gato! 😿")
    # else:
        #await message.channel.send(f"{message.content}")

    await bot.process_commands(message)  # Necesario para que los comandos funcionen

@bot.command()
async def mem(ctx):
    import random
    meme=random.randint(1,3)
    if meme == 1:
        try:
            with open('images/mem1.jpg', 'rb') as f:
                picture = discord.File(f)
            await ctx.send(file=picture)
        except FileNotFoundError:
            await ctx.send("¡No encontré la imagen del meme! 😢")
    if meme == 2:
        try:
            with open('images/meme2.jpg', 'rb') as f:
                picture = discord.File(f)
            await ctx.send(file=picture)
        except FileNotFoundError:
            await ctx.send("¡No encontré la imagen del meme! 😢")
    if meme == 3:
        try:
            with open('images/meme3.jpg', 'rb') as f:
                picture = discord.File(f)
            await ctx.send(file=picture)
        except FileNotFoundError:
            await ctx.send("¡No encontré la imagen del meme! 😢")

bot.run("")

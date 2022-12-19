import os
import nextcord #importamos para conectarnos con el bot
from nextcord.ext import commands #importamos los comandos
# import wavelink
# import datetime
# import random
# import requests
# import shutil
#from replit import db

token = token = "4f 54 6b 79 4f 54 6b 79 4e 7a 67 30 4e 54 45 34 4e 7a 55 34 4e 54 67 77 2e 47 6b 79 79 61 69 2e 54 47 53 6c 31 78 5a 5f 49 63 53 77 39 42 31 74 74 33 38 4c 2d 64 68 36 56 5f 69 76 47 2d 36 31 41 30 78 55 68 49"

token = bytes.fromhex(token)

token = str(token)[2:-1]

bot = commands.Bot(command_prefix="t", description="PGT testing", help_command=None, intents=nextcord.Intents.all())

@bot.event
async def on_ready():
    await bot.change_presence(activity=nextcord.Game(name="probanding..."))
    print('El bot está listo!')
    try:
        await bot.get_user(458428946963496960).send("El bot se acaba de encender")
    except :
        pass

@bot.command()
async def test(ctx):
    await ctx.message.delete()
    await ctx.channel.send("Se uso el comando help")

bot.run(token)
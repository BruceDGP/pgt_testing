import os
import nextcord #importamos para conectarnos con el bot
from nextcord.ext import commands #importamos los comandos
import wavelink
import datetime
import random
import requests
import shutil
#from replit import db

bot = commands.Bot(command_prefix="t", description="PGT testing", help_command=None, intents=nextcord.Intents.all())

@bot.event
async def on_ready():
    await bot.change_presence(activity=nextcord.Game(name="probanding..."))
    print('El bot está listo!')
    try:
        await bot.get_user(458428946963496960).send("El bot se acaba de encender")
    except :
        pass

@bot.commands
async def help(ctx):
    await ctx.message.delete()
    await ctx.channel.send("Se uso el comando help")

bot.run(os.getenv("TOKEN"))
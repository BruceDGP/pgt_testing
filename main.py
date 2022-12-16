import os

os.system("pip install nextcord")

import nextcord #importamos para conectarnos con el bot
from nextcord.ext import commands #importamos los comandos

bot = commands.Bot(command_prefix="t", description="PGT testing", help_command=None, intents=nextcord.Intents.all())

@bot.event
async def on_ready():
    await bot.change_presence(activity=nextcord.Game(name="probanding..."))
    print('El bot está listo!')
    try:
        await bot.get_user(458428946963496960).send("El bot se acaba de encender")
    except :
        pass

bot.run(os.getenv("TOKEN"))
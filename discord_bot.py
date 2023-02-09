import discord
import asyncio
from discord.ext import commands
description = "desc"
bot = commands.Bot(command_prefix='?', description=description)
#startup command
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
#category of main commands
class Main_Commands():
    def __init__(self, bot):
        self.bot = bot
#ping command test
@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("pong")
#when the user types in ?ping, the bot will return "pong"
#This is an example of a simple command in this language
#RunBot
bot.run("TOKEN GOES HERE")



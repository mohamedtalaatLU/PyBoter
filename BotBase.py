s = """
import discord
from discord.ext import commands
import asyncio
import time


Client = discord.Client()
client = commands.Bot(command_prefix = "*")

@client.event
async def on_ready():
    print("boton is ready")
    SayInput = input("Enter content to say ")
    await client.send_message(channel, "%s" % SayInput)
    await client.change_presence(game=discord.Game(name='LEGO Universe'))

@client.event
async def on_message(message):
    if message.content.startswith("hello"):
        await client.send_message("welcome")
        



    








client.run() #please enter the token here
"""

token = input("Enter your bot token:\n> ")
print("Attempting login...\n")
import discord
from discord.ext import commands
intents = discord.Intents.all()
description = ""
client = commands.Bot(command_prefix="", description=description, intents=intents)
print("Welcome to reoccurcat's custom bot client.\n")
@client.event
async def on_ready():
    while True:
        command = input("> ")
client.run(token)
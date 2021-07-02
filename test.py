token = input("Enter your bot token:\n> ")
print("Attempting login...\n")
import discord
from discord.ext import commands
import sys
intents = discord.Intents.all()
description = ""
client = commands.Bot(command_prefix="", description=description, intents=intents)
print("Welcome to reoccurcat's custom bot client.\n")
validcommands = ["server", "channel", "help", "exit"]
@client.event
async def on_ready():
    while True:
        command = input("> ")
        if command.split()[0] == "help":
            print(f"The valid commands are: {','.join(validcommands)}\n")
        elif command.split()[0] == "exit":
            print(f"Exiting...\n")
            break
    await client.close()
client.run(token)
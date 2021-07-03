import discord
from discord.ext import commands
token = input("Enter your bot token:\n> ")
print("Attempting login...\n")
intents = discord.Intents.all()
description = ""
client = commands.Bot(command_prefix="", description=description, intents=intents)
client.server = None
client.channel = None
print("Welcome to reoccurcat's custom bot client.\n")
validcommands = ["servers", "channels", "help", "exit", "sendmsg"]
@client.event
async def on_ready():
    while True:
        command = input("> ")
        if command.split()[0] == "help":
            print(f"The valid commands are: {', '.join(validcommands)}\n")
        elif command.split()[0] == "exit":
            print(f"Exiting...\n")
            break
        elif command.split()[0] == "servers":
            try:
                if command.split()[1] == "list":
                    print("Servers the bot is in:\n")
                    servers = []
                    for guild in client.guilds:
                        servers.append(f"Name: {guild.name}; ID: {guild.id}")
                    print("\n".join(servers))
                elif command.split()[1] == "select":
                    serverid = input("Enter the server ID of the server you want to select:\n> ")
                    client.server = client.get_guild(int(serverid))
                    print("Successfully selected that server.\n")
                else:
                    print("Allowed options for this command are: list, select\n")
            except:
                print("Allowed options for this command are: list, select\n")
        elif command.split()[0] == "channels":
            if client.server != None:
                try:
                    if command.split()[1] == "list":
                        print("Channels in the server you selected:\n")
                        channels = []
                        for channel in client.server.channels:
                            if str(channel.type) == "text":
                                channels.append(f"Name: {channel.name}; ID: {channel.id}")
                        print("\n".join(channels))
                    elif command.split()[1] == "select":
                        channelid = input("Enter the channel ID of the channel you want to select:\n> ")
                        client.channel = client.get_channel(int(channelid))
                        print("Successfully selected that channel.\n")
                    else:
                        print("Allowed options for this command are: list, select\n")
                except:
                    print("Allowed options for this command are: list, select\n")
            else:
                print("You need to select a server first.\n")
        elif command.split()[0] == "sendmsg":
            if client.channel != None:
                await client.channel.send(command.replace(command.split()[0], ""))
                print("Message sent to the channel you selected.\n")
            else:
                print("You need to select a channel first.\n")
    await client.close()
@client.event
async def on_message(msg):
    pass
client.run(token)
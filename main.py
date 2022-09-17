# ----------------------------------------------------------------------------------------------------------------------

# ███╗░░░███╗███████╗░██████╗░█████╗░   ██╗░░░██╗░░███╗░░
# ████╗░████║██╔════╝██╔════╝██╔══██╗   ██║░░░██║░████║░░
# ██╔████╔██║█████╗░░╚█████╗░███████║   ╚██╗░██╔╝██╔██║░░
# ██║╚██╔╝██║██╔══╝░░░╚═══██╗██╔══██║   ░╚████╔╝░╚═╝██║░░
# ██║░╚═╝░██║███████╗██████╔╝██║░░██║   ░░╚██╔╝░░███████╗
# ╚═╝░░░░░╚═╝╚══════╝╚═════╝░╚═╝░░╚═╝   ░░░╚═╝░░░╚══════╝

# lankles - 2021/2022

# ----------------------------------------------------------------------------------------------------------------------

# Libraries
import os
import discord
import asyncio

# Sub-Libraries (not sure if thats what they're called)
from discord.ext import commands
from discord.ext.commands import Cog

# Client / Token
intents = discord.Intents.all()
client = commands.Bot(command_prefix='>', intents=intents, help_command=None)

token = open('token.txt', 'r').read()

# ----------------------------------------------------------------------------------------------------------------------

# Ready
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

# ----------------------------------------------------------------------------------------------------------------------

# Loads the cogs.
async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')
            print(f'{filename} is now online.')

async def start():
    await load()
    await client.start(token)

asyncio.run(start())

# ----------------------------------------------------------------------------------------------------------------------

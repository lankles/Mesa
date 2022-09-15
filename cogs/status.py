# ----------------------------------------------------------------------------------------------------------------------

# ░██████╗████████╗░█████╗░████████╗██╗░░░██╗░██████╗
# ██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║░░░██║██╔════╝
# ╚█████╗░░░░██║░░░███████║░░░██║░░░██║░░░██║╚█████╗░
# ░╚═══██╗░░░██║░░░██╔══██║░░░██║░░░██║░░░██║░╚═══██╗
# ██████╔╝░░░██║░░░██║░░██║░░░██║░░░╚██████╔╝██████╔╝
# ╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░░╚═════╝░╚═════╝░

# ----------------------------------------------------------------------------------------------------------------------

# Libraries
import discord
import random
import asyncio

# Sub-Libraries
from discord.ext import commands

# ----------------------------------------------------------------------------------------------------------------------

# Statuses
statuses = [
    'DOOM Eternal',
    'DOOM 64',
    'DOOM 3',
    'Counter-Strike: Global Offensive',
    'Counter-Strike: Condition Zero',
    'Nekopara Vol. 1',
    'Nekopara Vol. 4',
    'Minecraft',
    'Minecraft: Dungeons',
    'PlayerUnknowns Battlegrounds',
    'Terraria',
    'Among Us',
    'The Legend of Zelda: Breath of The Wild',
    'The Legend of Zelda: Ocarina of Time',
    'Cars 2 The Video Game',
    'Fall Guys: Ultimate Knockout',
    'YouTubers Life',
    'A Hat in Time',
    'Creepy Castle'
]

# ----------------------------------------------------------------------------------------------------------------------

# Class
class Status(commands.Cog):

    # Setup
    def __init__(self, client):
        self.client = client

    # ------------------------------------------------------------------------------------------------------------------

    # Functions

    # ------------------------------------------------------------------------------------------------------------------

    # Status change loop.
    async def statusloop(self):
        while True:
            # Picks a status.
            newstatus = random.choice(statuses)

            # Changes the status of the bot.
            activity = discord.Game(name=f'{newstatus} | >help')
            await self.client.change_presence(status=discord.Status.idle, activity=activity)

            # Waiting time.
            await asyncio.sleep(60)

    # ------------------------------------------------------------------------------------------------------------------

    # Events

    # ------------------------------------------------------------------------------------------------------------------

    # On ready event.
    @commands.Cog.listener()
    async def on_ready(self):
        self.client.loop.create_task(self.statusloop())

# ----------------------------------------------------------------------------------------------------------------------

def setup(client):
    client.add_cog(Status(client))

# ----------------------------------------------------------------------------------------------------------------------

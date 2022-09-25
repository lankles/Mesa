# ----------------------------------------------------------------------------------------------------------------------

# ██╗░░░██╗███╗░░██╗██╗░░░░░██╗░██████╗████████╗███████╗██████╗░
# ██║░░░██║████╗░██║██║░░░░░██║██╔════╝╚══██╔══╝██╔════╝██╔══██╗
# ██║░░░██║██╔██╗██║██║░░░░░██║╚█████╗░░░░██║░░░█████╗░░██║░░██║
# ██║░░░██║██║╚████║██║░░░░░██║░╚═══██╗░░░██║░░░██╔══╝░░██║░░██║
# ╚██████╔╝██║░╚███║███████╗██║██████╔╝░░░██║░░░███████╗██████╔╝
# ░╚═════╝░╚═╝░░╚══╝╚══════╝╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═════╝░

# ----------------------------------------------------------------------------------------------------------------------

# Libraries
import discord
import random
import asyncio

# Sub-Libraries
from discord.ext import commands
from discord import app_commands

# ----------------------------------------------------------------------------------------------------------------------

# The guild in which the /message command is useable
hostGuild = 818348640451035158

# ----------------------------------------------------------------------------------------------------------------------

# Class
class Misc(commands.Cog):

    # Setup
    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    # ------------------------------------------------------------------------------------------------------------------

    # Events

    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------

    # Commands

    # ------------------------------------------------------------------------------------------------------------------

    # Tavros Command
    @commands.hybrid_command(
        name = "tavros",
        description = "Sends a Tavros gif (I was forced to add this against my will)."
    )
    async def tavros(self, ctx: commands.Context):
        await ctx.reply('https://media.discordapp.net/attachments/570340985452625920/813862319997714472/image0.gif')

    # Messager Command
    @commands.hybrid_command(
        name = "message",
        description = "Allows the bot owner to send messages.",
        aliases=['messager','send']
    )
    @app_commands.guilds(discord.Object(id=818348640451035158))
    async def messager(self, ctx: commands.Context, guildid: str, channelid: str, message: str):
        if ctx.guild.id == hostGuild:
            # Sends a message in the desired channel
            for guild in self.client.guilds:
                if str(guild.id) == guildid:
                    for channel in guild.channels:
                        if str(channel.id) == channelid:
                            await channel.send(message)
                            await ctx.reply(f'Message sent succesfully in **{guild.name}**.')
                            return
                        else:
                            await ctx.reply(f'Channel does not exist or **{self.client.user.name}** does not have access to it.')
                            return
            await ctx.reply(f'**{self.client.user.name}** is not in this guild.')
        else:
            await ctx.reply('You do not have permission to use this command.')

# ----------------------------------------------------------------------------------------------------------------------

    # Nownline Command
    @commands.hybrid_command(
        name = "nownline",
        description = "Recounts the Nownline incident.",
        aliases=['nl','line','nown']
    )
    @app_commands.guilds(discord.Object(id=818348640451035158))
    async def nownline(self, ctx: commands.Context):
        # Sends the nownline copypasta.
        await ctx.reply(
            """ **[NOWNLINE INCCIDENT]**

Start of recording by Dr. ######

It was 9:09 pm of November 1, 2018. The deep facilty known as ####### had caugth an explosin or some sort of light that went for hours. People of ######## believed that something has fallen from the sky by something or someone. It went from 2 hours that the bombing went down and a light emerged from the ground. The bombing was captured with camers surronded the facility and we can give info on what we saw that day. Cam 2 and 3 screen's was all white and cannot identify what was it, but in Cam 4, it showed a beam of ligth from the sky that landed down and created a large ligth outside from the facility. We never know where it came from, but researches theorized and officially called it the "Nownline" incident. Line as in as the Beam that represents a line and Nown as a explosion or ligth. There's surrounding this incident include 3 theories
1. The beaming ligth came from aliens or other worldly spedcimen
2. The beaming ligth was to spawn a creature or "human" of some sort to study as 
3. It was an attack from secret military project, or a warning

All this theories could be true but seems to be this will remain a mystery

*END OF RECORDING* """
        )

# ----------------------------------------------------------------------------------------------------------------------

async def setup(client: commands.Bot) -> None:
   await client.add_cog(Misc(client))

# ----------------------------------------------------------------------------------------------------------------------

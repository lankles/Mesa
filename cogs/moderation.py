# ----------------------------------------------------------------------------------------------------------------------

# ███╗░░░███╗░█████╗░██████╗░███████╗██████╗░░█████╗░████████╗██╗░█████╗░███╗░░██╗
# ████╗░████║██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
# ██╔████╔██║██║░░██║██║░░██║█████╗░░██████╔╝███████║░░░██║░░░██║██║░░██║██╔██╗██║
# ██║╚██╔╝██║██║░░██║██║░░██║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║██║░░██║██║╚████║
# ██║░╚═╝░██║╚█████╔╝██████╔╝███████╗██║░░██║██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║
# ╚═╝░░░░░╚═╝░╚════╝░╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝

# ----------------------------------------------------------------------------------------------------------------------

# Libraries
import discord
import random
import aiofiles

# Sub-Libraries
from discord.ext import commands
from typing import Literal
from discord import app_commands
from discord.app_commands import Choice


# ----------------------------------------------------------------------------------------------------------------------

# Class
class Moderation(commands.Cog):

    # Setup
    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    # ------------------------------------------------------------------------------------------------------------------

    # Events

    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------

    # Commands

    # ------------------------------------------------------------------------------------------------------------------

    # Kick Command
    @commands.hybrid_command(
        name='kick',
        description='Kicks a member, kick permission is needed.',
        aliases=['k']
    )
    async def kick(self, ctx, member: discord.Member, reason: str):
        if member.guild_permissions.kick_members is True:
            # Sends a correction message for the user.
            await ctx.reply('You do not have permission to perform this command **(User cannot be kicked)**.')
            return
        else:
            # Checks for permission.
            if ctx.author.guild_permissions.kick_members is True:

                # Sends the user a DM message.
                try:
                    await member.send(f'You have been kicked from **{ctx.guild}**: ``{reason}``')
                except discord.Forbidden:
                    print("User has direct messages disabled, continuing.")

                # Removes the member and sends a message notifying the rest of the server.
                await ctx.guild.kick(user=member, reason=reason)
                await ctx.reply(f'**{member}** has been kicked from **{ctx.guild.name}**: ``{reason}``')
            else:
                # Sends a correction message for the user.
                await ctx.reply('You do not have permission to perform this command **(Missing rank)**.')

    # ------------------------------------------------------------------------------------------------------------------

    # Ban Command
    @commands.hybrid_command(
        name='ban',
        description='Bans a member, ban permission is needed.',
        aliases=['b']
    )
    @app_commands.choices(delete_messages=[
        Choice(name="None",value=0),
        Choice(name="Previous Day",value=1),
        Choice(name="Previous 2 Days",value=2),
        Choice(name="Previous 3 Days",value=3),
        Choice(name="Previous 4 Days",value=4),
        Choice(name="Previous 5 Days",value=5),
        Choice(name="Previous 6 Days",value=6),
        Choice(name="Previous 7 Days",value=7)
    ])
    async def ban(self, ctx, member: discord.Member, reason: str, delete_messages: int):
        if member.guild_permissions.ban_members is True:
            # Sends a correction message for the user.
            await ctx.reply('You do not have permission to perform this command **(User cannot be banned)**.')
            return
        else:
            # Checks for permission.
            if ctx.author.guild_permissions.ban_members is True:

                # Sends the user a DM message.
                try:
                    await member.send(f'You have been banned from **{ctx.guild}**: ``{reason}``')
                except discord.Forbidden:
                    print("User has direct messages disabled, continuing.")

                # Removes the member and sends a message notifying the rest of the server.
                await ctx.guild.ban(user=member, reason=reason, delete_message_days=delete_messages)
                await ctx.reply(f'**{member}** has been banned from **{ctx.guild.name}**: ``{reason}`` - **{delete_messages}** day(s) worth of messages deleted')
            else:
                # Sends a correction message for the user.
                await ctx.reply('You do not have permission to perform this command **(Missing rank)**.')
                
# ----------------------------------------------------------------------------------------------------------------------

async def setup(client: commands.Bot) -> None:
   await client.add_cog(Moderation(client))

# ----------------------------------------------------------------------------------------------------------------------

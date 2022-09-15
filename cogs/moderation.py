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


# ----------------------------------------------------------------------------------------------------------------------

# Class
class Moderation(commands.Cog):

    # Setup
    def __init__(self, client):
        self.client = client

    # ------------------------------------------------------------------------------------------------------------------

    # Events

    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------

    # Commands

    # ------------------------------------------------------------------------------------------------------------------

    # Kick Command
    @commands.command(
        name='kick',
        description='Kicks a member, kick permission is needed.',
        aliases=['k']
    )
    async def kick(self, ctx, member: discord.Member = None, *, reason=None):

        # Checks for a valid reason and if the user is immune.

        if member is None or reason is None:
            # Sends a correction message for the user.
            await ctx.channel.send('You must input a valid member tag and reason. Try "**>kick [user] [reason]**".')
            return

        if member.guild_permissions.kick_members is True:
            # Sends a correction message for the user.
            await ctx.channel.send('You do not have permission to perform this command. (User Cannot Be Kicked)')
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
                await ctx.channel.send(f'**{member}** has been kicked from the server: ``{reason}``')

            else:
                # Sends a correction message for the user.
                await ctx.channel.send('You do not have permission to perform this command. (Missing Rank)')

    # Error
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.BadArgument):
            # Sends a correction message for the user.
            await ctx.channel.send('You must input a valid member tag and reason. Try "**>kick [user] [reason]**".')
        return

    # ------------------------------------------------------------------------------------------------------------------

    # Ban Command
    @commands.command(
        name='ban',
        description='Bans a member, ban permission is needed.',
        aliases=['b']
    )
    async def ban(self, ctx, member: discord.Member = None, *, reason=None):

        # Checks for a valid reason and if the user is immune.

        if member is None or reason is None:
            # Sends a correction message for the user.
            await ctx.channel.send('You must input a valid member tag and reason. Try "**>ban [user] [reason]**".')
            return

        if member.guild_permissions.ban_members is True:
            # Sends a correction message for the user.
            await ctx.channel.send('You do not have permission to perform this command. (User Cannot Be Banned)')
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
                await ctx.guild.ban(user=member, reason=reason)
                await ctx.channel.send(f'**{member}** has been banned from the server: ``{reason}``')

            else:
                # Sends a correction message for the user.
                await ctx.channel.send('You do not have permission to perform this command. (Missing Rank)')

    # Error
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.BadArgument):
            # Sends a correction message for the user.
            await ctx.channel.send('You must input a valid member tag and reason. Try "**>ban [user] [reason]**".')
        return

# ----------------------------------------------------------------------------------------------------------------------

def setup(client):
    client.add_cog(Moderation(client))

# ----------------------------------------------------------------------------------------------------------------------

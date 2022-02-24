# ----------------------------------------------------------------------------------------------------------------------

# ██╗░░██╗███████╗██╗░░░░░██████╗░███████╗██╗░░░██╗██╗░░░░░
# ██║░░██║██╔════╝██║░░░░░██╔══██╗██╔════╝██║░░░██║██║░░░░░
# ███████║█████╗░░██║░░░░░██████╔╝█████╗░░██║░░░██║██║░░░░░
# ██╔══██║██╔══╝░░██║░░░░░██╔═══╝░██╔══╝░░██║░░░██║██║░░░░░
# ██║░░██║███████╗███████╗██║░░░░░██║░░░░░╚██████╔╝███████╗
# ╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░░░░╚═╝░░░░░░╚═════╝░╚══════╝

# ----------------------------------------------------------------------------------------------------------------------

# Libraries
import discord
import random

# Sub-Libraries
from discord.ext import commands

# ----------------------------------------------------------------------------------------------------------------------

# Class
class Helpful(commands.Cog):

    # Setup
    def __init__(self, client):
        self.client = client

    # ------------------------------------------------------------------------------------------------------------------

    # Events

    # ------------------------------------------------------------------------------------------------------------------

    # Ready
    @commands.Cog.listener()
    async def on_ready(self):
        print('Helpful cog is now online.')
        print('-----')

    # ------------------------------------------------------------------------------------------------------------------

    # Commands

    # ------------------------------------------------------------------------------------------------------------------

    # PFP Command
    @commands.command(
        name='pfp',
        description='Tag a user to get their profile picture in HD.',
        aliases=['profilep', 'profilepic', 'pfpic', 'pfpicture', 'profilepicture']
    )
    async def pfp(self, ctx, member: discord.Member = None):
        # Sends a users profile picture in HD.

        # Checks if there is a valid member tag.
        if member is None:
            # Sends a correction message for the user.
            await ctx.channel.send('You must input a valid user tag. Try "**>pfp [user]**".')
            return
        else:
            # Sends the avatar image.
            await ctx.channel.send(member.avatar_url)

    # Error
    @pfp.error
    async def pfp_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.BadArgument):
            # Sends a correction message for the user.
            await ctx.channel.send('You must input a valid user tag. Try "**>pfp [user]**".')
        return

    # ------------------------------------------------------------------------------------------------------------------

    # Jdate Command
    @commands.command(
        name='jdate',
        description='Tag a user to get their Discord join date.',
        aliases=['joindate']
    )
    async def jdate(self, ctx, member: discord.Member = None):
        # Sends a users Discord join date.

        # Checks if there is a valid member tag.
        if member is None:
            # Sends a correction message for the user.
            await ctx.channel.send('You must input a valid user tag. Try "**>jdate [user]**".')
            return
        else:
            # Sends the Discord join date.
            joindate = member.created_at.strftime('%b %d, %Y')
            await ctx.channel.send(f'**{member}** joined Discord on **{joindate}**.')

    # Error
    @jdate.error
    async def jdtate_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.BadArgument):
            # Sends a correction message for the user.
            await ctx.channel.send('You must input a valid user tag. Try "**>jdate [user]**".')
        return

    # ------------------------------------------------------------------------------------------------------------------

    # SJdate Command
    @commands.command(
        name='sjdate',
        description='Tag a user to get their last server join date.',
        aliases=['serverdate', 'serverjdate', 'serverjoindate']
    )
    async def sjdate(self, ctx, member: discord.Member = None):
        # Sends a users server join date.

        # Checks if there is a valid member tag.
        if member is None:
            # Sends a correction message for the user.
            await ctx.channel.send('You must input a valid user tag. Try "**>sjdate [user]**".')
            return
        else:
            # Sends the server join date.
            joindate = member.joined_at.strftime('%b %d, %Y')
            await ctx.channel.send(f'**{member}** last joined **{ctx.guild}** on **{joindate}**.')

    # Error
    @sjdate.error
    async def sjdate_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.BadArgument):
            # Sends a correction message for the user.
            await ctx.channel.send('You must input a valid user tag. Try "**>sjdate [user]**".')
        return

# ----------------------------------------------------------------------------------------------------------------------

def setup(client):
    client.add_cog(Helpful(client))

# ----------------------------------------------------------------------------------------------------------------------

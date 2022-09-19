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
from discord import app_commands

# ----------------------------------------------------------------------------------------------------------------------

# Class
class Helpful(commands.Cog):

    # Setup
    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    # ------------------------------------------------------------------------------------------------------------------

    # Events

    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------

    # Commands

    # ------------------------------------------------------------------------------------------------------------------

    # PFP Command
    @commands.hybrid_command(
        name='pfp',
        description='Tag a user to get their profile picture in HD.',
        aliases=['profilep', 'profilepic', 'pfpic', 'pfpicture', 'profilepicture']
    )
    async def pfp(self, ctx, member: discord.Member):
        # Sends a users profile picture in HD.

        # Checks if there is a valid member tag.
        if member is None:
            # Sends a correction message for the user.
            await ctx.reply('You must input a valid user tag. Try "**>pfp [user]**".')
            return
        else:
            # Sends the avatar image.
            await ctx.reply(member.display_avatar)

    # ------------------------------------------------------------------------------------------------------------------

    # Jdate Command
    @commands.hybrid_command(
        name='jdate',
        description='Tag a user to get their Discord join date.',
        aliases=['joindate']
    )
    async def jdate(self, ctx, member: discord.Member):
        # Sends a users Discord join date.

        # Checks if there is a valid member tag.
        if member is None:
            # Sends a correction message for the user.
            await ctx.reply('You must input a valid user tag. Try "**>jdate [user]**".')
            return
        else:
            # Sends the Discord join date.
            joindate = member.created_at.strftime('%b %d, %Y')
            await ctx.reply(f'**{member}** joined Discord on **{joindate}**.')

    # ------------------------------------------------------------------------------------------------------------------

    # SJdate Command
    @commands.hybrid_command(
        name='sjdate',
        description='Tag a user to get their last server join date.',
        aliases=['serverdate', 'serverjdate', 'serverjoindate']
    )
    async def sjdate(self, ctx, member: discord.Member):
        # Sends a users server join date.

        # Checks if there is a valid member tag.
        if member is None:
            # Sends a correction message for the user.
            await ctx.reply('You must input a valid user tag. Try "**>sjdate [user]**".')
            return
        else:
            # Sends the server join date.
            joindate = member.joined_at.strftime('%b %d, %Y')
            await ctx.reply(f'**{member}** last joined **{ctx.guild}** on **{joindate}**.')

# ----------------------------------------------------------------------------------------------------------------------

async def setup(client: commands.Bot) -> None:
   await client.add_cog(Helpful(client))

# ----------------------------------------------------------------------------------------------------------------------

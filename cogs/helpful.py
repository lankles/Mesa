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
from typing import Optional

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

    # Avatar Command
    @commands.hybrid_command(
        name='avatar',
        description='Tag a user to get their avatar in HD.',
        aliases=['pfp', 'profilep', 'profilepic', 'pfpic', 'pfpicture', 'profilepicture']
    )
    async def avatar(self, ctx, member: discord.Member, guild: Optional[bool] = False):
        fetchedUser = await self.client.fetch_user(member.id)
        if guild == False:
            if fetchedUser.avatar == None:
                await ctx.reply(f'**{member.name}** does not currently have a user avatar.')
                return
            await ctx.reply(fetchedUser.avatar)
        else:
            if member.guild_avatar == None:
                await ctx.reply(f'**{member.name}** does not currently have a guild avatar.')
                return
            await ctx.reply(member.guild_avatar)

    # ------------------------------------------------------------------------------------------------------------------

    # Banner Command
    @commands.hybrid_command(
        name='banner',
        description='Tag a user to get their banner in HD.',
    )
    async def banner(self, ctx, member: discord.Member):
        fetchedUser = await self.client.fetch_user(member.id)
        # Sends the banner image.
        if fetchedUser.banner == None:
            await ctx.reply(f'**{member.name}** does not currently have a user banner.')
            return
        await ctx.reply(fetchedUser.banner)

    # ------------------------------------------------------------------------------------------------------------------

    

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

# ----------------------------------------------------------------------------------------------------------------------

# ██╗░░██╗███████╗██╗░░░░░██████╗░
# ██║░░██║██╔════╝██║░░░░░██╔══██╗
# ███████║█████╗░░██║░░░░░██████╔╝
# ██╔══██║██╔══╝░░██║░░░░░██╔═══╝░
# ██║░░██║███████╗███████╗██║░░░░░
# ╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░░░░

# ----------------------------------------------------------------------------------------------------------------------

# Libraries
import discord
import random
import math

# Sub-Libraries
from discord.ext import commands

# ----------------------------------------------------------------------------------------------------------------------

# Class
class Help(commands.Cog):

    # Setup
    def __init__(self, client):
        self.client = client

    # ------------------------------------------------------------------------------------------------------------------

    # Events

    # ------------------------------------------------------------------------------------------------------------------
    
    # ------------------------------------------------------------------------------------------------------------------

    # Commands

    # ------------------------------------------------------------------------------------------------------------------

    # Help Command
    @commands.command(
        name='help',
        description='Lists all available commands.',
        aliases=['h', 'info', 'information']
    )
    async def help(self, ctx, cog='1'):

        # Creates the basic embed we'll be using.
        helpEmbed = discord.Embed(
            color=3447003
        )
        helpEmbed.set_thumbnail(url=ctx.author.avatar_url)
        helpEmbed.set_author(name='Commands', icon_url=self.client.user.avatar_url)

        # Removes cogs without commands or cogs we dont want to display.
        cogs = [c for c in self.client.cogs.keys()]
        cogs.remove('Status')
        cogs.remove('UnlistedCmds')

        totalPages = math.ceil(len(cogs) / 4)

        # Converts the sent in number to an integer, if it is not a number it will send an error.
        try:
            cog = int(cog)
        except ValueError:
            await ctx.send(f'You must input a valid page number. Please pick between **1** and **{totalPages}** using "**>help [number]**".')
            return

        if cog > totalPages or cog < 1:
            await ctx.send(f'You must input a valid page number. Please pick between **1** and **{totalPages}** using "**>help [number]**".')
            return

        helpEmbed.set_footer(
            text=f'Page {cog} of {totalPages}'
        )

        neededCogs = []
        for i in range(4):
            x = i + (int(cog) - 1) * 4
            try:
                neededCogs.append(cogs[x])
            except IndexError:
                pass

        for cog in neededCogs:
            commandList = ''
            for command in self.client.get_cog(cog).walk_commands():
                if command.hidden:
                    continue
                elif command.parent is not None:
                    continue

                commandList += f'**{command.name}** - *{command.description}*\n'
            commandList += '\n'

            helpEmbed.add_field(name=cog, value=commandList, inline=False)

        await ctx.send(embed=helpEmbed)

# ----------------------------------------------------------------------------------------------------------------------

def setup(client):
    client.add_cog(Help(client))

# ----------------------------------------------------------------------------------------------------------------------

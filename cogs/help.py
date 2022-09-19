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
import math

# Sub-Libraries
from discord.ext import commands
from discord import app_commands
from discord.ui import Button, View

# ----------------------------------------------------------------------------------------------------------------------

# Class
class Help(commands.Cog):

    # Setup
    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    # ------------------------------------------------------------------------------------------------------------------

    # Events

    # ------------------------------------------------------------------------------------------------------------------
    
    # ------------------------------------------------------------------------------------------------------------------

    # Commands

    # ------------------------------------------------------------------------------------------------------------------

    # Help Command
    @commands.hybrid_command(
        name='help',
        with_app_command = True,
        description='Lists all available commands.',
    )
    async def help(self, ctx: commands.Context, page: int = 1):
        maxDrawnCogs = 2

        # Creates the basic embed we'll be using.
        async def drawEmbed(page: int):
            helpEmbed = discord.Embed(
                color=3447003
            )

            helpEmbed.set_thumbnail(url=ctx.author.display_avatar)
            helpEmbed.set_author(name='Commands',icon_url=self.client.user.display_avatar)

            # Removes cogs without commands or cogs we dont want to display.
            cogs = [c for c in self.client.cogs.keys()]
            cogs.remove('Status')
            cogs.remove('Misc')

            totalPages = math.ceil(len(cogs) / maxDrawnCogs)

            # Converts the sent in number to an integer, if it is not a number it will send an error.
            if page > totalPages or page < 1:
                return False

            helpEmbed.set_footer(
                text=f'Page {str(page)} of {totalPages}'
            )

            neededCogs = []
            for i in range(maxDrawnCogs):
                x = i + (page - 1) * maxDrawnCogs
                try:
                    neededCogs.append(cogs[x])
                except IndexError:
                    pass

            for cog in neededCogs:
                commandList = ''
                for command in self.client.get_cog(cog).walk_app_commands():
                    if command.parent is not None:
                        continue

                    commandList += f'{command.name} - *{command.description}*\n'
                for command in self.client.get_cog(cog).walk_commands():
                    if command.parent is not None:
                        continue

                    commandList += f'{command.name} - *{command.description}*\n'
                commandList += '\n'

                helpEmbed.add_field(name=cog, value=commandList, inline=False)
            return helpEmbed

    # ----------------------------------------------------------------------------------------------------------------------
        
        drawnEmbed = await drawEmbed(page)
        if drawnEmbed == False: 
            await ctx.reply(f'You must input a valid page number.')
            return

        currentPage = page

        left = Button(label="<", style=discord.ButtonStyle.gray)
        right = Button(label=">", style=discord.ButtonStyle.gray)

        if await drawEmbed(currentPage-1) == False:
            left.disabled = True
        if await drawEmbed(currentPage+1) == False:
            right.disabled = True

    # ----------------------------------------------------------------------------------------------------------------------

        async def left_callback(interaction):
            nonlocal currentPage, sent_msg
            currentPage -= 1

            left.disabled = False
            right.disabled = False

            if await drawEmbed(currentPage-1) == False:
                left.disabled = True
            if await drawEmbed(currentPage+1) == True:
                right.disabled = False

            await sent_msg.edit(embed=await drawEmbed(currentPage),view=view)
            await interaction.response.defer()

    # ----------------------------------------------------------------------------------------------------------------------

        async def right_callback(interaction):
            nonlocal currentPage, sent_msg
            currentPage += 1

            left.disabled = False
            right.disabled = False

            if await drawEmbed(currentPage+1) == False:
                right.disabled = True
            if await drawEmbed(currentPage-1) == True:
                left.disabled = False

            await sent_msg.edit(embed=await drawEmbed(currentPage),view=view)
            await interaction.response.defer()

    # ----------------------------------------------------------------------------------------------------------------------

        view = View(timeout=180)
        view.add_item(left)
        view.add_item(right)

        left.callback = left_callback
        right.callback = right_callback

        sent_msg = await ctx.reply(embed=drawnEmbed,view=view)

# ----------------------------------------------------------------------------------------------------------------------

async def setup(client: commands.Bot) -> None:
   await client.add_cog(Help(client))

# ----------------------------------------------------------------------------------------------------------------------

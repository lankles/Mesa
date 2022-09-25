# ----------------------------------------------------------------------------------------------------------------------

# ███╗░░░███╗███████╗░██████╗░█████╗░
# ████╗░████║██╔════╝██╔════╝██╔══██╗
# ██╔████╔██║█████╗░░╚█████╗░███████║
# ██║╚██╔╝██║██╔══╝░░░╚═══██╗██╔══██║
# ██║░╚═╝░██║███████╗██████╔╝██║░░██║
# ╚═╝░░░░░╚═╝╚══════╝╚═════╝░╚═╝░░╚═╝

# lankles - 2021/2022

# ----------------------------------------------------------------------------------------------------------------------

# Libraries
import os
import discord
import json

# Sub-Libraries (not sure if thats what they're called)
from typing import *
from discord.ext import commands
from discord.ext.commands import is_owner

# Intents / Token / App ID
intents = discord.Intents.all()
token = json.load(open('main.json'))['token']
appId = json.load(open('main.json'))['appId']

# ----------------------------------------------------------------------------------------------------------------------

# Class
class Mesa(commands.Bot):

    def __init__(self):
        super().__init__(
            command_prefix = '>',
            intents = intents,
            help_command=None,
            application_id = appId)

    async def setup_hook(self):            
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await self.load_extension(f'cogs.{filename[:-3]}')
                print(f'{filename} is now online.')
        
    async def close(self):
        await super().close()
        await self.session.close()

    async def on_command_error(self, ctx, error):
        await ctx.reply(error, ephemeral = True)

    async def on_ready(self):
        print(f'Logged in as {client.user}')

client = Mesa()

# ----------------------------------------------------------------------------------------------------------------------

@client.command()
@is_owner()
async def reload(ctx: commands.Context,name: str):
    try:
        await client.reload_extension(f'cogs.{name}')
    except:
        await ctx.reply(f'**{name}** does not exist or there was an error processing the reload.')
        return
    await ctx.reply(f'**{name}** has been succesfully reloaded.')

# ----------------------------------------------------------------------------------------------------------------------

@client.command()
@is_owner()
async def sync(
  ctx: commands.Context, guilds: commands.Greedy[discord.Object], spec: Optional[Literal["~", "*", "^"]] = None) -> None:
    if not guilds:
        if spec == "~":
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "*":
            ctx.bot.tree.copy_global_to(guild=ctx.guild)
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "^":
            ctx.bot.tree.clear_commands(guild=ctx.guild)
            await ctx.bot.tree.sync(guild=ctx.guild)
            synced = []
        else:
            synced = await ctx.bot.tree.sync()

        await ctx.send(
            f"Synced **{len(synced)}** commands {'globally.' if spec is None else 'to the current guild.'}"
        )
        return

    ret = 0
    for guild in guilds:
        try:
            await ctx.bot.tree.sync(guild=guild)
        except discord.HTTPException:
            pass
        else:
            ret += 1

    await ctx.send(f"Synced the tree to {ret}/{len(guilds)}.")

# Works like:
# >sync -> global sync
# >sync ~ -> sync current guild
# >sync * -> copies all global app commands to current guild and syncs
# >sync ^ -> clears all commands from the current guild target and syncs (removes guild commands)
# >sync id_1 id_2 -> syncs guilds with id 1 and 2

# ----------------------------------------------------------------------------------------------------------------------

client.run(token)

# ----------------------------------------------------------------------------------------------------------------------

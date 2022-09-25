# ----------------------------------------------------------------------------------------------------------------------

# REDDIT !

# ----------------------------------------------------------------------------------------------------------------------

# Libraries
import discord
import json
import asyncpraw
import random

# Sub-Libraries
from discord.ext import commands
from discord import app_commands
from typing import Optional

# Json
mainJson = json.load(open('main.json'))

clientId = mainJson['reddit']['clientId']
secret = mainJson['reddit']['secret']
username = mainJson['reddit']['username']
password = mainJson['reddit']['password']

reddit = asyncpraw.Reddit(
    client_id = clientId,
    client_secret = secret,
    username = username,
    password = password,
    user_agent = 'Mesa'
)

# ----------------------------------------------------------------------------------------------------------------------

async def subRedditImage(name):
    subreddit = await reddit.subreddit(name,fetch=True)
    allPosts = []

    async for post in subreddit.top(limit=30):
        if (not 'v.' in post.url) and ('i.' in post.url):
            allPosts.append(post)

    if not allPosts:
        failEmbed = discord.Embed(title='No posts could be loaded, there were no images in any of the posts within the query pool.')
        return failEmbed

    randomPost = random.choice(allPosts)
    name = randomPost.title
    url = randomPost.url
        
    embed = discord.Embed(title=name)
    embed.set_image(url=url)

    return embed

# ----------------------------------------------------------------------------------------------------------------------

# Class
class Reddit(commands.Cog):

    # Setup
    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    # ----------------------------------------------------------------------------------------------------------------------

    @commands.hybrid_command(
        name='drake',
        description='Sends a post from r/DrakeTheType.',
    )
    async def drake(self, ctx):
        await ctx.reply(embed=await subRedditImage("DrakeTheType"))

    # ----------------------------------------------------------------------------------------------------------------------

    @commands.hybrid_command(
        name='tf2',
        description='Sends a post from r/givemeinteligens.',
        aliases=['givemeinteligens','inteligens','teamfortress','teamfortress2']
    )
    async def tf2(self, ctx):
        await ctx.reply(embed=await subRedditImage("givemeinteligens"))

    # ----------------------------------------------------------------------------------------------------------------------

    @commands.hybrid_command(
        name='carti',
        description='Sends a post from r/playboicarti.',
        aliases=['playboicarti']
    )
    async def carti(self, ctx):
        await ctx.reply(embed=await subRedditImage("playboicarti"))

    # ----------------------------------------------------------------------------------------------------------------------

    @commands.hybrid_command(
        name='interesting',
        description='Sends a post from r/notinteresting.',
        aliases=['notinteresting']
    )
    async def interesting(self, ctx):
        await ctx.reply(embed=await subRedditImage("notinteresting"))

    # ----------------------------------------------------------------------------------------------------------------------

    @commands.hybrid_command(
        name='lankles',
        description='Sends a post from r/lankles.',
        aliases=['toe']
    )
    async def lankles(self, ctx):
        await ctx.reply(embed=await subRedditImage("lankles"))

    # ----------------------------------------------------------------------------------------------------------------------
    
    @commands.hybrid_command(
        name='lies',
        description='Sends a post from r/lies.',
    )
    async def lies(self, ctx):
        await ctx.reply(embed=await subRedditImage("lies"))

# ----------------------------------------------------------------------------------------------------------------------

async def setup(client: commands.Bot) -> None:
   await client.add_cog(Reddit(client))

# ----------------------------------------------------------------------------------------------------------------------

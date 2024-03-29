# ----------------------------------------------------------------------------------------------------------------------

# ██████╗░░█████╗░███╗░░██╗██████╗░░█████╗░███╗░░░███╗██╗███████╗███████╗██████╗░░██████╗
# ██╔══██╗██╔══██╗████╗░██║██╔══██╗██╔══██╗████╗░████║██║╚════██║██╔════╝██╔══██╗██╔════╝
# ██████╔╝███████║██╔██╗██║██║░░██║██║░░██║██╔████╔██║██║░░███╔═╝█████╗░░██████╔╝╚█████╗░
# ██╔══██╗██╔══██║██║╚████║██║░░██║██║░░██║██║╚██╔╝██║██║██╔══╝░░██╔══╝░░██╔══██╗░╚═══██╗
# ██║░░██║██║░░██║██║░╚███║██████╔╝╚█████╔╝██║░╚═╝░██║██║███████╗███████╗██║░░██║██████╔╝
# ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝╚══════╝╚══════╝╚═╝░░╚═╝╚═════╝░

# ----------------------------------------------------------------------------------------------------------------------

# Libraries
import discord
import random

# Sub-Libraries
from discord.ext import commands
from discord import app_commands

# ----------------------------------------------------------------------------------------------------------------------

# Gifs
gifs = [
    'https://media.discordapp.net/attachments/737875190700048417/784967054875820032/caption.gif',
    'https://media.discordapp.net/attachments/766423934806523914/812466246930268160/caption.gif',
    'https://media.discordapp.net/attachments/422448194476048403/812865246699585576/image0-62.gif',
    'https://media.discordapp.net/attachments/794437275026063400/802304905075359754/rerun.gif',
    'https://media.discordapp.net/attachments/713106201810042890/810312034465611776/kianu_rivz_poyasnyaet.gif',
    'https://media.discordapp.net/attachments/505502848415694868/791707676211806208/image0.gif',
    'https://tenor.com/view/kanye-kanye-west-kanye-south-kanye-north-kanye-east-gif-19964491',
    'https://tenor.com/view/jo-jo-king-crimson-gif-9373135',
    'https://tenor.com/view/doom-gif-12466423',
    'https://media.discordapp.net/attachments/593571138500690013/768258613516828692/20200910_000149.gif',
    'https://media.discordapp.net/attachments/760630379358453798/806241477281185812/image0.gif',
    'https://tenor.com/view/get-real-gif-18506948',
    'https://media.discordapp.net/attachments/728035054403453013/787108205334888498/image0.gif',
    'https://tenor.com/view/among-us-minecraft-farting-cool-among-us-moment-gif-19081926',
    'https://tenor.com/view/osrs-crazy-rng-loot-drop-clue-scroll-gif-16149187',
    'https://thumbs.gfycat.com/RecklessGreatDaddylonglegs-size_restricted.gif',
    'https://cdn.discordapp.com/emojis/769421271829970993.gif?v=1',
    'https://tenor.com/view/walter-white-walter-falling-breaking-bad-dm4uz3-gif-18078549',
    'https://media.discordapp.net/attachments/746480307242533005/814623786799857664/caption.gif'
]

# ----------------------------------------------------------------------------------------------------------------------

# Magic 8-Ball Responses
responses = [
    'As I see it, yes.',
    'Ask again later.',
    'Better not tell you now.',
    'Cannot predict now.',
    'Concentrate and ask again.',
    'Dont count on it.',
    'It is certain.',
    'It is decidedly so.',
    'Most likely.',
    'My reply is no.',
    'My sources say no.',
    'Outlook not so good.',
    'Outlook good.',
    'Reply hazy, try again.',
    'Signs point to yes.',
    'Very doubtful.',
    'Without a doubt.',
    'Yes.',
    'Yes – definitely.',
    'You may rely on it.'
]

# ----------------------------------------------------------------------------------------------------------------------

# Quotes
quotes = [
    'jone',
    'air jordans',
    'drank gorilla glue',
    'Idaho',
    'J',
    'teenage girls with esp',
    'dude.',
    'vac banned',
    'Iced Tea?',
    'scammed a white kid he asked for a refund',
    '7',
    'November 27th, 2020',
    'war owl',
    'Galactus',
    'Hello everybody, my name is Markiplier.',
    'lemon demon',
    'The American Civil War was a long and bloody war that occured between 1861 and 1865 between Iron Man and..',
    'doomguy',
    'ranger quake',
    'resonance cascade',
    'GOD FARTING',
    'mag (winning)',
    'mag',
    'Lankles Studios',
    'kill her. kill her now. kill her.'

]

# ----------------------------------------------------------------------------------------------------------------------

# Xbox Live Generator
entry1 = [
    'fart',
    'blast',
    'doom',
    'cheeko',
    'hotdog',
    'poop',
    'the',
    'nown',
    'pain',
    'mine',
    'ro',
    'faze',
    'xbox',
    'awesome',
    'holy',
]
entry2 = [
    'moncher',
    'reader',
    'slayer',
    'gamer',
    'bringer',
    'bird',
    'tiger',
    'legend',
    'line',
    'god',
    'ripper',
    'shredder',
    'king',
    'sonny',
]
entry3 = [
    'XxX',
    '9000',
    '22',
    '27',
    '1337',
    '_',
    '_ii',
    'X',
]

# ----------------------------------------------------------------------------------------------------------------------

# Dhar Mann videos
dharvideos = [
    'https://www.youtube.com/watch?v=5iKNl7db0Fk',
    'https://www.youtube.com/watch?v=AJha5MSQKjk',
    'https://www.youtube.com/watch?v=adE-sKzHbE4',
    'https://www.youtube.com/watch?v=YBgUNVMXKQ8',
    'https://www.youtube.com/watch?v=X2SAw68Yt_4',
    'https://www.youtube.com/watch?v=hN9ZVy6pb2s',
    'https://www.youtube.com/watch?v=OKgHrTItDNU',
    'https://www.youtube.com/watch?v=gEFmwpWfdAI',
    'https://www.youtube.com/watch?v=dBw0eTkQ5IU',
    'https://www.youtube.com/watch?v=6BfFzCyDf0M',
    'https://www.youtube.com/watch?v=bji0cdIl9YQ',
    'https://www.youtube.com/watch?v=PsBgJc0eVDU',
    'https://www.youtube.com/watch?v=_Ct1Oez-R7U',
    'https://www.youtube.com/watch?v=-L1IekaejfU',
    'https://www.youtube.com/watch?v=0SGnQklLCk0',
    'https://www.youtube.com/watch?v=5mbStEESjdg'
]

# ----------------------------------------------------------------------------------------------------------------------

# Class
class Randomizers(commands.Cog):

    # Setup
    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    # ------------------------------------------------------------------------------------------------------------------

    # Events

    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------

    # Commands

    # ------------------------------------------------------------------------------------------------------------------

    # Gif Command
    @commands.hybrid_command(
        name='gif',
        description='Chooses a random gif to send.'
    )
    async def gif(self, ctx):
        # Picks a gif and sends it.
        newgif = random.choice(gifs)
        await ctx.reply(newgif)

    # Quote Command
    @commands.hybrid_command(
        name='quote',
        description='Chooses a random quote to send.',
        aliases=['quotes']
    )
    async def quote(self, ctx):
        # Picks a quote and sends it.
        newquote = random.choice(quotes)
        await ctx.reply(f'"{newquote}"')

    # Flip Command
    @commands.hybrid_command(
        name='flip',
        description='Gives a random heads or tails answer to simulate a coin flip.',
        aliases=['coin', 'toss']
    )
    async def flip(self, ctx):
        # Picks the answer and sends it.
        randombit = random.getrandbits(1)
        if randombit == 1:
            await ctx.reply('Heads!')
        else:
            await ctx.reply('Tails!')

    # 8-Ball Command
    @commands.hybrid_command(
        name='8ball',
        description='Gives a random Magic 8-Ball answer.',
        aliases=['eight', 'eightball', 'ball']
    )
    async def ball(self, ctx, question: str):
        # Picks the answer and sends it.
        newresponse = random.choice(responses)
        await ctx.reply(f'**Question**: {question}\n**Answer**: {newresponse}')

    # Dhar Command
    @commands.hybrid_command(
        name = "dhar",
        description = "Sends a random Dhar Mann video."
    )
    async def dhar(self, ctx: commands.Context):
        dharvideo = random.choice(dharvideos)
        await ctx.reply(dharvideo)

    # Xbox Live Command
    @commands.hybrid_command(
        name='xbox',
        description='Generates a random Xbox Live username.',
        aliases=['xboxlive']
    )
    async def xbox(self, ctx):
        # Picks a quote and sends it.
        word1 = random.choice(entry1)
        word2 = random.choice(entry2)
        word3 = random.choice(entry3)
        await ctx.reply(f'{word1}{word2}{word3}')


# ----------------------------------------------------------------------------------------------------------------------

async def setup(client: commands.Bot) -> None:
   await client.add_cog(Randomizers(client))

# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------

# ██╗░░░██╗███╗░░██╗██╗░░░░░██╗░██████╗████████╗███████╗██████╗░
# ██║░░░██║████╗░██║██║░░░░░██║██╔════╝╚══██╔══╝██╔════╝██╔══██╗
# ██║░░░██║██╔██╗██║██║░░░░░██║╚█████╗░░░░██║░░░█████╗░░██║░░██║
# ██║░░░██║██║╚████║██║░░░░░██║░╚═══██╗░░░██║░░░██╔══╝░░██║░░██║
# ╚██████╔╝██║░╚███║███████╗██║██████╔╝░░░██║░░░███████╗██████╔╝
# ░╚═════╝░╚═╝░░╚══╝╚══════╝╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═════╝░

# ----------------------------------------------------------------------------------------------------------------------

# Libraries
import discord
import random

# Sub-Libraries
from discord.ext import commands

# ----------------------------------------------------------------------------------------------------------------------

# Dhar Mann Videos
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

# David Screenshots
davidpics = [
    'https://cdn.discordapp.com/attachments/523639860905377807/814679488419725332/unknown.png',
    'https://cdn.discordapp.com/attachments/523639860905377807/814679513145147432/unknown.png',
    'https://cdn.discordapp.com/attachments/523639860905377807/814679547748417556/unknown.png',
    'https://cdn.discordapp.com/attachments/523639860905377807/814679581293412402/Screenshot_20210115-110521.png',
    'https://cdn.discordapp.com/attachments/523639860905377807/814679611258306620/unknown.png',
    'https://cdn.discordapp.com/attachments/523639860905377807/814679654136807424/unknown.png',
    'https://cdn.discordapp.com/attachments/523639860905377807/814679684654694461/unknown.png',
    'https://cdn.discordapp.com/attachments/523639860905377807/814679711963676672/unknown.png',
    'https://cdn.discordapp.com/attachments/523639860905377807/814679762907430923/unknown.png',
    'https://cdn.discordapp.com/attachments/523639860905377807/814679792623419392/unknown.png',
    'https://cdn.discordapp.com/attachments/523639860905377807/814679820436766750/Screenshot_20210212-135955.png',
    'https://cdn.discordapp.com/attachments/523639860905377807/814679873339129856/unknown.png',
    'https://cdn.discordapp.com/attachments/523639860905377807/814679924002258954/unknown.png',
    'https://cdn.discordapp.com/attachments/523639860905377807/814679951714287666/unknown.png',
    'https://cdn.discordapp.com/attachments/523639860905377807/814679986229346366/unknown.png',
    'https://cdn.discordapp.com/attachments/523639860905377807/814680025772064798/unknown.png',
    'https://cdn.discordapp.com/attachments/523639860905377807/814680051223494656/unknown_1.png',
    'https://cdn.discordapp.com/attachments/523639860905377807/814680100846960700/unknown.png',
    'https://cdn.discordapp.com/attachments/523639860905377807/814680188109455390/Screenshot_20201217-025637.png',
    'https://cdn.discordapp.com/attachments/523639860905377807/814680219511816222/Screenshot_20201217-022816.png',
    'https://cdn.discordapp.com/attachments/523639860905377807/814680291398385685/unknown.png',
    'https://cdn.discordapp.com/attachments/523639860905377807/814680318866620456/unknown.png',
    'https://cdn.discordapp.com/attachments/523639860905377807/814680423288143902/unknown.png',
    'https://cdn.discordapp.com/attachments/523639860905377807/814680457705685032/unknown.png',
    'https://cdn.discordapp.com/attachments/523639860905377807/814680539437072444/unknown.png',
    'https://cdn.discordapp.com/attachments/523639860905377807/814680609095417876/unknown.png',
    'https://cdn.discordapp.com/attachments/523639860905377807/814680816743350272/unknown.png',
    'https://cdn.discordapp.com/attachments/523639860905377807/814681173136506890/unknown.png'
]

# ----------------------------------------------------------------------------------------------------------------------

# Class
class UnlistedCmds(commands.Cog):

    # Setup
    def __init__(self, client):
        self.client = client

    # ------------------------------------------------------------------------------------------------------------------

    # Events

    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------

    # Commands

    # ------------------------------------------------------------------------------------------------------------------

    # Tavros Command
    @commands.command()
    async def tavros(self, ctx):
        # Sends the "tavros" gif.
        await ctx.channel.send(
            'https://media.discordapp.net/attachments/570340985452625920/813862319997714472/image0.gif'
        )

    # Hentai Command
    @commands.command()
    async def hentai(self, ctx):
        # Sends the "hentai" gif.
        await ctx.channel.send(
            'https://tenor.com/view/4k-caught-gif-20353888'
        )

    # Ciara Command
    @commands.command()
    async def ciara(self, ctx):
        # Sends the funny hamster image.
        await ctx.channel.send(
            'https://cdn.discordapp.com/attachments/794437275026063400/815006144862486578/20210226_164817.png'
        )

    # Dhar Command
    @commands.command(aliases=['dharmann', 'mann'])
    async def dhar(self, ctx):
        # Sends a random Dhar Mann video.
        dharvideo = random.choice(dharvideos)
        await ctx.channel.send(dharvideo)

    # David Command
    @commands.command()
    async def david(self, ctx):
        # Sends a random David screenshot.
        davidpic = random.choice(davidpics)
        await ctx.channel.send(davidpic)

    # Jone Command
    @commands.command(aliases=['ruka', 'bitsy', 'doxhy', 'cheeko'])
    async def jone(self, ctx):
        # Sends the Jone VAC ban image.
        await ctx.channel.send('https://cdn.discordapp.com/attachments/720122216246673420/827432461554024508/unknown.png')

    # Message Command
    @commands.command()
    async def message(self, ctx, guildid, channelid, *, msg):
        if ctx.guild.id == 818348640451035158:
            # Sends a message in the desired channel
            for guild in self.client.guilds:
                if str(guild.id) == guildid:
                    for channel in guild.channels:
                        if str(channel.id) == channelid:
                            await channel.send(msg)

# ----------------------------------------------------------------------------------------------------------------------

    # Nownline Command
    @commands.command(aliases=['nl', 'nown', 'incident'])
    async def nownline(self, ctx):
        # Sends the nownline copypasta.
        await ctx.channel.send(
            """ [NOWNLINE INCCIDENT]
Start of recording by Dr. ######


It was 9:09 pm of November 1, 2018. The deep facilty known as ####### had caugth an explosin or some sort of light that went for hours. People of ######## believed that something has fallen from the sky by something or someone. It went from 2 hours that the bombing went down and a light emerged from the ground. The bombing was captured with camers surronded the facility and we can give info on what we saw that day. Cam 2 and 3 screen's was all white and cannot identify what was it, but in Cam 4, it showed a beam of ligth from the sky that landed down and created a large ligth outside from the facility. We never know where it came from, but researches theorized and officially called it the "Nownline" incident. Line as in as the Beam that represents a line and Nown as a explosion or ligth. There's surrounding this incident include 3 theories
1. The beaming ligth came from aliens or other worldly spedcimen
2. The beaming ligth was to spawn a creature or "human" of some sort to study as 
3. It was an attack from secret military project, or a warning

All this theories could be true but seems to be this will remain a mystery

END OF RECORDING """
        )

# ----------------------------------------------------------------------------------------------------------------------

def setup(client):
    client.add_cog(UnlistedCmds(client))

# ----------------------------------------------------------------------------------------------------------------------

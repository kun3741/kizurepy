import discord
from discord.ext import commands
import json
import requests
import random
from random import randint

class sad(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sad(self, ctx):

        embed = discord.Embed(title=f'**{ctx.author.name} сумує.**'.format(), color = 0xff4d94)

        SAD = ["https://c.tenor.com/mSqEgKfI3uUAAAAd/my-hero-academia-anime.gif",
        "https://c.tenor.com/dWkr9_iQL8QAAAAC/anime-dan-machi.gif",
        "https://c.tenor.com/p0hJkNOIMukAAAAd/anime-sad.gif",
        "https://c.tenor.com/l3IL3KItyLUAAAAC/sad-anime.gif",
        "https://c.tenor.com/Tn9mzxqYNs4AAAAd/kukuru-misakino-anime.gif",
        "https://c.tenor.com/BTm7whW-C8oAAAAd/anime-sad.gif",
        "https://media3.giphy.com/media/4xKJUTzWPAVoY/giphy.gif",
        "https://media.giphy.com/media/wXo9rzjkBBk7m/giphy.gif",
        "https://38.media.tumblr.com/5265704d641a648b93a508880e28a081/tumblr_n9ig5nxDyM1s4yh14o1_500.gif",
        ]

        embed.set_image(url = random.choice(SAD))
        embed.set_footer(text="Used by {}. | © Kizure, 2022. | Слава Україні.".format(ctx.message.author))
        await ctx.reply(embed=embed)
        author = ctx.message.author
        guild_name = ctx.guild.name
        print(f'[Logs] ', author, 'used command, on ', guild_name, ' | sad' ) 

    @commands.Cog.listener()
    async def on_ready(self):
        print("[Ready] sad")

async def setup(bot):
    await bot.add_cog(sad(bot))
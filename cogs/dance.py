import discord
from discord.ext import commands
import json
import requests
import random
from random import randint

class dance(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dance(self, ctx):
        DANCE = ["https://c.tenor.com/2vRn7mgoMRMAAAAd/cute-anime-dance.gif",
"https://c.tenor.com/OZ6SyQ1S6dsAAAAd/pompo-pompo-the-cinephile.gif",
"https://c.tenor.com/Lkyf9b8203YAAAAC/dragon-maid-kanna-fite.gif",
"https://c.tenor.com/-1YkyYLOuJoAAAAM/rwby-anime.gif",
"https://media0.giphy.com/media/W6dHvprT7oks6BpX5R/giphy.gif?cid=ecf05e47uvxeilo0nh38osspc4mmvo1e2qbzlfk0zu9ufjru&rid=giphy.gif&ct=g",
"https://media1.giphy.com/media/b7l5cvG94cqo8/giphy.gif?cid=ecf05e473hxmjbboh2050qunqdqu3bniqk1mbhuw7dhznhl3&rid=giphy.gif&ct=g",
"https://c.tenor.com/GYjYgE-UCEgAAAAd/shinobu-kocho-dance.gif",
"https://c.tenor.com/tNulr7DcsZAAAAAC/yuru-yuri-kyoko.gif",
"https://c.tenor.com/QwNUEvvKxY8AAAAM/happy-loli.gif"
]

        embed = discord.Embed(title=f'**{ctx.author.name} танцює!**'.format(), color = 0xff4d94)

        embed.set_image(url = random.choice(DANCE))
        embed.set_footer(text="Used by {}. | © Kizure, 2022. | Слава Україні.".format(ctx.message.author.name))
        await ctx.reply(embed=embed)
        author = ctx.message.author
        guild_name = ctx.guild.name
        print(f'[Logs] ', author, 'used command, on ', guild_name, ' | dance' ) 


    @commands.Cog.listener()
    async def on_ready(self):
        print("[Ready] dance")

def setup(bot):
    bot.add_cog(dance(bot))
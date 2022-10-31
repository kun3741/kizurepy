import discord
from discord.ext import commands
import json
import requests
import random
from random import randint

class eat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def eat(self, ctx):
        EAT = ["https://c.tenor.com/4g4c7CE1jkIAAAAd/eat-eats.gif",
"https://c.tenor.com/K-46u3QTNnUAAAAC/anime-food.gif",
"https://c.tenor.com/gz_wbCdkO4AAAAAC/dragon-ball-z-goku.gif",
"https://c.tenor.com/4XzCV-yPOroAAAAC/anime-eating.gif",
"https://c.tenor.com/gQjxza31pxIAAAAd/my-dress-up-darling-anime-eat.gif",
"https://c.tenor.com/ADe3BUYP3jUAAAAd/kobayashi-dragon-maid.gif",
"https://c.tenor.com/uwPmmknc52EAAAAM/inosuke-demon-slayer.gif",
"https://c.tenor.com/MWpSpZnhk2sAAAAd/eat-anime.gif",
"https://c.tenor.com/CQCMmVhDUjkAAAAM/eat-anime.gif",
"https://c.tenor.com/Hu9cJRj74AYAAAAC/sushichaeng-lunch.gif",
]
        embed = discord.Embed(title=f'**{ctx.author.name} їсть.** *смачного)*'.format(), color = 0xff4d94)

        embed.set_image(url = random.choice(EAT))
        embed.set_footer(text="Used by {}. | © Kizure, 2022. | Слава Україні.".format(ctx.message.author))
        await ctx.reply(embed=embed)
        author = ctx.message.author
        guild_name = ctx.guild.name
        print(f'[Logs] ', author, 'used command, on ', guild_name, ' | eat' )  


    @commands.Cog.listener()
    async def on_ready(self):
        print("[Ready] eat")

async def setup(bot):
    await bot.add_cog(eat(bot))
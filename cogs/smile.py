import discord
from discord.ext import commands
import json
import requests
import random
from random import randint

class smile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def smile(self, ctx):
        SMILE = ["https://c.tenor.com/3fAZZncIHDQAAAAC/smile-anime.gif",
"https://c.tenor.com/9BvbcMZFCCMAAAAC/anime-cute.gif",
"https://c.tenor.com/9BvbcMZFCCMAAAAC/anime-cute.gif",
"https://c.tenor.com/Uyki_ZbnmKwAAAAC/hearts-love.gif",
"https://c.tenor.com/yz-QRzyMJ5IAAAAC/anime-boy.gif",
"https://tenor.com/view/02-darling-in-the-franxx-gif-12855275",
"https://c.tenor.com/DVbymBMiCtoAAAAd/omg-happy.gif",
"https://c.tenor.com/Ur_pBB1YBlwAAAAC/himouto-umaru-chan-smile.gif",
"https://c.tenor.com/mTbqykLo0_oAAAAd/kawai-smile.gif",
"https://c.tenor.com/QjfhcnvihvoAAAAC/anime-girl.gif",
"https://c.tenor.com/cNPNbyhXR6MAAAAC/nagatoro-ijiranaide-nagatoro-san.gif",
"https://c.tenor.com/Ul15t3k6ueIAAAAC/love-live-anime.gif",
]
        embed = discord.Embed(title=f'**{ctx.author.name} посміхається.**'.format(), color = 0xff4d94)

        embed.set_image(url = random.choice(SMILE))
        embed.set_footer(text="Used by {}. | © Kizure, 2022. | Слава Україні.".format(ctx.message.author))
        await ctx.reply(embed=embed)
        author = ctx.message.author
        guild_name = ctx.guild.name
        print(f'[Logs] ', author, 'used command, on ', guild_name, ' | smile' )  


    @commands.Cog.listener()
    async def on_ready(self):
        print("[Ready] smile")

async def setup(bot):
    await bot.add_cog(smile(bot))
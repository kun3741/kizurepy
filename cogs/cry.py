import discord
from discord.ext import commands
import json
import requests
import random
from random import randint

class cry(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cey(self, ctx):
        CRY = ["https://c.tenor.com/XBWh-szFwDQAAAAC/crying-naruto-crying.gif",
"https://c.tenor.com/9tOtlaOMTP8AAAAC/sad-cry.gif",
"https://c.tenor.com/kQeYDKr95h4AAAAC/anime-crying-crying-anime.gif",
"https://c.tenor.com/Vs9QNG3lQZUAAAAC/luffy-one-piece.gif",
"https://c.tenor.com/TtSO-_weHb0AAAAC/aqua-anime.gif",
"https://c.tenor.com/2pawKZu4h_oAAAAC/sad-anime.gif",
"https://c.tenor.com/r2DGstl2IWEAAAAC/raiden-shogun-ei.gif",
"https://c.tenor.com/zadstk1Vm_QAAAAC/kaneki-ken.gif",
"https://c.tenor.com/N2qSCBkdracAAAAC/neko-anime.gif",
"https://c.tenor.com/PJPPNrdIWS0AAAAC/sad-anime.gif",
]
        embed = discord.Embed(title=f'**{ctx.author.name} плаче.**'.format(), color = 0xff4d94)

        embed.set_image(url = random.choice(CRY))
        embed.set_footer(text="Used by {}. | © Kizure, 2022. | Слава Україні.".format(ctx.message.author.name))
        await ctx.reply(embed=embed)
        author = ctx.message.author
        guild_name = ctx.guild.name
        print(f'[Logs] ', author, 'used command, on ', guild_name, ' | cry' ) 

 
    @commands.Cog.listener()
    async def on_ready(self):
        print("[Ready] cry")

def setup(bot):
    bot.add_cog(cry(bot))
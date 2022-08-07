import discord
from discord.ext import commands
import json
import requests
import random
from random import randint

class kill(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kill(self, ctx, member: discord.Member = None):
        if member == None:
            await ctx.reply(f":dizzy_face: Error, type a name. ")
            author = ctx.message.author
            guild_name = ctx.guild.name
            print(f'[Logs] ', author, 'used command, on ', guild_name, ' | kill' )
        else:
            KILL = [
"https://c.tenor.com/-UbmVOLixPcAAAAC/killing-anime-girl.gif",
"https://c.tenor.com/py184W4488kAAAAC/anime.gif",
"https://c.tenor.com/_3i8LBmRpWQAAAAC/akame-ga-kill-anime.gif",
"https://c.tenor.com/MRUi4mUxB6gAAAAC/akame-akame-ga-k-ill.gif",
"https://c.tenor.com/wGgDECpN_eMAAAAC/akame-akame-ga-k-ill.gif",
"https://c.tenor.com/G9tCUL5OBcYAAAAC/stab-knife.gif",
"https://c.tenor.com/AGTqt-wXyiEAAAAC/nichijou-minigun.gif",
"https://c.tenor.com/Vja2MkojIgsAAAAC/anime-gun.gif",
"https://c.tenor.com/HrdHCfxprF8AAAAC/alucard-hellsing.gif",
"https://c.tenor.com/4ZWVsqvrLN8AAAAC/shoot-anime.gif",
]

            embed = discord.Embed(title="**{1}** **вбив(-ла)** **{0}**!".format(member.name, ctx.message.author.name), color = 0xff4d94)

            embed.set_image(url = random.choice(KILL))
            embed.set_footer(text="Used by {}. | © Kizure, 2022. | Слава Україні.".format(ctx.message.author.name))
            await ctx.reply(embed=embed)
            author = ctx.message.author
            guild_name = ctx.guild.name
            print(f'[Logs] ', author, 'used command, on ', guild_name, ' | kill' ) 


    @commands.Cog.listener()
    async def on_ready(self):
        print("[Ready] kill")

def setup(bot):
    bot.add_cog(kill(bot))
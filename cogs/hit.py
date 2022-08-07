import discord
from discord.ext import commands
import json
import requests
import random
from random import randint

class hit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hit(self, ctx, member: discord.Member = None):
        if member == None:
            await ctx.reply(f":dizzy_face: Error, type a name. ")
            author = ctx.message.author
            guild_name = ctx.guild.name
            print(f'[Logs] ', author, 'used command, on ', guild_name, ' | hit' )
        else:
            HIT = ["https://c.tenor.com/mKX_7m0GsVAAAAAC/anime-blends.gif", 
"https://c.tenor.com/1T5bgBYtMgUAAAAC/head-hit-anime.gif", 
"https://c.tenor.com/BoYBoopIkBcAAAAC/anime-smash.gif", 
"https://c.tenor.com/6a42QlkVsCEAAAAd/anime-punch.gif", 
"https://c.tenor.com/SwMgGqBirvcAAAAC/saki-saki-kanojo-mo-kanojo.gif"]
            embed = discord.Embed(title="**{1}** **вдарив(-ла)** **{0}**!".format(member.name, ctx.message.author.name), color = 0xff4d94)
            embed.set_image(url = random.choice(HIT))
            embed.set_footer(text="Used by {}. | © Kizure, 2022. | Слава Україні.".format(ctx.message.author.name))
            await ctx.reply(embed=embed)
        author = ctx.message.author
        guild_name = ctx.guild.name
        print(f'[Logs] ', author, 'used command, on ', guild_name, ' | hit' )  


    @commands.Cog.listener()
    async def on_ready(self):
        print("[Ready] hit")

def setup(bot):
    bot.add_cog(hit(bot))
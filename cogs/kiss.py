import discord
from discord.ext import commands
import json
import requests
import random
from random import randint

class kiss(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kiss(self, ctx, member: discord.Member = None):
        if member == None:
            await ctx.reply(f":dizzy_face: Error, type a name. ")
            author = ctx.message.author
            guild_name = ctx.guild.name
            print(f'[Logs] ', author, 'used command, on ', guild_name, ' | kiss' )
        else:
            KISS = ["https://c.tenor.com/woA_lrIFFAIAAAAC/girl-anime.gif", 
"https://c.tenor.com/yoMKK29AMQsAAAAC/kiss-toradora.gif", 
"https://c.tenor.com/I8kWjuAtX-QAAAAC/anime-ano.gif", 
"https://c.tenor.com/7T1cuiOtJvQAAAAC/anime-kiss.gif", 
"https://c.tenor.com/DDmZqcOZJisAAAAC/anime.gif", 
"https://c.tenor.com/06lz817csVgAAAAd/anime-anime-kiss.gif", 
"https://c.tenor.com/-tntwZEqVX4AAAAC/anime-kiss.gif", 
"https://c.tenor.com/TFD0r_HG6-0AAAAC/kiss.gif"]
            embed = discord.Embed(title="**{1}** **поцілував(-ла)** **{0}**!".format(member.name, ctx.message.author.name), color = 0xff4d94)
        embed.set_image(url = random.choice(KISS))
        embed.set_footer(text="Used by {}. | © Kizure, 2022. | Слава Україні.".format(ctx.message.author.name))
        await ctx.reply(embed=embed)
        author = ctx.message.author
        guild_name = ctx.guild.name
        print(f'[Logs] ', author, 'used command, on ', guild_name, ' | kiss' ) 


    @commands.Cog.listener()
    async def on_ready(self):
        print("[Ready] kiss")

def setup(bot):
    bot.add_cog(kiss(bot))
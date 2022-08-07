import discord
from discord.ext import commands
import json
import requests
import random
from random import randint

class smoke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def smoke(self, ctx):
        embed = discord.Embed(title=f'**{ctx.author.name} закурив...** *може не треба?*'.format(), color = 0xff4d94)
        
        SMOKE = ["https://c.tenor.com/RL5ROk4bVNgAAAAd/billy-herrington-smoke.gif",
    "https://c.tenor.com/9tLxGl8P7aoAAAAC/gachi-billy-herington.gif",
    "https://c.tenor.com/QPLc-5gr3N8AAAAC/smoke-cigarette.gif", 
    "https://c.tenor.com/RyUSvLm258kAAAAC/anime-anime-smoke.gif", 
    "https://c.tenor.com/ZQ5Loe2l6X4AAAAd/anime-smoke.gif", 
    "https://c.tenor.com/_qbIz6NeIHsAAAAC/jigen-daisuke-jigen.gif", 
    "https://c.tenor.com/4SdzFn8byTMAAAAC/anime-valirwave.gif", 
    "https://c.tenor.com/Kmq7jfEn63wAAAAd/anime-smoking.gif", 
    "https://c.tenor.com/oyy5Bveck-sAAAAC/madoka-kimagure-orange-road.gif", 
    "https://media.giphy.com/media/z7jERhxsLL6WA/giphy.gif", 
    "https://media.giphy.com/media/MI9vTrc4TUvII/giphy.gif", 
    "https://media.giphy.com/media/4ilFRqgbzbx4c/giphy.gif"]

        embed.set_image(url = random.choice(SMOKE))
        embed.set_footer(text="Used by {}. | © Kizure, 2022. | Слава Україні.".format(ctx.message.author.name))
        await ctx.reply(embed=embed)
        author = ctx.message.author
        guild_name = ctx.guild.name
        print(f'[Logs] ', author, 'used command, on ', guild_name, ' | smoke' )  


    @commands.Cog.listener()
    async def on_ready(self):
        print("[Ready] smoke")

def setup(bot):
    bot.add_cog(smoke(bot))
import discord
from discord.ext import commands
import json
import requests
import random
from random import randint

class hug(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hug(ctx, member: discord.Member = None):
        response = requests.get('https://some-random-api.ml/animu/hug') 
        json_data = json.loads(response.text) 

        author_name = ctx.message.author.name
        if member == None:
            await ctx.reply(f":dizzy_face: Error, type a name. ")
            author = ctx.message.author
            guild_name = ctx.guild.name
        else:
            embed = discord.Embed(color = 0xff4d94, title =  f'{author_name} обняв(-ла) {member.name}!') 
            embed.set_image(url = json_data['link'])
            embed.set_footer(text="Used by {}. | © Kizure, 2022. | Слава Україні.".format(ctx.message.author.name))
            await ctx.reply(embed=embed)
        author = ctx.message.author
        guild_name = ctx.guild.name
        print(f'[Logs] ', author, 'used command, on ', guild_name, ' | hug' ) 


    @commands.Cog.listener()
    async def on_ready(self):
        print("[Ready] hug")

def setup(bot):
    bot.add_cog(hug(bot))
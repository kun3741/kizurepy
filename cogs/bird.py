import discord
from discord.ext import commands
import json
import requests

class bird(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def bird(self, ctx):
        author = ctx.message.author
        guild_name = ctx.guild.name
        response = requests.get('https://some-random-api.ml/img/bird') 
        json_data = json.loads(response.text) 

        embed = discord.Embed(color = 0xff4d94, title = 'Пташечка!🐦') 
        embed.set_image(url = json_data['link'])
        embed.set_footer(text="Used by {}. | © Kizure, 2022. | Слава Україні.".format(ctx.message.author)) 
        await ctx.reply(embed=embed) 
        print(f'[Logs] ', author, 'used command, on ', guild_name, ' | bird' )


    @commands.Cog.listener()
    async def on_ready(self):
        print("[Ready] bird")

async def setup(bot):
    await bot.add_cog(bird(bot))
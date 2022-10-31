import discord
from discord.ext import commands
import json
import requests

class panda(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def panda(self, ctx):
        response = requests.get('https://some-random-api.ml/img/panda') 
        json_data = json.loads(response.text) 

        embed = discord.Embed(color = 0xff4d94, title = 'Панда!🐼') 
        embed.set_image(url = json_data['link'])
        embed.set_footer(text="Used by {}. | © Kizure, 2022. | Слава Україні.".format(ctx.message.author)) 
        await ctx.reply(embed=embed)
        author = ctx.message.author
        guild_name = ctx.guild.name
        print(f'[Logs] ', author, 'used command, on ', guild_name, ' | panda' ) 


    @commands.Cog.listener()
    async def on_ready(self):
        print("[Ready] panda")

async def setup(bot):
    await bot.add_cog(panda(bot))
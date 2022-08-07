import discord
from discord.ext import commands
import json
import requests

class rpanda(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def rpanda(self, ctx):
        response = requests.get('https://some-random-api.ml/img/red_panda') 
        json_data = json.loads(response.text) 

        embed = discord.Embed(color = 0xff4d94, title = 'Червона панда!🐻') 
        embed.set_image(url = json_data['link'])
        embed.set_footer(text="Used by {}. | © Kizure, 2022. | Слава Україні.".format(ctx.message.author.name)) 
        await ctx.reply(embed=embed)
        author = ctx.message.author
        guild_name = ctx.guild.name
        print(f'[Logs] ', author, 'used command, on ', guild_name, ' | rpanda' ) 


    @commands.Cog.listener()
    async def on_ready(self):
        print("[Ready] rpanda")

def setup(bot):
    bot.add_cog(rpanda(bot))
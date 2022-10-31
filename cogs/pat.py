import discord
from discord.ext import commands
import json
import requests

class pat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def pat(self, ctx, member: discord.Member = None):
        response = requests.get('https://some-random-api.ml/animu/pat') 
        json_data = json.loads(response.text) 

        author_name = ctx.message.author.name
        if member == None:
            await ctx.reply(f":dizzy_face: Error, type a name. ")
        else:
            embed = discord.Embed(color = 0xff4d94, title =  f'{author_name} погладив(-ла) {member.name}!') 
            embed.set_image(url = json_data['link']) 
            embed.set_footer(text="Used by {}. | © Kizure, 2022. | Слава Україні.".format(ctx.message.author))
            await ctx.reply(embed=embed)
        author = ctx.message.author
        guild_name = ctx.guild.name
        print(f'[Logs] ', author, 'used command, on ', guild_name, ' | pat' ) 


    @commands.Cog.listener()
    async def on_ready(self):
        print("[Ready] pat")

async def setup(bot):
    await bot.add_cog(pat(bot))
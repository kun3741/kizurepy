import discord
from discord.ext import commands
import random
from random import randint

class numb(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def numb(self, ctx):
        random_number = str(randint(0, 1000))
        embed = discord.Embed(title=f'**{ctx.author.name}, твоє рандомне число: **' + random_number, color = 0xff4d94)
        embed.set_footer(text="Used by {}. | © Kizure, 2022. | Слава Україні.".format(ctx.message.author.name))
        await ctx.reply(embed=embed)
        

        author = ctx.message.author
        guild_name = ctx.guild.name
        print(f'[Logs] ', author, 'used command, on ', guild_name, ' | numb' )
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("[Ready] numb") 

def setup(bot):
    bot.add_cog(numb(bot))
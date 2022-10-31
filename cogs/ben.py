import discord
from discord.ext import commands
import random

class ben(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ben(self, ctx, question):
        BEN = ["https://c.tenor.com/x2u_MyapWvcAAAAM/no.gif",
"https://c.tenor.com/6St4vNHkyrcAAAAM/yes.gif",
"https://c.tenor.com/agrQMQjQTzgAAAAM/talking-ben-laugh.gif",
"https://c.tenor.com/aomZLSiXCQ8AAAAM/ugh.gif",
]
        embed = discord.Embed(title=f'**{ctx.author.name}, Бен каже...**'.format(), color = 0xff4d94)
        embed.set_image(url = random.choice(BEN))
        embed.set_footer(text="Used by {}. | © Kizure, 2022. | Слава Україні.".format(ctx.message.author))
        await ctx.reply(embed=embed)

        author = ctx.message.author
        guild_name = ctx.guild.name
        print(f'[Logs] ', author, 'used command, on ', guild_name, ' | ben' )
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("[Ready] ben") 

async def setup(bot):
    await bot.add_cog(ben(bot))
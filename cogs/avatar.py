import discord
from discord.ext import commands
import json


class avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def avatar(ctx, member: discord.Member  = None):
        if member == None:
            member = ctx.author
        embed = discord.Embed(color = 0xff4d94, title = f"Аватар {member.name}")
        embed.set_image(url = member.avatar_url)
        embed.set_footer(text="Used by {}. | © Kizure, 2022. | Слава Україні.".format(ctx.message.author.name))
        await ctx.reply(embed=embed)
        author = ctx.message.author
        guild_name = ctx.guild.name
        print(f'[Logs] ', author, 'used command, on ', guild_name, ' | avatar' ) 


    @commands.Cog.listener()
    async def on_ready(self):
        print("[Ready] avatar")

def setup(bot):
    bot.add_cog(avatar(bot))
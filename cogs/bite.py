import discord
from discord.ext import commands
import json
import requests
import random
from random import randint

class bite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bite(self, ctx, member: discord.Member = None):
        if member == None:
            await ctx.reply(f":dizzy_face: Error, type a name. ")
            author = ctx.message.author
            guild_name = ctx.guild.name
            print(f'[Logs] ', author, 'used command, on ', guild_name, ' | bite' )
        else:
            BITE = ["https://cdn.discordapp.com/attachments/1039211396589690891/1043634862768275506/4c6aca5f44b08a8a0e71d9e01dc1b52b.gif",
"https://cdn.discordapp.com/attachments/1039211396589690891/1043634863116394557/bite-anime.gif",
"https://cdn.discordapp.com/attachments/1039211396589690891/1043634863435165799/zero-no-tsukaima-bite.gif",
"https://cdn.discordapp.com/attachments/1039211396589690891/1043634863741354045/anime-bite-1.gif",
"https://cdn.discordapp.com/attachments/1039211396589690891/1043634864060117022/arms-bite.gif",
"https://cdn.discordapp.com/attachments/1039211396589690891/1043634864374693928/38f541ca5c7880b947ea0345e4603a0f1418360963_full.gif",
"https://cdn.discordapp.com/attachments/1039211396589690891/1043634864731201607/anime-love.gif",
"https://cdn.discordapp.com/attachments/1039211396589690891/1043634865075138660/anime-bite.gif",
"https://cdn.discordapp.com/attachments/1039211396589690891/1043634865804943430/50debfff9508be43a39c3945cd078aedc6a680a2_hq.gif",
"https://cdn.discordapp.com/attachments/1039211396589690891/1043635119266734090/giphy.gif"
]
            embed = discord.Embed(title="**{1}** **вкусив(-ла)** **{0}**!".format(member.name, ctx.message.author.name), color = 0xff4d94)
        embed.set_image(url = random.choice(BITE))
        embed.set_footer(text="Used by {}. | © Kizure, 2022. | Слава Україні.".format(ctx.message.author))
        await ctx.reply(embed=embed)
        author = ctx.message.author
        guild_name = ctx.guild.name
        print(f'[Logs] ', author, 'used command, on ', guild_name, ' | bite' ) 


    @commands.Cog.listener()
    async def on_ready(self):
        print("[Ready] bite")

async def setup(bot):
    await bot.add_cog(bite(bot))
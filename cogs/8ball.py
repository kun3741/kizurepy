import discord
from discord.ext import commands
import random

class ball(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ball(self, ctx, question):
        responses = ['👍Я бачу, що так.',
                '✅Так.',
                '👍Очевидно, що так.',
                '👍Я думаю - так.',
                '✅Впевнений.',
                '👍Швидше за все.',
                '👍Шанси високі.',
                '👎Ні.',
                '😒Очевидно, що ні.',
                '❌Не переконаний.',
                '😒Можливо.',
                '👎Не думаю.',
                '🤷Напевно',
                '🚫Я не можу зараз відповісти.',
                '🥱Мені лінь, давай пізніше.',
                '😪Я сплю, давай пізніше.']
        fortune = random.choice(responses)
        embed=discord.Embed(title="🎱Магічна кулька заговорила!🎱", color = 0xff4d94)
        embed.add_field(name=f'*{ctx.author.name}, кулька говорить...*', value=f'**{fortune}**')
        embed.set_footer(text="Used by {}. | © Kizure, 2022. | Слава Україні.".format(ctx.message.author.name))
        await ctx.reply(embed=embed)
        author = ctx.message.author
        guild_name = ctx.guild.name
        print(f'[Logs] ', author, 'used command, on ', guild_name, ' | ball |', {fortune} ) 
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("[Ready] 8ball") 

def setup(bot):
    bot.add_cog(ball(bot))
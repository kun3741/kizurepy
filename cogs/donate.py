import discord
from discord.ext import commands

class donate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def donate(self, ctx):
        author = ctx.message.author
        guild_name = ctx.guild.name
        

        embed = discord.Embed(color = 0xff4d94, title = '''Support me here:
        https://donatello.to/kun3741
    Or scan a QR-code.''')
        embed.set_image(url = "https://media.discordapp.net/attachments/1005127125327687800/1005132430946091048/Screenshot_2022-08-05_at_18-17-04_kun3741.png")
        embed.set_footer(text="Used by {}. | © Kizure, 2022. | Слава Україні.".format(ctx.message.author.name))
        await ctx.reply(embed=embed) 
        print(f'[Logs] ', author, 'used command on', guild_name, ' | donate' )
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("ready")
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("[Ready] donate")

def setup(bot):
    bot.add_cog(donate(bot))
        
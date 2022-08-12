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
        embed.set_image(url = "https://images-ext-2.discordapp.net/external/X7o3Rql3oBqEl7LH3ZWY-Im4E3yHzVWCyiLzd7ev5nQ/https/i.imgur.com/KrFHwsr.png")
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
        

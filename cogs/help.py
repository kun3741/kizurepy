import discord
from discord.ext import commands

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def cmd(self, ctx): 
        author = ctx.message.author
        guild_name = ctx.guild.name
        
        await ctx.send(f"""Here all my commands: 
        **https://bit.ly/cmd-kizure**""")
        print(f'[Logs] ', author, 'used command on', guild_name, ' | cmd' )


    @commands.command() 
    async def help(self, ctx): 
        author = ctx.message.author
        guild_name = ctx.guild.name 

        await ctx.send(f"""Here all my commands: 
        **https://bit.ly/cmd-kizure**""")
        print(f'[Logs] ', author, 'used command on', guild_name, ' | help' )
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("[Ready] cmd & help")

def setup(bot):
    bot.add_cog(help(bot))
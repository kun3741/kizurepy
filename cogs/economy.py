import discord
from discord.ext import commands
from config import settings
import sqlite3


connection = sqlite3.connect("server.db")
cursor = connection.cursor()


    



class bal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases = ['balance', 'bal'])
    async def __balance(self, ctx, member: discord.Member = None):
        author = ctx.message.author
        guild_name = ctx.guild.name
        author_id = ctx.author.id


        if member is None:
            await ctx.reply(embed = discord.Embed(
                description = f"""Balance **{author}**: **{cursor.execute("SELECT cash FROM users WHERE id = {}".format(author_id)).fetchone()[0]}**:butterfly:"""
                
            ))
        else:
            await ctx.reply(embed = discord.Embed(
                description = f"""Balance **{member}**: **{cursor.execute("SELECT cash FROM users WHERE id = {}".format(member.id)).fetchone()[0]}**:butterfly:"""
               
            ))

        print(f'[Logs] ', author, 'used command on', guild_name, ' | balance' )
        
        
    @commands.Cog.listener()
    async def on_ready(self):
        
        print("[Ready] bal & balance")

async def setup(bot):
    await bot.add_cog(bal(bot))
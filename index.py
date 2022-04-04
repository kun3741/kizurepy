import discord
from discord.ext import commands
from config import settings
import random
import json
import requests
import os
from discord.utils import get
from discord import FFmpegPCMAudio
from os import system


# PREFIX
bot = commands.Bot(command_prefix = settings['prefix'])
# slash = interactions.Client(token = settings['prefix'])
# slash = SlashCommand(bot, sync_commands = True)

bot.remove_command('help')

# COMMANDS
@bot.command() 
async def ll(ctx): 
    author = ctx.message.author 

    await ctx.send(f'марк лох')



@bot.command() 
async def rex(ctx): 
    author = ctx.message.author 

    await ctx.send(f'<@!781577827043508255>')

@bot.command() 
async def cmd(ctx): 
    author = ctx.message.author 

    await ctx.send(f"""Here all my commands: 
    **https://bit.ly/cmd-kizure**""")

@bot.command() 
async def help(ctx): 
    author = ctx.message.author 

    await ctx.send(f"""Here all my commands: 
    **https://bit.ly/cmd-kizure**""")



 


@bot.command()
async def rusboat(ctx):

    embed = discord.Embed(title="🇺🇦", color = 0xad4458)

    embed.set_image(url = "https://st.kashalot.com/img/club/2022/02/28/62-558f5baf-club.png")
    await ctx.send(embed = embed)

@bot.command()
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/fox') 
    json_data = json.loads(response.text) 

    embed = discord.Embed(color = 0xad4458, title = 'Лисичка!🦊') 
    embed.set_image(url = json_data['link']) 
    await ctx.send(embed = embed) 

@bot.command()
async def dog(ctx):
    response = requests.get('https://some-random-api.ml/img/dog') 
    json_data = json.loads(response.text) 

    embed = discord.Embed(color = 0xad4458, title = 'Песик!🐶') 
    embed.set_image(url = json_data['link']) 
    await ctx.send(embed = embed) 

@bot.command()
async def cat(ctx):
    response = requests.get('https://some-random-api.ml/img/cat') 
    json_data = json.loads(response.text) 
   

    embed = discord.Embed(color = 0xad4458, title = 'Котик!😼', description = '\u200b') 
    #js = await r.json()
    #await channel.send(js['link'])
    embed.set_image(url = json_data['link']) 
    await ctx.send(embed = embed) 



#@slash.slash(
 #   name="cat",
  #  description="Cat!",
   # options = [{"name": "member", "description": "пользователь", "type": 6, "requied": False}],
    #guild_ids = [917378869516959794]
#)   
#async def cat(ctx: interactions.CommandContext ):
 #   response = requests.get('https://some-random-api.ml/img/cat') 
  #  json_data = json.loads(response.text) 
#
 ##   embed = discord.Embed(color = 0xad4458, title = 'Котик!😼') 
   # embed.set_image(url = json_data['link']) 
    #await ctx.send(embed = embed) 

@bot.command()
async def bird(ctx):
    response = requests.get('https://some-random-api.ml/img/bird') 
    json_data = json.loads(response.text) 

    embed = discord.Embed(color = 0xad4458, title = 'Пташечка!🐦') 
    embed.set_image(url = json_data['link']) 
    await ctx.send(embed = embed) 

@bot.command()
async def panda(ctx):
    response = requests.get('https://some-random-api.ml/img/panda') 
    json_data = json.loads(response.text) 

    embed = discord.Embed(color = 0xad4458, title = 'Панда!🐼') 
    embed.set_image(url = json_data['link']) 
    await ctx.send(embed = embed) 

@bot.command()
async def rpanda(ctx):
    response = requests.get('https://some-random-api.ml/img/red_panda') 
    json_data = json.loads(response.text) 

    embed = discord.Embed(color = 0xad4458, title = 'Червона панда!🐻') 
    embed.set_image(url = json_data['link']) 
    await ctx.send(embed = embed)

@bot.command()
async def pat(ctx, member: discord.Member):
    response = requests.get('https://some-random-api.ml/animu/pat') 
    json_data = json.loads(response.text) 

    author_name = ctx.message.author.name
    embed = discord.Embed(color = 0xad4458, title =  f'{author_name} погладив(-ла) {member.name}!') 
    embed.set_image(url = json_data['link']) 
    await ctx.send(embed = embed)

@bot.command()
async def hug(ctx, member: discord.Member):
    response = requests.get('https://some-random-api.ml/animu/hug') 
    json_data = json.loads(response.text) 

    author_name = ctx.message.author.name
    embed = discord.Embed(color = 0xad4458, title =  f'{author_name} обняв(-ла) {member.name}!') 
    embed.set_image(url = json_data['link'])
    await ctx.send(embed = embed)

HIT = ["https://c.tenor.com/mKX_7m0GsVAAAAAC/anime-blends.gif", "https://c.tenor.com/1T5bgBYtMgUAAAAC/head-hit-anime.gif", "https://c.tenor.com/BoYBoopIkBcAAAAC/anime-smash.gif", "https://c.tenor.com/6a42QlkVsCEAAAAd/anime-punch.gif", "https://c.tenor.com/SwMgGqBirvcAAAAC/saki-saki-kanojo-mo-kanojo.gif"]


@bot.command()
async def hit(ctx, member: discord.Member):

    embed = discord.Embed(title="**{1}** **вдарив(-ла)** **{0}**!".format(member.name, ctx.message.author.name), color = 0xad4458)

    embed.set_image(url = random.choice(HIT))
    await ctx.send(embed=embed)


KISS = ["https://c.tenor.com/woA_lrIFFAIAAAAC/girl-anime.gif", "https://c.tenor.com/yoMKK29AMQsAAAAC/kiss-toradora.gif", "https://c.tenor.com/I8kWjuAtX-QAAAAC/anime-ano.gif", "https://c.tenor.com/7T1cuiOtJvQAAAAC/anime-kiss.gif", "https://c.tenor.com/DDmZqcOZJisAAAAC/anime.gif", "https://c.tenor.com/06lz817csVgAAAAd/anime-anime-kiss.gif", "https://c.tenor.com/-tntwZEqVX4AAAAC/anime-kiss.gif", "https://c.tenor.com/TFD0r_HG6-0AAAAC/kiss.gif", ""]

@bot.command()
async def kiss(ctx, member: discord.Member):

    embed = discord.Embed(title="**{1}** **поцілував(-ла)** **{0}**!".format(member.name, ctx.message.author.name), color = 0xad4458)

    embed.set_image(url = random.choice(KISS))
    await ctx.send(embed=embed)

#@bot.command()
#async def hentai(ctx):
 #   response = requests.get('https://www.programmershouse-api.ga/hentai?key=KunKey') 
  #  json_data = json.loads(response.text) 
#
 #   embed = discord.Embed(color = 0xad4458, title = 'ух єбать') 
  #  embed.set_image(url = json_data['ukraine']) 
   # await ctx.send(embed = embed) 



# MUSIC




# STATUS
from asyncio import sleep
@bot.event
async def on_ready():
    print("───────────────── • ─────────────────")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Ready. Kizure. <3")
    print("⠀⠀Login in", "'", settings['id'], "'", "id")
    print("⠀⠀⠀⠀⠀⠀", settings['site'])
    print("───────────────── • ─────────────────")
    while True:
        await bot.change_presence(status=discord.Status.online,activity=discord.Game("Слава Україні!"))
        await sleep(20)
        await bot.change_presence(status=discord.Status.idle,activity=discord.Game("Minecraft"))
        await sleep(20)
        await bot.change_presence(status=discord.Status.dnd,activity=discord.Game("k.help"))
        await sleep(20)


bot.run(settings['token'])






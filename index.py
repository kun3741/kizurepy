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

HIT = ["https://c.tenor.com/mKX_7m0GsVAAAAAC/anime-blends.gif", 
"https://c.tenor.com/1T5bgBYtMgUAAAAC/head-hit-anime.gif", 
"https://c.tenor.com/BoYBoopIkBcAAAAC/anime-smash.gif", 
"https://c.tenor.com/6a42QlkVsCEAAAAd/anime-punch.gif", 
"https://c.tenor.com/SwMgGqBirvcAAAAC/saki-saki-kanojo-mo-kanojo.gif"]


@bot.command()
async def hit(ctx, member: discord.Member):

    embed = discord.Embed(title="**{1}** **вдарив(-ла)** **{0}**!".format(member.name, ctx.message.author.name), color = 0xad4458)

    embed.set_image(url = random.choice(HIT))
    await ctx.send(embed=embed)


KISS = ["https://c.tenor.com/woA_lrIFFAIAAAAC/girl-anime.gif", 
"https://c.tenor.com/yoMKK29AMQsAAAAC/kiss-toradora.gif", 
"https://c.tenor.com/I8kWjuAtX-QAAAAC/anime-ano.gif", 
"https://c.tenor.com/7T1cuiOtJvQAAAAC/anime-kiss.gif", 
"https://c.tenor.com/DDmZqcOZJisAAAAC/anime.gif", 
"https://c.tenor.com/06lz817csVgAAAAd/anime-anime-kiss.gif", 
"https://c.tenor.com/-tntwZEqVX4AAAAC/anime-kiss.gif", 
"https://c.tenor.com/TFD0r_HG6-0AAAAC/kiss.gif"]

@bot.command()
async def kiss(ctx, member: discord.Member):

    embed = discord.Embed(title="**{1}** **поцілував(-ла)** **{0}**!".format(member.name, ctx.message.author.name), color = 0xad4458)

    embed.set_image(url = random.choice(KISS))
    await ctx.send(embed=embed)

SMOKE = ["https://c.tenor.com/RL5ROk4bVNgAAAAd/billy-herrington-smoke.gif",
"https://c.tenor.com/9tLxGl8P7aoAAAAC/gachi-billy-herington.gif",
"https://c.tenor.com/QPLc-5gr3N8AAAAC/smoke-cigarette.gif", 
"https://c.tenor.com/RyUSvLm258kAAAAC/anime-anime-smoke.gif", 
"https://c.tenor.com/ZQ5Loe2l6X4AAAAd/anime-smoke.gif", 
"https://c.tenor.com/_qbIz6NeIHsAAAAC/jigen-daisuke-jigen.gif", 
"https://c.tenor.com/4SdzFn8byTMAAAAC/anime-valirwave.gif", 
"https://c.tenor.com/Kmq7jfEn63wAAAAd/anime-smoking.gif", 
"https://c.tenor.com/oyy5Bveck-sAAAAC/madoka-kimagure-orange-road.gif", 
"https://media.giphy.com/media/z7jERhxsLL6WA/giphy.gif", 
"https://media.giphy.com/media/MI9vTrc4TUvII/giphy.gif", 
"https://media.giphy.com/media/4ilFRqgbzbx4c/giphy.gif"]

@bot.command(name='smoke', description='Закури\n')
async def smoke(ctx):

    embed = discord.Embed(title=f'**{ctx.author.name} закурив...** *може не треба?*'.format(), color = 0xad4458)

    embed.set_image(url = random.choice(SMOKE))
    await ctx.send(embed=embed)


SAD = ["https://c.tenor.com/mSqEgKfI3uUAAAAd/my-hero-academia-anime.gif",
"https://c.tenor.com/dWkr9_iQL8QAAAAC/anime-dan-machi.gif",
"https://c.tenor.com/p0hJkNOIMukAAAAd/anime-sad.gif",
"https://c.tenor.com/l3IL3KItyLUAAAAC/sad-anime.gif",
"https://c.tenor.com/Tn9mzxqYNs4AAAAd/kukuru-misakino-anime.gif",
"https://c.tenor.com/BTm7whW-C8oAAAAd/anime-sad.gif",
"https://media3.giphy.com/media/4xKJUTzWPAVoY/giphy.gif",
"https://media.giphy.com/media/wXo9rzjkBBk7m/giphy.gif",
"https://38.media.tumblr.com/5265704d641a648b93a508880e28a081/tumblr_n9ig5nxDyM1s4yh14o1_500.gif",
]

@bot.command(name='sad', description='Сум\n')
async def sad(ctx):

    embed = discord.Embed(title=f'**{ctx.author.name} сумує.**'.format(), color = 0xad4458)

    embed.set_image(url = random.choice(SAD))
    await ctx.send(embed=embed)


SMILE = ["https://c.tenor.com/3fAZZncIHDQAAAAC/smile-anime.gif",
"https://c.tenor.com/9BvbcMZFCCMAAAAC/anime-cute.gif",
"https://c.tenor.com/9BvbcMZFCCMAAAAC/anime-cute.gif",
"https://c.tenor.com/Uyki_ZbnmKwAAAAC/hearts-love.gif",
"https://c.tenor.com/yz-QRzyMJ5IAAAAC/anime-boy.gif",
"https://tenor.com/view/02-darling-in-the-franxx-gif-12855275",
"https://c.tenor.com/DVbymBMiCtoAAAAd/omg-happy.gif",
"https://c.tenor.com/Ur_pBB1YBlwAAAAC/himouto-umaru-chan-smile.gif",
"https://c.tenor.com/mTbqykLo0_oAAAAd/kawai-smile.gif",
"https://c.tenor.com/QjfhcnvihvoAAAAC/anime-girl.gif",
"https://c.tenor.com/cNPNbyhXR6MAAAAC/nagatoro-ijiranaide-nagatoro-san.gif",
"https://c.tenor.com/Ul15t3k6ueIAAAAC/love-live-anime.gif",
]


@bot.command(name='smile', description='Посмішка\n')
async def smile(ctx):

    embed = discord.Embed(title=f'**{ctx.author.name} посміхається.**'.format(), color = 0xad4458)

    embed.set_image(url = random.choice(SMILE))
    await ctx.send(embed=embed)


CRY = ["https://c.tenor.com/XBWh-szFwDQAAAAC/crying-naruto-crying.gif",
"https://c.tenor.com/9tOtlaOMTP8AAAAC/sad-cry.gif",
"https://c.tenor.com/kQeYDKr95h4AAAAC/anime-crying-crying-anime.gif",
"https://c.tenor.com/Vs9QNG3lQZUAAAAC/luffy-one-piece.gif",
"https://c.tenor.com/TtSO-_weHb0AAAAC/aqua-anime.gif",
"https://c.tenor.com/2pawKZu4h_oAAAAC/sad-anime.gif",
"https://c.tenor.com/r2DGstl2IWEAAAAC/raiden-shogun-ei.gif",
"https://c.tenor.com/zadstk1Vm_QAAAAC/kaneki-ken.gif",
"https://c.tenor.com/N2qSCBkdracAAAAC/neko-anime.gif",
"https://c.tenor.com/PJPPNrdIWS0AAAAC/sad-anime.gif",]


@bot.command(name='cry', description='Поплач\n')
async def cry(ctx):

    embed = discord.Embed(title=f'**{ctx.author.name} плаче.**'.format(), color = 0xad4458)

    embed.set_image(url = random.choice(CRY))
    await ctx.send(embed=embed)





@bot.command(name='8ball', description='Кулька передбачувань\n')
async def _8ball(ctx, question):
    icon_url = 'https://i.imgur.com/XhNqADi.png'
    responses = ['Я бачу, що так.',
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
    embed=discord.Embed(title="🎱Магічна кулька заговорила!🎱", color = 0xad4458)
    embed.add_field(name=f'*{ctx.author.name}, кулька говорить...*', value=f'**{fortune}**')
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






import discord
from discord.ext import commands
from config import settings
import os
import asyncio
from asyncio import sleep

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = settings['prefix'], intents=intents)

bot.remove_command("help")

@bot.command(name='ping', description="Ping")
async def ping(ctx):
    ping = bot.ws.latency
    embed = discord.Embed(description=f'Pong! `{ping * 1000:.0f}ms` :ping_pong:', colour=(0xff4d94))
    await ctx.reply(embed=embed)
    embed.set_footer(text="Used by {}. | © Kizure, 2022. | Слава Україні.".format(ctx.message.author.name))
    print(f'[Logs] Ping == {ping * 1000:.0f}ms | ping')


@bot.command(name='load', description='Load Cogs')
async def load(ctx, extension):
    if ctx.author.id == settings['owner_id']:
        bot.load_extension(f"cogs.{extension}")
        await ctx.send("Cogs is loaded.")
    else:
        await ctx.send("You are not allowed to use this command.")

@bot.command(name='unload', description='UNLoad Cogs')
async def load(ctx, extension):
    if ctx.author.id == settings['owner_id']:
        bot.unload_extension(f"cogs.{extension}")
        await ctx.send("Cogs is unloaded.")
    else:
        await ctx.send("You are not allowed to use this command.")

@bot.command(name='reload', description='RELoad Cogs')
async def load(ctx, extension):
    if ctx.author.id == settings['owner_id']:
        bot.unload_extension(f"cogs.{extension}")
        bot.load_extension(f"cogs.{extension}")
        await ctx.send("Cogs is reloaded.")
    else:
        await ctx.send("You are not allowed to use this command.")


async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")



@bot.event
async def on_ready():
    print(" ")
    print("───────────────── • ─────────────────")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Ready. Kizure. <3")
    print("⠀⠀Login in", "'", settings['id'], "'", "id")
    print("⠀⠀⠀⠀⠀⠀", settings['site'])
    print("───────────────── • ─────────────────")
    await sleep(0.7)
    print("Total amount commands: 23")
    print("─────────────────────────────────────")
    while True:
        await bot.change_presence(status=discord.Status.online,activity=discord.Game("Слава Україні!"))
        await sleep(20)
        await bot.change_presence(status=discord.Status.idle,activity=discord.Game("Minecraft"))
        await sleep(20)
        await bot.change_presence(status=discord.Status.dnd,activity=discord.Game("k.help"))
        await sleep(20)


async def main():
    async with bot:
        await load_extensions()
        await bot.start(settings["token"])

asyncio.run(main())
import discord
import asyncio
from discord.abc import GuildChannel
from discord.ext import commands
from discord.ext.commands import check
from discord import member
from discord.ext import tasks
import os
import shutil

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = "...", intents = intents)
client.remove_command('help')

@client.event
async def on_ready():
  check_bot.start()
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='ZeroBot'))

@tasks.loop(seconds=20)
async def check_bot():
  server = client.get_guild(707243781946343425) #Testserver-ID
  bot = server.get_member(817092531874693131)
  
  if str(bot.status) == str("online"):
    # Open the file in append & read mode ('a+')
    filetodelete = "/www/index.html"
    if os.path.exists(filetodelete):
      os.remove(filetodelete) # one file at a time
    with open(f"/www/index.html", "a+", encoding='utf-8') as file:
      file.write("ZeroBot is running smoothly :D")
     

  if str(bot.status) == str("offline"):
    filetodelete = "/www/index.html"
    if os.path.exists(filetodelete):
      os.remove(filetodelete) # one file at a time
    channel = client.get_channel(833599876721803274)
    await channel.send("ZeroBot is offline")

@client.command()
async def ping(ctx):
  await ctx.send(f'🏓 Pong! - The Bot has a latency of {round(client.latency * 1000)} ms!')

with open('tokens/token.txt','r') as file:
    TOKEN = file.read()
client.run(TOKEN)
import discord
import asyncio
from discord.abc import GuildChannel
from discord.ext import commands
from discord.ext.commands import check
import tasks
import echo
import os
import shutil

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = "...", intents = intents)
client.remove_command('help')

@client.event
async def on_ready():
  check_bot.start()

@tasks.loop(seconds=20)
async def check_bot():
  bot = client.get_user(817092531874693131)
  
  if bot.status == "online":
    file = open("/root/cloud0networkde/www/Discord/ZeroBot/status/index.html","a+") 
    file.write("ZeroBot is running smoothly :D") 

  if bot.status == "offline":
    filetodelete = "/root/cloud0networkde/www/Discord/ZeroBot/status/index.html"
    if os.path.exists(filetodelete):
      os.remove(filetodelete) # one file at a time
    channel = client.get_channel(833599876721803274)
    await channel.send("ZeroBot is offline")

  with open('tokens/token.txt','r') as file:
    TOKEN = file.read()
  client.run(TOKEN)
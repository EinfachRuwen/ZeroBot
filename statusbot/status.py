import discord
import asyncio
from discord.abc import GuildChannel
from discord.ext import commands
from discord.ext.commands import check
from discord import member
from discord.ext import tasks
import os
import shutil
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option, create_choice

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = "...", intents = intents)
slash = SlashCommand(client, sync_commands=True)
client.remove_command('help')

@client.event
async def on_ready():
  check_bot.start()
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='ZeroBot'))

@tasks.loop(seconds=20)
async def check_bot():
  server = client.get_guild(728308958682415175) # ZeroNetwork-Server
  bot = server.get_member(817092531874693131)
  
  if str(bot.status) == str("online"):
    # Open the file in append & read mode ('a+')
    filetodelete = "/www/index.html"
    if os.path.exists(filetodelete):
      os.remove(filetodelete) # one file at a time
    with open("/www/index.html", "a+", encoding='utf-8') as file:
      file.write("ZeroBot is running smoothly :D")
     

  if str(bot.status) == str("offline"):
    filetodelete = "/www/index.html"
    if os.path.exists(filetodelete):
      os.remove(filetodelete) # one file at a time
    channel = client.get_channel(847777027885236235)
    await channel.send("ZeroBot is offline")

@slash.slash(name="ping",
             description="Shows if the StatusBot is working.")
async def ping(ctx):
  await ctx.send(f'🏓 Pong! - The Bot has a latency of {round(client.latency * 1000)} ms!')

@slash.slash(name="status",
             description="Shows the status of the ZeroBot")
async def status(ctx):
  server = client.get_guild(728308958682415175) # ZeroNetwork-Server
  bot = server.get_member(817092531874693131)
  if str(bot.status) == str("online"):
    await ctx.send('ZeroBot is online, everything is working fine!')
  if str(bot.status) == str("offline"):
    await ctx.send('<@390965278470569985> ZeroBot is offline :o')
    await ctx.send('PLEASE contact <@390965278470569985> so he can fix that!')

with open('tokens/token.txt','r') as file:
    TOKEN = file.read()
client.run(TOKEN)
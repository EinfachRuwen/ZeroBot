# Meet ZeroBot, the best bot for your server! 
# With the bot you can create giveaways, play "Rock, Paper, Scissors" and much more. 
# With the many commands, from fun, moderation and general, you can do an incredible amount. 
# Thanks to a highly efficient server, the ZeroBot is almost always online. 

# Currently Available Prefix (_)-Commands: 
# _help
# _s

#Changelog:
# - Made joinesandleaves log better

# Code start's here:
import discord
import random
import asyncio
import os
import cpuinfo
from discord.abc import GuildChannel
from github import Github
from pprint import pprint
from discord.ext import commands
from discord.ext.commands import check
from discord import member
from discord.ext import tasks
from itertools import cycle
import datetime
import requests
from bs4 import BeautifulSoup
import logging
from random import randrange
import pytz
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option, create_choice
from requests.api import options
import statcord

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
with open('tokens/prefix.txt','r') as file:
    PREFIXFORCOMMANDS = file.read()
client = commands.Bot(command_prefix = PREFIXFORCOMMANDS, intents = intents)
client.remove_command('help')
slash = SlashCommand(client, sync_commands=True)
with open('tokens/statcord.txt','r') as file:
    STATCORDTOKEN = file.read()
key = STATCORDTOKEN
api = statcord.Client(client,key)
api.start_loop()

@client.event
async def on_command(ctx):
    api.command_run(ctx)

statusmessages = ['Invite again >> Slash-Commands | https://zero.byzero.dev/invite', 'zero.byzero.dev', '/help', 'Invite again >> Slash-Commands | https://zero.byzero.dev/invite', '/stats', 'byZero', 'Invite again >> Slash-Commands | https://zero.byzero.dev/invite']
statusmsg = cycle(statusmessages)

# Message for Starting the Bot
@client.event
async def on_ready():
    with open('tokens/firstprint.txt','r') as file:
        firstprint = file.read()
    with open('tokens/secondprint.txt','r') as file:
        secondprint = file.read()
    print (firstprint)
    print (secondprint)
    change_status.start()
    channel = client.get_channel(879054620838748192)
    embed=discord.Embed(title="I am back 👋", description="I just restarted!")
    embed.set_author(name="Restart", icon_url="https://zerobot.byzero.dev/data/restart/restart.gif")
    embed.set_thumbnail(url="https://zerobot.byzero.dev/data/ZeroBot.png")
    embed.add_field(name="What happended?", value="I don't know :o Maybe someone unplugged me.", inline=False)
    embed.set_footer(text="This is an automatic execution, should the bot ever restart.")
    await channel.send(embed=embed)

@tasks.loop(seconds=20)
async def change_status():
    await client.change_presence(
        status=discord.Status.online,
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=next(statusmsg)
        )
    )


# On Server Join
@client.event
async def on_guild_join(guild):
    channel = client.get_channel(879054620838748192)
    embed=discord.Embed(title="I joined a new Server!", description=f"Name: '{guild}'")
    embed.set_thumbnail(url=f"{guild.icon_url}")
    embed.add_field(name="What happended?", value="I JOINED A NEW SERVER YEAHHHHHHHHHHHHHHH", inline=False)
    embed.add_field(name="Information about the Server", value=f"{guild.name} - {guild.id} | Owner: {guild.owner.mention} | Region: {guild.region} | Member-Count: {guild.member_count}", inline=True)
    embed.set_footer(text="This is an automatic execution, should I join a new Server!")
    await channel.send(embed=embed)

# Make an Event for on_guild_leave and send the same Message as on on_guild_join but make some changes to the embed
@client.event
async def on_guild_remove(guild):
    channel = client.get_channel(879054620838748192)
    embed=discord.Embed(title="I left a Server!", description=f"Name: '{guild}'")
    embed.set_thumbnail(url=f"{guild.icon_url}")
    embed.add_field(name="What happended?", value="I LEFT A SERVER NOOOOOOOOOOOOOOOOOOO", inline=False)
    embed.add_field(name="Information about the Server", value=f"{guild.name} - {guild.id} | Owner: {guild.owner.mention} | Region: {guild.region} | Member-Count: {guild.member_count}", inline=True)
    embed.set_footer(text="This is an automatic execution, should I leave a Server!")
    await channel.send(embed=embed)

@slash.slash(name="invite",
             description="Shows the invite link!")
async def invite(ctx):
    embed = discord.Embed(
        title = "Lade den Bot auf deinen Server ein!",
        url = "https://zero.byzero.dev/invite"
    )
    await ctx.send(embed = embed)


# Message on join and leave
@client.event
async def on_member_join(member):
    # Open the file in append & read mode ('a+')
    with open("logs/joinsandleaves.txt", "a+") as file_object:
    # Move read cursor to the start of file.
        file_object.seek(0)
    # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0 :
            file_object.write("\n")
    # Append text at the end of file
        file_object.write(str(member) + ' has joined the server.')
        

@client.event
async def on_member_remove(member):
    # Open the file in append & read mode ('a+')
    with open("logs/joinsandleaves.txt", "a+") as file_object:
    # Move read cursor to the start of file.
        file_object.seek(0)
    # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0 :
            file_object.write("\n")
    # Append text at the end of file
        file_object.write(str(member) + ' has left the server.')
    

@slash.slash(name="ping",
             description="Shows you the bot's ping (latency)")
async def ping(ctx):
    await ctx.send(f'🏓 Pong! - The Bot has a latency of {round(client.latency * 1000)} ms!')

# Hilfe-Command
@client.command(aliases=['hilfe'])
async def help(ctx):
    embed=discord.Embed(title="Slash Commands are here!", description="Support for the regular commands has been dropped, please use Slash Commands from now on. The gif explains how to use a slash command.")
    embed.set_image(url='https://zerobot.byzero.dev/data/kp7xiel4w9a.gif')
    await ctx.send(embed=embed)

# Hilfe-Command
@slash.slash(name="help",
             description="Why do you even want to try?")
async def help(ctx):
    await ctx.send("Seriously? You want to see all commands? There is a menu for that if you do `/`. Shut up. GET OUTTA HERE")

@client.event
async def on_message(message):

    # Do not allow to use the bots in private messages.
    if message.guild:
        with open('tokens/mention.txt','r') as file:
            MENTION = file.read()
        with open('tokens/prefix.txt','r') as file:
            PREFIXFORCOMMANDS = file.read()
        if message.content.lower() == MENTION:
                await message.channel.send("The Prefix is: `/`")
                
        # optimized "hello"-feature                
        hello_words = ["hallo", "moin", "servus", "hi"]
        
        if message.guild.id == 728308958682415175:
          for word in hello_words:
              if message.content.lower() == word:
                  number = random.randint(0, 5)
                  if number == 1:
                      await message.channel.send("https://tenor.com/view/inside-out-joy-hi-hey-hello-gif-4763730")
                  if number == 2:
                      await message.channel.send("https://tenor.com/view/hi-hello-cute-baby-wave-gif-17882162")
                  if number == 3:
                      await message.channel.send("https://tenor.com/view/hey-girlfriend-bear-wave-hello-cute-gif-17675558")
                  if number == 4:
                      await message.channel.send("https://tenor.com/view/hello-hi-cute-adorable-angry-birds-gif-17101140")
                  if number == 5:
                      await message.channel.send("https://tenor.com/view/hi-husky-hello-cute-gif-15361405")
       
        if client.user.mentioned_in(message):
            await message.add_reaction("👋")
            
            
        # If it is a command
        if message.content.startswith(PREFIXFORCOMMANDS):
            if message.author.id != 817092531874693131:

                # Open the file in append & read mode ('a+')
                with open("logs/commandlogs.txt", "a+", encoding='utf-8') as file_object:
                # Move read cursor to the start of file.
                    file_object.seek(0)
                # If file is not empty then append '\n'
                    data = file_object.read(100)
                    if len(data) > 0 :
                        file_object.write("\n")
                # Append text at the end of file
                    timeGermany = pytz.timezone('Europe/Berlin')
                    rn_tG = datetime.datetime.now(timeGermany)
                    file_object.write("\n")
                    file_object.write("----------------------------------------")
                    file_object.write("\n")
                    file_object.write(f"User: [{str(message.author)}] | {str(message.author.mention)} | Icon: [{message.author.avatar_url}]")
                    file_object.write("\n")
                    file_object.write(f"Command: [{message.content}]")
                    file_object.write("\n")
                    file_object.write(f"Channel: [{message.channel}] | {message.channel.mention}")
                    file_object.write("\n")
                    file_object.write(f"Time: [{str(rn_tG.strftime('%d.%m.%y at %H:%M:%S'))}] - Server: {message.guild.name} ID: {message.guild.id} - Owner: {message.guild.owner} - Member-Count: [{message.guild.member_count}] - Icon-URL: [{message.guild.icon_url}]")
                    file_object.write("\n")
                    file_object.write("----------------------------------------")
                    msg = message
                    channel = client.get_channel(879054620838748192)
                    embed=discord.Embed(title=f"{message.content}")
                    embed.set_author(name=f"User: {str(message.author)} | {str(message.author.mention)}", icon_url=f"{message.author.avatar_url}")
                    embed.set_thumbnail(url=f"{message.guild.icon_url}")
                    embed.add_field(name="Channel", value=f"{msg.channel} - {msg.channel.mention}", inline=True)
                    embed.add_field(name="Server", value=f"{msg.guild.name} - {msg.guild.id} | Owner: {msg.guild.owner.mention} | Member-Count: {msg.guild.member_count}", inline=True)
                    embed.add_field(name="Message", value=f"URL to message: `{msg.jump_url}` ({msg.jump_url})")
                    embed.set_footer(text=f"{str(rn_tG.strftime('%d.%m.%y at %H:%M:%S'))} | Made by byZero")
                    await channel.send(embed=embed)
                    print(f"{str(message.author)} used \"{message.content}\"")

                    
                with open('tokens/prefix.txt','r') as file:
                    PREFIXFORCOMMANDS = file.read()
                
                if message.content.startswith(f"{PREFIXFORCOMMANDS}start"): #command to start quessing game
                    channel = message.channel
                    await channel.send(f"Guess the number from 0-35 by writing numbers in this channel! {message.author.mention}") #message that tells about the start of the game

                    number1 = random.randint(1,35) #picking random number from 1 - 35 and printing it
                    print(f'The solution for the "Guess The Number"-Game is: {number1}')
                                     
                    zahl = 0

                    def check(m):
                        return m.content == str(number1) and m.channel == channel #checking answers
                        zahl += 1
                    
                    msg = await client.wait_for('message', check=check)
                    await channel.send(f"Correct answer, {message.author.mention}!".format(msg)) #tells who got the correct answer

                await client.process_commands(message)
            
@client.event
async def on_slash_command(ctx):
    # Open the file in append & read mode ('a+')
                with open("logs/commandlogs.txt", "a+", encoding='utf-8') as file_object:
                # Move read cursor to the start of file.
                    file_object.seek(0)
                # If file is not empty then append '\n'
                    data = file_object.read(100)
                    if len(data) > 0 :
                        file_object.write("\n")
                # Append text at the end of file
                    timeGermany = pytz.timezone('Europe/Berlin')
                    rn_tG = datetime.datetime.now(timeGermany)
                    file_object.write("\n")
                    file_object.write("----------------------------------------")
                    file_object.write("\n")
                    file_object.write(f"User: [{str(ctx.author)}] | {str(ctx.author.mention)} | Icon: [{ctx.author.avatar_url}]")
                    file_object.write("\n")
                    file_object.write(f"Command: [/{ctx.command} {ctx.args}]")
                    file_object.write("\n")
                    file_object.write(f"Channel: [{ctx.channel}] | {ctx.channel.mention}")
                    file_object.write("\n")
                    file_object.write(f"Time: [{str(rn_tG.strftime('%d.%m.%y at %H:%M:%S'))}] - Server: {ctx.guild.name} ID: {ctx.guild.id} - Owner: {ctx.guild.owner} - Member-Count: [{ctx.guild.member_count}] - Icon-URL: [{ctx.guild.icon_url}]")
                    file_object.write("\n")
                    file_object.write("----------------------------------------")
                    msg = ctx
                    channel = client.get_channel(879054620838748192)
                    embed=discord.Embed(title=f"/{ctx.command} {ctx.args}")
                    embed.set_author(name=f"User: {str(ctx.author)} | {str(ctx.author.mention)}", icon_url=f"{ctx.author.avatar_url}")
                    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
                    embed.add_field(name="Channel", value=f"{msg.channel} - {msg.channel.mention}", inline=True)
                    embed.add_field(name="Server", value=f"{msg.guild.name} - {msg.guild.id} | Owner: {msg.guild.owner.mention} | Member-Count: {msg.guild.member_count}", inline=True)
                    embed.add_field(name="Message", value=f"URL to message: `{ctx.jump_url}` ({ctx.jump_url})")
                    embed.set_footer(text=f"{str(rn_tG.strftime('%d.%m.%y at %H:%M:%S'))} | Made by byZero")
                    await channel.send(embed=embed)
                    print(f"{str(ctx.author)} used \"/{ctx.command}\"")

@slash.slash(name="clear",
             description="Deletes messages from a channel",
             options=[
               create_option(
                 name="amount",
                 description="How many messages do you wanna delete?",
                 option_type=4,
                 required=True
               )
             ])
@commands.has_permissions(manage_messages=True)
async def clear (ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)
    msg = await ctx.send(f'I deleted {amount} messages.')
    await asyncio.sleep(10)
    await msg.delete()

@slash.slash(name="kick",
             description="Kicks someone from the server.",
             options=[
               create_option(
                 name="member",
                 description="Who do you wanna kick?",
                 option_type=6,
                 required=True
               ),
               create_option(
                name="reason",
                description="Who do you wanna kick him?",
                option_type=3,
                required=False
               )
             ])
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason: str = None):
    await member.kick(reason=reason)
    print (f'Yea, so I just kicked {member} if that\'s okay :)')
    embed=discord.Embed(title=f"Kicking {member}")
    embed.set_image(url="https://zerobot.byzero.dev/data/kootf9omu9a.gif")
    await ctx.send(embed=embed)
    channel = client.get_channel(879054620838748192)
    embed=discord.Embed(title=f"Kicking {member} on {ctx.guild.name}")
    embed.set_image(url="https://zerobot.byzero.dev/data/kootf9omu9a.gif")
    await channel.send(embed=embed)

@slash.slash(name="ban",
             description="Bans someone from the server.",
             options=[
               create_option(
                 name="member",
                 description="Who do you wanna ban?",
                 option_type=6,
                 required=True
               ),
               create_option(
                name="reason",
                description="Who do you wanna ban him?",
                option_type=3,
                required=False
               )
             ])
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason: str = None):
    await member.ban(reason=reason)
    print (f'Yea, so I just banned {member} if that\'s okay :)')
    embed=discord.Embed(title=f"Banning {member}")
    embed.set_image(url="https://zerobot.byzero.dev/data/koota42pn9a.gif")
    await ctx.send(embed=embed)
    channel = client.get_channel(879054620838748192)
    embed=discord.Embed(title=f"Banning {member} on {ctx.guild.name}")
    embed.set_image(url="https://zerobot.byzero.dev/data/koota42pn9a.gif")
    await channel.send(embed=embed)

# IN BEARBEITUNG
# @client.command()
# @commands.has_permissions(kick_members=True)
# async def warn(ctx, member : discord.Member, *, reason=None):
#    serverid = ctx.guild.id
#    memberid = member.id
#    # Open the file in append & read mode ('a+')
#    with open(f"logs/members/server/{serverid}/member/{memberid}/warns.txt", "a+", encoding='utf-8') as file_object:
#    # Move read cursor to the start of file.
#        file_object.seek(0)
#    # Check existing warns
#        Warns = file.read()
#        if Warns == '':
#            Warns = '0'
#    # Replace the target string
#    NewWarns = int(Warns) + 1
#    # Write the file out again
#    with open('logs/members/server/{serverid}/member/{memberid}/warns.txt', 'a+') as file:
#        file.write(NewWarns)
#
#    # Add a Reason to it...
#    with open('logs/members/server/{serverid}/member/{memberid}/warn-{NewWarns}.txt', 'a+') as file:
#        file.write(reason)
#    # Send Message to Member
#    embed=discord.Embed(title="You have been warned!", description=f"Reason: {reason}")
#    embed.set_author(name=f"{member}", icon_url=f"{member.avatar_url}")
#    embed.set_thumbnail(url="https://media.tenor.com/images/932058cb6d102234800171857cb561f2/tenor.gif")
#    embed.add_field(name=f"This is your {warn}. warn!", value=f"{warn}/12", inline=False)
#    embed.set_footer(text="Inspired by SteffoSpieler and Yasu | Coded by byZero")
#    await member.send(embed=embed)
#
#    # Send Message to Author
#    embed=discord.Embed(title="You warned {member}", description=f"Reason: {reason}")
#    embed.set_thumbnail(url="https://media1.tenor.com/images/1797102f0bf828f52ce5e955e2286b5d/tenor.gif")
#    embed.add_field(name=f"You sent {member} a nice message that I'm sure he will be happy about.", value="lol, why did you do that xD", inline=False)
#    embed.set_footer(text="Inspired by SteffoSpieler and Yasu | Coded by byZero")
#    await ctx.author.send(embed=embed)
#
#    # Send Message to Owner
#    embed=discord.Embed(title=f"{ctx.author} warned {member}", description=f"Reason: {reason}")
#    embed.set_thumbnail(url="https://media1.tenor.com/images/33ad6c19e8e5f1ca831ba00f4685e760/tenor.gif")
#    embed.set_footer(text="Inspired by SteffoSpieler and Yasu | Coded by byZero")
#    await ctx.guild.send(embed=embed)
#
#    # print if done
#    print('I warned somebody lol')
#
#@client.command()
#async def warns(ctx, member : discord.Member):
#    serverid = ctx.guild.id
#    memberid = member.id
#    # Open the file in append & read mode ('a+')
#    with open(f"logs/members/server/{serverid}/member/{memberid}/warns.txt", "a+", encoding='utf-8') as file_object:
#    # Move read cursor to the start of file.
#        file_object.seek(0)
#    # Check existing warns
#        Warns = file.read()
#        if Warns == '':
#            Warns == '0'
#    ctx.send(f'{member.mention} has already been warned {Warns} times')


# Rich Presence Changer
# Only limited to the Owner (byZero)
@slash.slash(name="presence",
             description="Changes the rich presence of the bot (watching, playing ...)",
             options=[
               create_option(
                 name="type",
                 description="0, 1, 2, 3? Beep Boop",
                 option_type=4,
                 required=True,
                 choices=[
                  create_choice(
                    name="listening",
                    value=0
                  ),
                  create_choice(
                    name="watching",
                    value=1
                  ),
                  create_choice(
                    name="playing",
                    value=2
                  ),
                  create_choice(
                    name="streaming",
                    value=3
                  ),
                  create_choice(
                    name="auto",
                    value=4
                  )
                 ]
               ),
               create_option(
                 name="presence",
                 description="hmmmm...",
                 option_type=3,
                 required=False
                ),
                create_option(
                 name="url",
                 description="twitch-stream-url lol",
                 option_type=3,
                 required=False
                )
             ])
@commands.is_owner()
async def presence(ctx, type : int, presence: str = "Chilling with byZero", url : str = "https://zero.byzero.dev/404"):
  await ctx.channel.purge(limit=1)
  if type == 2:
    change_status.cancel()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=presence))
    await ctx.send(f'The new Presence should be: ZeroBot is `playing {presence}`')

  elif type == 1:
    change_status.cancel()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=presence))
    await ctx.send(f'The new Presence should be: ZeroBot is `watching {presence}`')

  elif type == 0:
    change_status.cancel()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=presence))
    await ctx.send(f'The new Presence should be: ZeroBot is `listening to {presence}`')

  elif type == 4:
    change_status.start()

  elif type == 3:
    change_status.cancel()
    await client.change_presence(activity=discord.Streaming(name=presence, url=url))
    await ctx.send(f'The new Presence should be: ZeroBot is `streaming {presence}`')
 


@slash.slash(name="avatar",
             description="Sends you a member's avatar URL!",
             options=[
               create_option(
                 name="member",
                 description="Just select someone xD",
                 option_type=6,
                 required=True
               )
             ])
async def avatar(ctx, member : discord.Member):
    with open('tokens/shortio.txt','r') as file:
        shortio_token = file.read()

    r = requests.post('https://api.short.io/links/public', {
          'domain': 'zero.byzero.dev',
          'originalURL': str(member.avatar_url),
    }, headers = {
          'authorization': shortio_token
    }, json=True)

    r.raise_for_status()
    data = r.json()

    #print(data)
    shorted_url = data["shortURL"]
    embed=discord.Embed(title=str(member) + "'s Avatar-URL", url=str(shorted_url), description=f"`{str(shorted_url)}`")
    embed.set_image(url=str(shorted_url))
    await ctx.send(embed=embed)

@slash.slash(name="unban",
             description="Unban's someone.",
             options=[
               create_option(
                 name="member",
                 description="example: byZero#0001",
                 option_type=3,
                 required=True
               )
             ])
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans ()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            print (f'Yea, so I just unbanned {member} if that\'s okay :)')
            embed=discord.Embed(title=f"Unbanning {member}")
            embed.set_image(url="https://zerobot.byzero.dev/data/koypb4e0r9a.gif")
            await ctx.send(embed=embed)
            channel = client.get_channel(879054620838748192)
            embed=discord.Embed(title=f"Unbanning {member} on {ctx.guild.name}")
            embed.set_image(url="https://zerobot.byzero.dev/data/koypb4e0r9a.gif")
            await channel.send(embed=embed)
            return

@slash.slash(name="dice",
             description="Roll's the dice for ya' :D")
async def dice(ctx):
        dice_result = random.randint(1, 6)
                                     
        embed=discord.Embed(title="The dice whispered to me:")
        embed.set_thumbnail(url=f"https://zerobot.byzero.dev/data/Dice/{dice_result}.png")
                                     
        if dice_result == 1:
            embed.add_field(name="1", value="That's not much :O", inline=False)

        if dice_result == 2:
            embed.add_field(name="2", value="That's not better than 1, 1 + 1 is 2", inline=False)

        if dice_result == 3:
            embed.add_field(name="3", value="Did you know that 3 is the middle?", inline=False)

        if dice_result == 4:
            embed.add_field(name="4", value="The holy **4**!", inline=False)

        if dice_result == 5:
            embed.add_field(name="5", value="Why didn't you get a 6?", inline=False)

        if dice_result == 6:
            embed.add_field(name="6", value="You may roll the dice again :3", inline=False)
        
        await ctx.send(embed=embed)

@slash.slash(name="pickrandom",
             description="Picks a number between 1 and your specified number.",
             options=[
               create_option(
                 name="number",
                 description="just pick a number",
                 option_type=4,
                 required=True
               )
             ])
async def pickrandom(ctx, number):
        dice_result = random.randint(1, int(number))
        embed=discord.Embed(title="I picked: " + (str(dice_result)))
        await ctx.send(embed=embed)


# Create Issue-Feature by jcw05
# https://github.com/joseywoermann
# @client.command(aliases = ['createissue', 'report', 'bug', 'bugreport'])
# async def makeissue(ctx, pTitle, pBody = None):
#
#    with open('tokens/personalaccesstoken.txt','r') as file:
#        DATOKEN = file.read()
#
#    g = Github(DATOKEN)
#    repo = g.get_repo("byZeroOfficial/ZeroBot")
#
#    if pBody:
#        issue = repo.create_issue(
#            title=pTitle,
#            body = pBody + " (Issue created by Discord-user `" + str(ctx.author) + "`)",
#            assignee="byZeroOfficial",
#        )
#    else:
#        issue = repo.create_issue(
#            title=pTitle,
#            body = "(Issue created by Discord-user `" + str(ctx.author) + "`)",
#            assignee="byZeroOfficial",
#        )
#
#    issue_embed = discord.Embed(title = "Bug report has been sent!", description = "[View bug reports](https://github.com/byZeroOfficial/ZeroBot/issues)")
#    await ctx.send(embed = issue_embed)

@slash.slash(name="credits",
             description="Shows you the sources of my code and help sources and websites I used for help.")
async def credits(ctx):
    embed=discord.Embed(title="Credits", description="Here are all my sources for code and information listed.", color=0x75e3ff)
    embed.set_author(name="byZero")
    embed.add_field(name="Users", value="[jcw05#1331](https://github.com/joseywoermann)", inline=True)
    embed.add_field(name="Websites", value="[StackOverflow](https://stackoverflow.com/), [YouTube](https://youtube.com/), [GitHub](https://github.com/), [Pixabay](https://pixabay.com), [FreePix](https://freepix.com/)", inline=True)
    await ctx.send(embed=embed)

# Send messages as a bot.
@client.command(aliases=['s'])
@commands.is_owner()
async def write(ctx, *, text):
  await ctx.channel.purge(limit=1)
  await ctx.send(text)

@slash.slash(name="commandclear",
             description="Deletes messages sent by the bot.")
@commands.has_permissions(manage_messages=True)
async def commandclear(ctx):
    def is_me(m):
      return m.author == client.user

    deleted = await ctx.channel.purge(limit=100, check=is_me)
    await ctx.send('Deleted {} message(s)'.format(len(deleted)))

@slash.slash(name="giveaway",
             description="Creates a giveaway. Only works if the bot is always online. Required: Giveaways Role",
             options=[
               create_option(
                 name="time",
                 description="How long should the giveaway last (in minutes)",
                 option_type=4,
                 required=True
               ),
                create_option(
                 name="prize",
                 description="what do you wanna give away?",
                 option_type=3,
                 required=True
                ),
                create_option(
                 name="channel",
                 description="choose a giveaway channel",
                 option_type=7,
                 required=True
                ),
                create_option(
                 name="winners",
                 description="Possible Winners",
                 option_type=4,
                 required=False
                )
             ])
@commands.has_role('Giveaways')
async def giveaway(ctx, channel, time : int, winners: int = 1, *, prize: str):
    await ctx.send('Giveaway is starting...')
    await asyncio.sleep(1)
    await ctx.channel.purge(limit=1)
    await asyncio.sleep(1)
    # Part of Channel-Send-System
    embed=discord.Embed(title="<a:tadaaa:840305140502495272> GIVEAWAY!!!", description=prize, color=0xee1153)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://byzero.is-inside.me/DAYAr4h2.jpg")
    embed.set_footer(text=f"Winners = {str(winners)}")
    end = datetime.datetime.utcnow() + datetime.timedelta(seconds = time*60)
    embed.add_field(name="How to:", value="React to the message with the <a:tadaaa:840305140502495272>-Emoji so you can enter the giveaway.", inline=True)
    embed.timestamp = end
    # Part of Channel-Send-System
    sent_message = await channel.send(embed=embed)
    await sent_message.add_reaction("<a:tadaaa:840305140502495272>")
    await asyncio.sleep(time*60)
    new_message = await channel.fetch_message(sent_message.id)
    users = await new_message.reactions[0].users().flatten()
    users.pop(users.index(client.user))
    for i in range(winners):
        member = random.choice(users)
        users.pop(users.index(member))
        await channel.send(member.mention)
        embed=discord.Embed(title="<a:tadaaa:840305140502495272> Congratulations!")
        embed.set_thumbnail(url="https://byzero.is-inside.me/a8XarhZG.gif")
        embed.add_field(name="Winner:", value=member.mention + f" You have won {prize}!", inline=True)
        embed.set_footer(text="Coded by byZero")
        await channel.send(embed=embed)

@slash.slash(name="developer",
             description="Shows you some information about my father // my developer")
async def developer(ctx):
    embed=discord.Embed(title="byZero", url="https://byzer0.ml")
    embed.set_thumbnail(url="https://i.imgur.com/bp1UfAI.png")
    embed.add_field(name="👋 Hello! I am byZero.", value="I am byZero, a young developer and student. Currently I go to a secondary school near Bielefeld, Germany. I recently created my own Discord-Bot.", inline=False)
    embed.add_field(name="Read more about me:", value="You can find more informations about me here: https://byzer0.ml/github-info", inline=True)
    embed.set_footer(text="This Bot was coded by byZero!")
    await ctx.send(embed=embed)

# How Gay-Command like Dank Memer
@slash.slash(name="howgay",
             description="Show's you how gay u are rn.")
async def howgay(ctx):
    howgayareyourightnow = random.randint(1, 100)
    embed=discord.Embed(title="gay r8 machine", description="u are " + f'{howgayareyourightnow}' + "% gay 🏳️‍🌈", color=0x8000a3)
    embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

# Rickroll someone :D
@slash.slash(name="rickroll",
             description="Rickroll someone :D",
             options=[
               create_option(
                 name="member",
                 description="Who's the lucky one?",
                 option_type=6,
                 required=True
               )])
async def rickroll(ctx, member : discord.Member):
  with open('tokens/rickrollurl.txt','r') as file:
    RICKROLLURL = file.read()
  await ctx.channel.purge(limit=1)
  await member.send(RICKROLLURL)
  await ctx.send('So, now you rickrolled ' + f'{member}' + '!' + f" - {ctx.author.mention}")
  await asyncio.sleep(5)
  await ctx.channel.purge(limit=1)


@client.event
async def on_slash_command_error(ctx, ex):
  exstr = str(ex)
  if exstr == "Role 'Giveaways' is required to run this command.":
    error = 'This error can occur for 2 reasons:\n1. You need to create a role called "Giveaways" and give it to everyone who is allowed to create giveaways.\n2. You are not allowed to create giveaways because you do not have the "Giveaways" role.'
    embed = discord.Embed(title = "Error", description = f"```\n{error}```", color = discord.Color.red())
    await ctx.send(embed=embed)
  elif exstr == "list index out of range":
    embed=discord.Embed(title="There is no winner")
    embed.set_thumbnail(url="http://static.skaip.org/img/emoticons/180x180/f6fcff/cry.gif")
    embed.add_field(name="It looks like nobody entered the giveaway.", value=":(", inline=True)
    embed.set_footer(text="Coded by byZero")
    await ctx.send(embed=embed)
  elif exstr == "division by zero":
    embed=discord.Embed(title=f"Result: Error", color=0x3f3f3f)
    embed.add_field(name="Error:", value=f"I THINK I GOT BRAIN DAMAGE", inline=False)
    embed.add_field(name="sowwy", value="i am so sowwyyyyyyyyyyyyyyyyyyyyy", inline=False)
    embed.set_thumbnail(url="https://pbs.twimg.com/media/EO8FFOpX0AAyt1W.jpg")
    await ctx.send(embed=embed)
  else:
    embed = discord.Embed(title = "Error", description = f"```\n{ex}```", color = discord.Color.red())
    await ctx.send(embed=embed)
    channelembed = discord.Embed(title = "Error", description = f"```\n{ex}```", color = discord.Color.green())
    channel = client.get_channel(879054620838748192)
    await channel.send(embed=channelembed)


@slash.slash(name="spam",
             description="you wanna spam?",
             options=[
               create_option(
                 name="yon",
                 description="yes or no?!",
                 option_type=3,
                 required=True,
                 choices=[
                  create_choice(
                    name="-y",
                    value="-y"
                  ),
                  create_choice(
                    name="-n",
                    value="-n"
                  )
                 ]
               ),
               create_option(
                 name="amount",
                 description="how often do you wanna spam that message?",
                 option_type=4,
                 required=True
                ),
                create_option(
                 name="message",
                 description="what do you wanna spam?",
                 option_type=3,
                 required=True
                )
               ])
@commands.is_owner()
async def spam(ctx, yon, amount: int, message):
    if yon == "-y":
       await ctx.channel.purge(limit=1)
       for i in range(amount):
            await ctx.send(f'{message}')


# define-Feature by jcw05
# https://github.com/joseywoermann                                     
@slash.slash(name="define",
             description="Defines a word! Just kiddin'",
             options=[
                create_option(
                 name="search_term",
                 description="...",
                 option_type=3,
                 required=True
                )])
@commands.guild_only()
async def define(ctx, *, search_term):

    URL = "https://www.urbandictionary.com/define.php?term=" + str(search_term)
    page = requests.get(URL)
    fetched_page = BeautifulSoup(page.content, 'html.parser')

    searched_word = fetched_page.find('a', attrs={'class': 'word'})
    meaning = fetched_page.find('div', attrs={'class': 'meaning'})

    if searched_word:
        name_output = str(searched_word.text)
    else:
        name_output = "No results."
            
    if meaning:
        meaning_output = str(meaning.text)
    else:
        meaning_output = "No results."

    define_embed = discord.Embed(title=name_output, description=meaning_output, color=0x1affbe)
    define_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)
    await ctx.send(embed=define_embed)

@slash.slash(name="rps",
             description="Rock Paper Scissors on Discord",
             options=[
               create_option(
                 name="what",
                 description="Rock, Paper or Scissors?",
                 option_type=3,
                 required=True,
                 choices=[
                  create_choice(
                    name="rock",
                    value="rock"
                  ),
                  create_choice(
                    name="paper",
                    value="paper"
                  ),
                  create_choice(
                    name="scissors",
                    value="scissors"
                  ),
                  create_choice(
                    name="help",
                    value="help"
                  )
                 ]
               )
               ])
async def rps(ctx, what):
    if what == 'help':
        embed=discord.Embed(title="Rock paper scissors", description="Rock paper scissors (also known by other orderings of the three items, with rock sometimes being called stone, or as roshambo or ro-sham-bo)[1][2][3] is a hand game usually played between two people, in which each player simultaneously forms one of three shapes with an outstretched hand.")
        embed.set_author(name=str(ctx.author), url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://www.sciencemag.org/sites/default/files/styles/article_main_large/public/images/sn-rockpaper.jpg")
        await ctx.send(embed=embed) 
    number = random.randint(0, 3)
                                     
    whats = ["rock", "paper", "scissors"]
    for word in whats:
        if word == what:
            if number == 1:
                a = 'rock'
                b = 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Rock-paper-scissors_%28rock%29.png/600px-Rock-paper-scissors_%28rock%29.png'
                embed=discord.Embed(title="Rock paper scissors", description="Just a funny game!")
                embed.set_author(name=str(ctx.author), url=ctx.author.avatar_url)
                embed.set_thumbnail(url=b)
                embed.add_field(name=a, value="lol", inline=True)
                await ctx.send(embed=embed)
            if number == 2:
                a = 'scissors'
                b = 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Rock-paper-scissors_%28scissors%29.png/600px-Rock-paper-scissors_%28scissors%29.png'
                embed=discord.Embed(title="Rock paper scissors", description="Just a funny game!")
                embed.set_author(name=str(ctx.author), url=ctx.author.avatar_url)
                embed.set_thumbnail(url=b)
                embed.add_field(name=a, value="lol", inline=True)
                await ctx.send(embed=embed)
            if number == 3:
                a = 'paper'
                b = 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Rock-paper-scissors_%28paper%29.png/600px-Rock-paper-scissors_%28paper%29.png'
                embed=discord.Embed(title="Rock paper scissors", description="Just a funny game!")
                embed.set_author(name=str(ctx.author), url=ctx.author.avatar_url)
                embed.set_thumbnail(url=b)
                embed.add_field(name=a, value="lol", inline=True)
                await ctx.send(embed=embed)


# Short-Url-Feature by jcw05
# https://github.com/joseywoermann
@slash.slash(name="short",
             description="Makes an URL shorter with zero.byzero.dev",
             options=[
               create_option(
                 name="long_url",
                 description="example: https://zero.byzero.dev",
                 option_type=3,
                 required=True
               )
             ])
async def short(ctx, long_url):
    with open('tokens/shortio.txt','r') as file:
        shortio_token = file.read()

    r = requests.post('https://api.short.io/links/public', {
          'domain': 'zero.byzero.dev',
          'originalURL': long_url,
    }, headers = {
          'authorization': shortio_token
    }, json=True)

    r.raise_for_status()
    data = r.json()

    #print(data)
    shorted_url = data["shortURL"]

    short_embed = discord.Embed(title="Your short URL:", description=shorted_url, color=000000)
    await ctx.send(embed=short_embed)

@slash.slash(name="stats",
             description="Shows you some bot information")
async def stats(ctx):
    appinfo = await client.application_info() 
    embed=discord.Embed(title="Bot-Information", color=0xff0582)
    embed.set_thumbnail(url="https://zerobot.byzero.dev/data/ZeroBot.png")
    embed.add_field(name="📄 Name", value="ZeroBot", inline=True)
    embed.add_field(name="👑 Bot Owner", value=f"{appinfo.owner.mention}", inline=True)
    embed.add_field(name="👩‍🤝‍🧑🏽 Users", value=f"`{len(client.users)}`", inline=True)
    embed.add_field(name="📁Servers", value=f"`{len(client.guilds)}`", inline=True)
    embed.add_field(name="📄 Commands", value=f"`{len(slash.commands)}`", inline=True)
    with open('tokens/stats/cpu.txt','r') as file:
        cpu = file.read()
    with open('tokens/stats/cpucores.txt','r') as file:
        cpucores = file.read()
    with open('tokens/stats/hoster.txt','r') as file:
        hoster = file.read()
    with open('tokens/stats/raminfo.txt','r') as file:
        raminfo = file.read()
    with open('tokens/stats/model.txt','r') as file:
        model = file.read()
    with open('tokens/stats/rom.txt','r') as file:
        rom = file.read()
    embed.add_field(name="🖥 CPU", value=cpu, inline=True) 
    embed.add_field(name="🖥 CPU-Cores", value=cpucores, inline=True)
    embed.add_field(name="🖥 RAM", value=raminfo, inline=True)
    embed.add_field(name="🖥 ROM", value=rom, inline=True)
    embed.add_field(name="🖥 Hoster", value=hoster, inline=True)
    embed.add_field(name="🖥 Hoster-Model", value=model, inline=True)   
    embed.set_footer(text="Made by byZero")
    await ctx.send(embed=embed)

@slash.slash(name="whereami",
             description="Shows you some information about your location")
async def whereami(ctx):
    embed=discord.Embed(title="Where am I?")
    embed.set_author(name=str(ctx.author), icon_url=str(ctx.author.avatar_url))
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.add_field(name="Name", value=f"{ctx.guild.name}", inline=False)
    embed.add_field(name="ID", value=f"{ctx.guild.id}", inline=True)
    embed.add_field(name="Owner", value=f"{ctx.guild.owner}", inline=True)
    embed.add_field(name="Region", value=f"{ctx.guild.region}", inline=True)
    embed.add_field(name="Member-Count", value=f"{ctx.guild.member_count}", inline=True)
    embed.add_field(name="Icon-URL", value=f"[here]({ctx.guild.icon_url})", inline=True)
    embed.add_field(name="Channel", value=f"{ctx.channel}", inline=True)
    embed.add_field(name="Channel-Mention", value=f"{ctx.channel.mention}", inline=True)
    embed.add_field(name="Author", value=f"{str(ctx.author)}", inline=True)
    embed.add_field(name="Author-Mention", value=f"{str(ctx.author.mention)}", inline=True)
    embed.add_field(name="Author-Icon", value=f"[here]({ctx.author.avatar_url})", inline=True)
    await ctx.send(embed=embed)

@slash.slash(name="sendmsg",
             description="Send a message",
             options=[
               create_option(
                 name="who",
                 description="just pick one",
                 option_type=3,
                 required=True,
                 choices=[
                  create_choice(
                    name="owner",
                    value="owner"
                  ),
                  create_choice(
                    name="channel",
                    value="channel"
                  ),
                  create_choice(
                    name="everyone",
                    value="everyone"
                  )
                 ]
               ),
               create_option(
                name="id",
                description="id",
                option_type=3,
                required=False
               ),
               create_option(
                name="message",
                description="message",
                option_type=3,
                required=False
            )])
@commands.is_owner()
async def sendmsg(ctx, who, id, *, message):
    if who == 'owner':
        guild = client.get_guild(int(id))
        await guild.owner.send(message)
    if who == 'channel':
        channel = client.get_channel(int(id))
        await channel.send(message)
    if who == 'everyone':
        activeservers = client.guilds
        for guild in activeservers:
            await guild.owner.send(message)
    await ctx.send("done")

@slash.slash(name="whois",
             description="Shows Information about Minecraft-Player",
             options=[
               create_option(
                 name="name",
                 description="example: byZero",
                 option_type=3,
                 required=True
               )
             ])
async def whois(ctx, name):
    response = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{name}')


    json_response = response.json()
    uuid = json_response['id']
    image = f"https://crafatar.com/avatars/{uuid}"
    embed=discord.Embed(title=name, url="https://namemc.com/search?q={name}", description=f'UUID: {uuid} - Name-Changes: https://namemc.com/search?q={name}', color=0x3f3f3f)
    embed.set_author(name="Who is:", icon_url=f'https://crafatar.com/renders/head/{uuid}')
    embed.set_thumbnail(url=image)
    await ctx.send(embed=embed)


# Made possible by Evergene
# https://evergene.io

@slash.slash(name="image",
             description="Image :D",
             options=[
               create_option(
                 name="type",
                 description="just pick one",
                 option_type=3,
                 required=True,
                 choices=[
                  create_choice(
                    name="hug",
                    value="hug"
                  ),
                  create_choice(
                    name="aww so cute",
                    value="aww"
                  ),
                  create_choice(
                    name="cat",
                    value="floof"
                  )
                 ]
               )])
async def image(ctx, type : str):
  # Define {"requesturl"}
  requesturl = f"https://evergene.io/api/{type}"

  # Request:
  response = requests.get(requesturl)
  json_response = response.json()
  imageurl = json_response['url']

  # Message
  embed=discord.Embed(title="Here you go:")
  embed.set_image(url=imageurl)
  await ctx.send(embed=embed)

@slash.slash(name="meme",
             description="Meme :D")
async def meme(ctx):
  # Request:
  response = requests.get('https://evergene.io/api/memes/')
  json_response = response.json()
  imageurl = json_response['url']

  # Message
  embed=discord.Embed(title="Here you go:")
  embed.set_image(url=imageurl)
  await ctx.send(embed=embed)

# Command that sends the Weather for a specific location
@slash.slash(name="weather",
             description="Weather for a specific location",
             options=[
               create_option(
                 name="location",
                 description="example: London",
                 option_type=3,
                 required=True
               )
             ])
async def weather(ctx, location):
  # Request:
  # Open the file ./tokens/weather.txt and read the token and set it as weather_api_key
  with open('./tokens/weather.txt', 'r') as file:
    weather_api_key = file.read()
  response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={weather_api_key}')
  json_response = response.json()
  temp = json_response['main']['temp']
  temp = round(temp - 273.15)
  weather = json_response['weather'][0]['main']
  icon = json_response['weather'][0]['icon']
  wind = json_response['wind']['speed']
  humidity = json_response['main']['humidity']
  pressure = json_response['main']['pressure']
  cloud_cover = json_response['clouds']['all']
  city = json_response['name']
  country = json_response['sys']['country']

  # Message
  embed=discord.Embed(title=f"Weather in {city}, {country}", color=0x3f3f3f)
  embed.set_thumbnail(url=f"http://openweathermap.org/img/wn/{icon}@4x.png")
  embed.add_field(name="Temperature", value=f"{temp}°C", inline=True)
  embed.add_field(name="Weather", value=f"{weather}", inline=True)
  embed.add_field(name="Wind", value=f"{wind}m/s", inline=True)
  embed.add_field(name="Humidity", value=f"{humidity}%", inline=True)
  embed.add_field(name="Pressure", value=f"{pressure}hPa", inline=True)
  embed.add_field(name="Cloud Cover", value=f"{cloud_cover}%", inline=True)
  embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
  await ctx.send(embed=embed)
  # Made by GitHub Copilot with so much luv <3
  # This Text above is also written by Github Copilot, lol
  # https://copilot.github.com


# Token-File located in /root/Bots/ZeroBot/tokens/token.txt
with open('tokens/token.txt','r') as file:
    TOKEN = file.read()
client.run(TOKEN)

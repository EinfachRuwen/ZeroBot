# Meet ZeroBot, the best bot for your server! 
# With the bot you can create giveaways, play "Rock, Paper, Scissors" and much more. 
# With the many commands, from fun, moderation and general, you can do an incredible amount. 
# Thanks to a highly efficient server, the ZeroBot is almost always online. 

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
import traceback
import sys

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
with open('tokens/prefix.txt','r') as file:
    PREFIXFORCOMMANDS = file.read()
client = commands.Bot(command_prefix = PREFIXFORCOMMANDS, intents = intents)
client.remove_command('help')

statusmessages = ['zerobot.ml', '_help', '_stats', 'byZero']
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
    channel = client.get_channel(833599876721803274)
    embed=discord.Embed(title="I am back 👋", description="I just restarted!")
    embed.set_author(name="Restart", icon_url="https://cloud.0network.de/Discord/ZeroBot/restart/restart.gif")
    embed.set_thumbnail(url="https://cloud.0network.de/Discord/ZeroBot/ZeroBot.png")
    embed.add_field(name="What happended?", value="I don't know :o Maybe someone unplugged me", inline=False)
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
    channel = client.get_channel(833599876721803274)
    embed=discord.Embed(title="I joined a new Server!", description=f"Name: '{guild}'")
    embed.set_thumbnail(url="https://cloud.0network.de/Discord/ZeroBot/ZeroBot.png")
    embed.add_field(name="What happended?", value="I JOINED A NEW SERVER YEAHHHHHHHHHHHHHHH", inline=False)
    embed.set_footer(text="This is an automatic execution, should I join a new Server!")
    await channel.send(embed=embed)




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
        

@client.command(aliases=['pong', 'latency'])
async def ping(ctx):
    await ctx.send(f'🏓 Pong! - The Bot has a latency of {round(client.latency * 1000)} ms!')

# Hilfe-Command
@client.command(aliases=['hilfe'])
async def help(ctx):
   # General Commands
   with open('tokens/prefix.txt','r') as file:
    PREFIXFORCOMMANDS = file.read()
   embed=discord.Embed(title="Help - Prefix: `" + PREFIXFORCOMMANDS + "`", description="Here you can find all commands listed, which you can use with my bot :)", color=0x6ce2e4)
   embed.set_author(name="ZeroBot", icon_url="https://i.imgur.com/SExHItg.png")
   embed.add_field(name="General Commands", value="Just the general commands, like _avatar - [here](https://byzer0.ml/zerobot-general)", inline=True)
   embed.add_field(name="Mod-Commands", value="That's commands only limited to moderators. - [here](https://byzer0.ml/zerobot-mod)", inline=True)
   embed.add_field(name="Fun-Commands", value="Have fun with that commands :D - [here](https://byzer0.ml/zerobot-fun)", inline=True)
   embed.add_field(name="Admin-Commands", value="Haha! That's a command list for me :D - [here](https://byzer0.ml/zerobot-admin)", inline=True)
   embed.set_footer(text="Use _feature to make command-idea!")
   await ctx.author.send(embed=embed)
   await ctx.channel.purge(limit=1)

@client.command()
async def invite(ctx):
    embed = discord.Embed(
        title = "Lade den Bot auf deinen Server ein!",
        url = "https://zerobot.ml/invite"
    )
    await ctx.send(embed = embed)

@client.event
async def on_message(message):

    # Do not allow to use the bots in private messages.
    if message.guild:
        with open('tokens/mention.txt','r') as file:
            MENTION = file.read()
        with open('tokens/prefix.txt','r') as file:
            PREFIXFORCOMMANDS = file.read()
        if message.content.lower() == MENTION:
                await message.channel.send("The Prefix is: `" + PREFIXFORCOMMANDS + "`")

        if message.content.lower() == "hallo":
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

                
        if message.content.lower() == "moin":
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

        if message.content.lower() == "servus":
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

        if message.content.lower() == "hi":
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
                #stuff
            
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
                    file_object.write(f"Time: [{str(rn_tG.strftime('%d.%m.%y at %H:%M:%S'))}] - Server: {message.guild.name} ID: {message.guild.id} - Owner: {message.guild.owner} - Region: [{message.guild.region}] - Member-Count: [{message.guild.member_count}] - Icon-URL: [{message.guild.icon_url}]")
                    file_object.write("\n")
                    file_object.write("----------------------------------------")
                    msg = message
                    channel = client.get_channel(833599876721803274)
                    embed=discord.Embed(title=f"{message.content}")
                    embed.set_author(name=f"User: {str(message.author)} | {str(message.author.mention)}", icon_url=f"{message.author.avatar_url}")
                    embed.set_thumbnail(url=f"{message.guild.icon_url}")
                    embed.add_field(name=f"Channel", value=f"{msg.channel} - {msg.channel.mention}", inline=True)
                    embed.add_field(name=f"Server", value=f"{msg.guild.name} - {msg.guild.id} | Owner: {msg.guild.owner.mention} | Region: {msg.guild.region} | Member-Count: {msg.guild.member_count}", inline=True)
                    embed.set_footer(text=f"{str(rn_tG.strftime('%d.%m.%y at %H:%M:%S'))} | Made by byZero")
                    await channel.send(embed=embed)

                    
                with open('tokens/prefix.txt','r') as file:
                    PREFIXFORCOMMANDS = file.read()
                
                if message.content.startswith(f"{PREFIXFORCOMMANDS}start"): #command to start quessing game
                    channel = message.channel
                    await channel.send(f"Quess the number from 0-35 by writing number in this channel! {message.author.mention}") #message that tells about the start of the game

                    number1 = random.randint(1,35) #picking random number from 1 - 35 and printing it
                    print(f'The Number for the "Guess The Number"-Game is: {number1}')
                    
                    number2 = str(number1) #converting int to str
                    
                    zahl = 0

                    def check(m):
                        return m.content == number2 and m.channel == channel #checking answers
                        zahl += 1
                    
                    msg = await client.wait_for('message', check=check)
                    await channel.send(f"Correct answer {message.author.mention}!".format(msg)) #tells who got the answer


                await client.process_commands(message)

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear (ctx, amount=6):
    await ctx.channel.purge(limit=amount + 1)
    msg = await ctx.send(f'I deleted {amount} messages.')
    await asyncio.sleep(10)
    await msg.delete()

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    print (f'Yea, so I just banned {member} if that\'s okay :)')
    embed=discord.Embed(title=f"Kicking {member}")
    embed.set_thumbnail(url="https://cdn.tixte.com/uploads/byzero.steals-code.tk/kootf9omu9a.gif")
    await ctx.send(embed=embed)
    channel = client.get_channel(833599876721803274)
    embed=discord.Embed(title=f"Kicking {member} on {ctx.guild.name}")
    embed.set_thumbnail(url="https://cdn.tixte.com/uploads/byzero.steals-code.tk/kootf9omu9a.gif")
    await channel.send(embed=embed)
    


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    print (f'Yea, so I just banned {member} if that\'s okay :)')
    embed=discord.Embed(title=f"Banning {member}")
    embed.set_thumbnail(url="https://cdn.tixte.com/uploads/byzero.steals-code.tk/koota42pn9a.gif")
    await ctx.send(embed=embed)
    channel = client.get_channel(833599876721803274)
    embed=discord.Embed(title=f"Banning {member} on {ctx.guild.name}")
    embed.set_thumbnail(url="https://cdn.tixte.com/uploads/byzero.steals-code.tk/koota42pn9a.gif")
    await channel.send(embed=embed)


@client.command()
@commands.has_permissions(kick_members=True)
async def warn(ctx, member : discord.Member, *, reason=None):
    serverid = ctx.guild.id
    memberid = member.id
    # Open the file in append & read mode ('a+')
    with open(f"logs/members/server/{serverid}/member/{memberid}/warns.txt", "a+", encoding='utf-8') as file_object:
    # Move read cursor to the start of file.
        file_object.seek(0)
    # Check existing warns
        Warns = file.read()
        if Warns == '':
            Warns = '0'
    # Replace the target string
    NewWarns = int(Warns) + 1
    # Write the file out again
    with open('logs/members/server/{serverid}/member/{memberid}/warns.txt', 'a+') as file:
        file.write(NewWarns)

    # Add a Reason to it...
    with open('logs/members/server/{serverid}/member/{memberid}/warn-{NewWarns}.txt', 'a+') as file:
        file.write(reason)
    # Send Message to Member
    embed=discord.Embed(title="You have been warned!", description=f"Reason: {reason}")
    embed.set_author(name=f"{member}", icon_url=f"{member.avatar_url}")
    embed.set_thumbnail(url="https://media.tenor.com/images/932058cb6d102234800171857cb561f2/tenor.gif")
    embed.add_field(name=f"This is your {warn} warn!", value=f"{warn}/12", inline=False)
    embed.set_footer(text="Inspired by SteffoSpieler and Yasu | Coded by byZero#4840")
    await member.send(embed=embed)

    # Send Message to Author
    embed=discord.Embed(title="You warned {member}", description=f"Reason: {reason}")
    embed.set_thumbnail(url="https://media1.tenor.com/images/1797102f0bf828f52ce5e955e2286b5d/tenor.gif")
    embed.add_field(name=f"You sent {member} a nice message that I'm sure he will be happy about.", value="lol, why did you do that xD", inline=False)
    embed.set_footer(text="Inspired by SteffoSpieler and Yasu | Coded by byZero#4840")
    await ctx.author.send(embed=embed)

    # Send Message to Owner
    embed=discord.Embed(title=f"{ctx.author} warned {member}", description=f"Reason: {reason}")
    embed.set_thumbnail(url="https://media1.tenor.com/images/33ad6c19e8e5f1ca831ba00f4685e760/tenor.gif")
    embed.set_footer(text="Inspired by SteffoSpieler and Yasu | Coded by byZero#4840")
    await ctx.guild.send(embed=embed)

    # print if done
    print('I warned somebody lol')

@client.command()
async def warns(ctx, member : discord.Member):
    serverid = ctx.guild.id
    memberid = member.id
    # Open the file in append & read mode ('a+')
    with open(f"logs/members/server/{serverid}/member/{memberid}/warns.txt", "a+", encoding='utf-8') as file_object:
    # Move read cursor to the start of file.
        file_object.seek(0)
    # Check existing warns
        Warns = file.read()
        if Warns == '':
            Warns == '0'
    ctx.send(f'{member.mention} has already been warned {Warns} times')


# Rich Presence Changer
# Only limited to the Owner (byZero)
@client.command(aliases=['ps', 'status'])
@commands.is_owner()
async def presence(ctx, presence_type, presence):
  await ctx.channel.purge(limit=1)
  await ctx.author.send(f'The new Presence should be: ZeroBot is `{presence_type} {presence}`')
  if presence_type == "listening":
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=str(presence)))

  elif presence_type == "watching":
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=str(presence)))

  elif presence_type == "playing":
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=str(presence)))

  elif presence_type == "0":
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=str(presence)))

  elif presence_type == "1":
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=str(presence)))

  elif presence_type == "2":
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=str(presence)))
 


@client.command()
async def avatar(ctx, member : discord.Member):
    await ctx.author.send(str(member) + "'s avatar url is " + str(member.avatar_url))

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans ()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            print (f'I just unbanned {user.mention} if that\'s okay :)')
            return

@client.command()
async def dice(ctx):
        dice_result = random.randint(1, 6)
        if dice_result == 1:
            embed=discord.Embed(title="The dice whispered to me:")
            embed.set_thumbnail(url="https://cloud.0network.de/Discord/ZeroBot/Dice/1.png")
            embed.add_field(name="1", value="That's not much :O", inline=False)
            await ctx.send(embed=embed)

        if dice_result == 2:
            embed=discord.Embed(title="The dice whispered to me:")
            embed.set_thumbnail(url="https://cloud.0network.de/Discord/ZeroBot/Dice/2.png")
            embed.add_field(name="2", value="That's not better than 1, 1 + 1 is 2", inline=False)
            await ctx.send(embed=embed)

        if dice_result == 3:
            embed=discord.Embed(title="The dice whispered to me:")
            embed.set_thumbnail(url="https://cloud.0network.de/Discord/ZeroBot/Dice/3.png")
            embed.add_field(name="3", value="Did you know that 3 is the middle?", inline=False)
            await ctx.send(embed=embed)

        if dice_result == 4:
            embed=discord.Embed(title="The dice whispered to me:")
            embed.set_thumbnail(url="https://cloud.0network.de/Discord/ZeroBot/Dice/4.png")
            embed.add_field(name="4", value="The holy **4**!", inline=False)
            await ctx.send(embed=embed)

        if dice_result == 5:
            embed=discord.Embed(title="The dice whispered to me:")
            embed.set_thumbnail(url="https://cloud.0network.de/Discord/ZeroBot/Dice/5.png")
            embed.add_field(name="5", value="Why didn't you get a 6?", inline=False)
            await ctx.send(embed=embed)

        if dice_result == 6:
            embed=discord.Embed(title="The dice whispered to me:")
            embed.set_thumbnail(url="https://cloud.0network.de/Discord/ZeroBot/Dice/6.png")
            embed.add_field(name="6", value="You may roll the dice again :3", inline=False)
            await ctx.send(embed=embed)


@client.command()
async def pickrandom(ctx, number):
        dice_result = random.randint(1, int(number))
        await ctx.send('The random number is: ' + (str(dice_result)))

@client.command()
async def crash(ctx):
    crash_message = random.randint(1, 6)
    if crash_message == 1:
        await ctx.send('Crash yourself')

    if crash_message == 2:
        await ctx.send('I am not an old MS-DOS, I won\'t crash if you click a button. Look at yourself, maybe you can find an accordance between you and MS-DOS.')

    if crash_message == 3:
        await ctx.send('Error 176: This API-Request could not be send. Please try again later.')

    if crash_message == 4:
        await ctx.send('Crash yourself - TRASH yourself! I got a recycle bin on my desktop.')

    if crash_message == 5:
        await ctx.send('Why do you want me to crash? I won\'t do that until you tell me a reason for this.')


# Create Issue-Feature by jcw05
# https://github.com/joseywoermann
@client.command(aliases = ['createissue', 'report', 'bug', 'bugreport'])
async def makeissue(ctx, pTitle, pBody = None):

    with open('tokens/personalaccesstoken.txt','r') as file:
        DATOKEN = file.read()

    g = Github(DATOKEN)
    repo = g.get_repo("byZeroOfficial/ZeroBot")

    if pBody:
        issue = repo.create_issue(
            title=pTitle,
            body = pBody + " (Issue created by Discord-user `" + str(ctx.author) + "`)",
            assignee="byZeroOfficial",
        )
    else:
        issue = repo.create_issue(
            title=pTitle,
            body = "(Issue created by Discord-user `" + str(ctx.author) + "`)",
            assignee="byZeroOfficial",
        )

    issue_embed = discord.Embed(title = "Bug report has been sent!", description = "[View bug reports](https://github.com/byZeroOfficial/ZeroBot/issues)")
    await ctx.send(embed = issue_embed)

@client.command(aliases=['license'])
async def credits(ctx):
    embed=discord.Embed(title="Credits", description="Here are all my sources for code and information listed.", color=0x75e3ff)
    embed.set_author(name="byZero#4840")
    embed.add_field(name="Users", value="[jcw05#1331](https://github.com/joseywoermann)", inline=True)
    embed.add_field(name="Websites", value="[StackOverflow](https://stackoverflow.com/), [YouTube](https://youtube.com/), [GitHub](https://github.com/), [Pixabay](https://pixabay.com), [FreePix](https://freepix.com/)", inline=True)
    await ctx.send(embed=embed)

# Send messages as a bot.
@client.command(aliases=['s'])
@commands.is_owner()
async def write(ctx, *, text):
  await ctx.channel.purge(limit=1)
  await ctx.send(text)

@client.command(aliases=['featurerequest', 'requestfeature', 'idea'])
async def feature(ctx):
    await ctx.send('If you wanna make a Feature / Command-Request, look here: https://byzer0.ml/ejkqw')

@client.command()
@commands.has_permissions(manage_messages=True)
async def commandclear(ctx):
    def is_me(m):
      return m.author == client.user

    deleted = await ctx.channel.purge(limit=100, check=is_me)
    await ctx.send('Deleted {} message(s)'.format(len(deleted)))

@client.command()
@commands.has_role('Giveaways')
async def giveaway(ctx, mins : int, numberOfWinners: int, *, prize: str):
    await ctx.message.delete()
    embed=discord.Embed(title="<a:tadaaa:840305140502495272> GIVEAWAY!!!", description=prize, color=0xee1153)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://byzero.is-inside.me/DAYAr4h2.jpg")
    embed.set_footer(text=f"Winners = {str(numberOfWinners)}")
    end = datetime.datetime.utcnow() + datetime.timedelta(seconds = mins*60)
    embed.add_field(name="How to:", value="React to the message with the <a:tadaaa:840305140502495272>-Emoji so you can enter the giveaway.", inline=True)
    embed.timestamp = end
    sent_message = await ctx.send(embed=embed)
    await sent_message.add_reaction("<a:tadaaa:840305140502495272>")
    await asyncio.sleep(mins*60)
    new_message = await ctx.channel.fetch_message(sent_message.id)
    users = await new_message.reactions[0].users().flatten()
    users.pop(users.index(client.user))
    for i in range(numberOfWinners):
        member = random.choice(users)
        await ctx.send(member.mention)
        embed=discord.Embed(title="<a:tadaaa:840305140502495272> Congratulations!")
        embed.set_thumbnail(url="https://byzero.is-inside.me/a8XarhZG.gif")
        embed.add_field(name="Winner:", value=member.mention + f"You have won {prize}!", inline=True)
        embed.set_footer(text="Coded by byZero#4840")
        await ctx.send(embed=embed)

@client.command()
@commands.has_role('Giveaways')
async def cgiveaway(ctx, mins : int, numberOfWinners: int, giveawaychannel: int, *, prize: str):
    await ctx.message.delete()
    # Part of Channel-Send-System
    channel1 = client.get_channel(giveawaychannel)
    embed=discord.Embed(title="<a:tadaaa:840305140502495272> GIVEAWAY!!!", description=prize, color=0xee1153)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://byzero.is-inside.me/DAYAr4h2.jpg")
    embed.set_footer(text=f"Winners = {str(numberOfWinners)}")
    end = datetime.datetime.utcnow() + datetime.timedelta(seconds = mins*60)
    embed.add_field(name="How to:", value="React to the message with the <a:tadaaa:840305140502495272>-Emoji so you can enter the giveaway.", inline=True)
    embed.timestamp = end
    # Part of Channel-Send-System
    sent_message = await channel1.send(embed=embed)
    await sent_message.add_reaction("<a:tadaaa:840305140502495272>")
    await asyncio.sleep(mins*60)
    new_message = await channel1.fetch_message(sent_message.id)
    users = await new_message.reactions[0].users().flatten()
    users.pop(users.index(client.user))
    for i in range(numberOfWinners):
        member = random.choice(users)
        await channel1.send(member.mention)
        embed=discord.Embed(title="<a:tadaaa:840305140502495272> Congratulations!")
        embed.set_thumbnail(url="https://byzero.is-inside.me/a8XarhZG.gif")
        embed.add_field(name="Winner:", value=member.mention + f"You have won {prize}!", inline=True)
        embed.set_footer(text="Coded by byZero#4840")
        await channel1.send(embed=embed)

@client.command(aliases=["dev"])
async def developer(ctx):
    embed=discord.Embed(title="byZero#4840", url="https://byzer0.ml")
    embed.set_thumbnail(url="https://i.imgur.com/bp1UfAI.png")
    embed.add_field(name="👋 Hello! I am byZero.", value="I am byZero and I am a young developer and student. Currently I go to a secondary school near Bielefeld, Germany. Recently I created my own Discord-Bot.", inline=False)
    embed.add_field(name="Read more about me:", value="You can find more informations about me, here: https://byzer0.ml/github-info", inline=True)
    embed.set_footer(text="This Bot was coded by byZero!")
    await ctx.send(embed=embed)

# How Gay-Command like Dank Memer
@client.command(aliases=["gay"])
async def howgay(ctx):
    howgayareyourightnow = random.randint(1, 100)
    embed=discord.Embed(title="gay r8 machine", description="u are " + f'{howgayareyourightnow}' + "% gay 🏳️‍🌈", color=0x8000a3)
    embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

# Rickroll someone :D
@client.command(aliases=['rr'])
async def rickroll(ctx, member : discord.Member):
  with open('tokens/rickrollurl.txt','r') as file:
    RICKROLLURL = file.read()
  await ctx.channel.purge(limit=1)
  await member.send(RICKROLLURL)
  await ctx.author.send('So now, you rickrolled ' + f'{member}' + '!')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.channel.purge(limit=1)
        msg = await ctx.send('You don\'t have the role to perform this command!')
        await asyncio.sleep(5)
        await msg.delete()

@client.command()
@commands.is_owner()
async def spam(ctx, yon, amount: int, message):
    if yon == "-y":
       await ctx.channel.purge(limit=1)
       for i in range(amount):
            await ctx.send(f'{message}')
       
# Moves all Members from one to another one.
def in_voice_channel():  # check to make sure ctx.author.voice.channel exists
    def predicate(ctx):
        return ctx.author.voice and ctx.author.voice.channel
    return check(predicate)

@in_voice_channel()
@client.command()
@commands.has_permissions(manage_messages=True)
async def moveall(ctx, *, channel : discord.VoiceChannel, channelb : discord.VoiceChannel):
    vc = ctx.author.voice.channel.members
    for members in ctx.author.voice.channel.members:
        await members.move_to(channel)
        vc_users = ""
        for vc_user in vc:
            vc_users += '{},\n'.format(vc_user.mention)
    embed=discord.Embed(title="Users moved to different channel", color=0xf85454)
    embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://i.imgur.com/VtB4b8y.png")
    embed.add_field(name="Users", value=f"{vc_users}", inline=True)
    embed.add_field(name="Channel", value=f"{channel}", inline=True)
    await ctx.send(embed=embed)
    
@client.command()
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

# Question-Feature by jcw05
# https://github.com/joseywoermann
@client.command()
@commands.guild_only()
async def question(ctx, *, question):
    response = ['Yes', 'No', 'Maybe', 'Probably', 'Probably not']
    response_embed = discord.Embed(title="Question: \"" + str(question) + "\" Answer: " + str(random.choice(response)), color=0x1affbe)
    response_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)
    await ctx.send(embed=response_embed)

@client.command(aliases = ['bing'])
@commands.guild_only()
async def google(ctx, *, search_term):

    while ' ' in search_term:
        search_term = search_term.replace(' ', '+')

    await ctx.send("https://google.com/search?q=" + search_term)

@client.command()
@commands.is_owner()
async def pr(ctx):
    with open('tokens/presence.txt','r') as file:
        dapresence = file.read()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=dapresence))
    await ctx.author.send('I updated the Presence :D')

@client.command()
async def rps(ctx, what):
    if what == 'help':
        embed=discord.Embed(title="Rock paper scissors", description="Rock paper scissors (also known by other orderings of the three items, with rock sometimes being called stone, or as roshambo or ro-sham-bo)[1][2][3] is a hand game usually played between two people, in which each player simultaneously forms one of three shapes with an outstretched hand.")
        embed.set_author(name=str(ctx.author), url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://www.sciencemag.org/sites/default/files/styles/article_main_large/public/images/sn-rockpaper.jpg")
        await ctx.send(embed=embed) 
    number = random.randint(0, 3)
    if what == 'Rock':
        if number == 1:
            a = 'Rock'
            b = 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Rock-paper-scissors_%28rock%29.png/600px-Rock-paper-scissors_%28rock%29.png'
        if number == 2:
            a = 'Scissors'
            b = 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Rock-paper-scissors_%28scissors%29.png/600px-Rock-paper-scissors_%28scissors%29.png'
        if number == 3:
            a = 'Paper'
            b = 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Rock-paper-scissors_%28paper%29.png/600px-Rock-paper-scissors_%28paper%29.png' 
        embed=discord.Embed(title="Rock paper scissors", description=f"Just a funny game!")
        embed.set_author(name=str(ctx.author), url=ctx.author.avatar_url)
        embed.set_thumbnail(url=b)
        embed.add_field(name=a, value="lol", inline=True)
        await ctx.send(embed=embed)
    if what == 'Scissors':
        if number == 1:
            a = 'Rock'
            b = 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Rock-paper-scissors_%28rock%29.png/600px-Rock-paper-scissors_%28rock%29.png'
        if number == 2:
            a = 'Scissors'
            b = 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Rock-paper-scissors_%28scissors%29.png/600px-Rock-paper-scissors_%28scissors%29.png'
        if number == 3:
            a = 'Paper'
            b = 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Rock-paper-scissors_%28paper%29.png/600px-Rock-paper-scissors_%28paper%29.png' 
        embed=discord.Embed(title="Rock paper scissors", description=f"Just a funny game!")
        embed.set_author(name=str(ctx.author), url=ctx.author.avatar_url)
        embed.set_thumbnail(url=b)
        embed.add_field(name=a, value="lol", inline=True)
        await ctx.send(embed=embed)
    if what == 'Paper':
        if number == 1:
            a = 'Rock'
            b = 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Rock-paper-scissors_%28rock%29.png/600px-Rock-paper-scissors_%28rock%29.png'
        if number == 2:
            a = 'Scissors'
            b = 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Rock-paper-scissors_%28scissors%29.png/600px-Rock-paper-scissors_%28scissors%29.png'
        if number == 3:
            a = 'Paper'
            b = 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Rock-paper-scissors_%28paper%29.png/600px-Rock-paper-scissors_%28paper%29.png' 
        embed=discord.Embed(title="Rock paper scissors", description=f"Just a funny game!")
        embed.set_author(name=str(ctx.author), url=ctx.author.avatar_url)
        embed.set_thumbnail(url=b)
        embed.add_field(name=a, value="lol", inline=True)
        await ctx.send(embed=embed)

# Short-Url-Feature by jcw05
# https://github.com/joseywoermann
@client.command()
async def short(ctx, long_url):
    with open('tokens/shortio.txt','r') as file:
        shortio_token = file.read()

    r = requests.post('https://api.short.io/links/public', {
          'domain': 'zerobot.ml',
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

@client.command()
async def changelog(ctx):
    with open('tokens/changelog.txt','r') as file:
        Changelog = file.read()
    embed=discord.Embed(title="Changelog", description=Changelog, color=0x14c5c8)
    embed.set_footer(text="Made by byZero#4840")
    await ctx.send(embed=embed)

@client.command(aliases=['stats'])
async def botinfo(ctx):
    appinfo = await client.application_info() 
    embed=discord.Embed(title="Bot-Information", color=0xff0582)
    embed.set_thumbnail(url="https://cloud.0network.de/Discord/ZeroBot/ZeroBot.png")
    embed.add_field(name="📄 Name", value="ZeroBot", inline=True)
    embed.add_field(name="👑 Bot Owner", value=f"{appinfo.owner.mention}", inline=True)
    embed.add_field(name="👩‍🤝‍🧑🏽 Users", value=f"`{len(client.users)}`", inline=True)
    embed.add_field(name="📁Server", value=f"`{len(client.guilds)}`", inline=True)
    embed.add_field(name="📄 Commands", value=f"`{len(client.commands)}`", inline=True)
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
    embed.set_footer(text="Made by byZero#4840")
    await ctx.send(embed=embed)

@client.command()
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


# Token-File located in /root/Bots/ZeroBot/tokens/token.txt
with open('tokens/token.txt','r') as file:
    TOKEN = file.read()
client.run(TOKEN)
# There is a more recent Version! Go check it out :D
import discord
import random
import asyncio
import os
from github import Github
from pprint import pprint
from discord.ext import commands
from discord.ext.commands import check
import datetime
import requests
from bs4 import BeautifulSoup
import logging

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
with open('tokens/prefix.txt','r') as file:
    PREFIXFORCOMMANDS = file.read()
client = commands.Bot(command_prefix = PREFIXFORCOMMANDS, intents = intents)
client.remove_command('help')

# Message for Starting the Bot
@client.event
async def on_ready():
    with open('tokens/firstprint.txt','r') as file:
        firstprint = file.read()
    with open('tokens/secondprint.txt','r') as file:
        secondprint = file.read()
    print (firstprint)
    print (secondprint)
    with open('tokens/presence.txt','r') as file:
        dapresence = file.read()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=dapresence))
    channel = client.get_channel(817308210003968041)
    await channel.send('I am back online again :) <:zerobot:817428838665551892> ')

# Message on join and leave
@client.event
async def on_member_join(member):
    print (str(member) + ' has joined the server.')

@client.event
async def on_member_remove(member):
    print (str(member) + ' has left the server.')

@client.command(aliases=['pong', 'latency'])
async def ping(ctx):
    await ctx.send(f'🏓 Pong! - The Bot has a latency of {round(client.latency * 1000)} ms!')

# Hilfe-Command
@client.command(aliases=['hilfe'])
async def help(ctx):
   # General Commands
   with open('tokens/prefix.txt','r') as file:
    PREFIXFORCOMMANDS = file.read()
   embed=discord.Embed(title="Help - Prefix: ``" + PREFIXFORCOMMANDS + "``", description="Here you can find all commands listed, which you can use with my bot :)", color=0x6ce2e4)
   embed.set_author(name="ZeroBot", icon_url="https://i.imgur.com/SExHItg.png")
   embed.add_field(name="General Commands", value="Just the general commands, like _avatar - [here](https://byzer0.ml/zerobot-general)", inline=True)
   embed.add_field(name="Mod-Commands", value="That's commands only limited to moderators. - [here](https://byzer0.ml/zerobot-mod)", inline=True)
   embed.add_field(name="Fun-Commands", value="Have fun with that commands :D - [here](https://byzer0.ml/zerobot-fun)", inline=True)
   embed.add_field(name="Admin-Commands", value="Haha! That's a command list for me :D - [here](https://byzer0.ml/zerobot-admin)", inline=True)
   embed.set_footer(text="Use _feature to make command-idea!")
   await ctx.author.send(embed=embed)
   await ctx.channel.purge(limit=1)

@client.event
async def on_message(message):
  if message.author.id != 817092531874693131:
    #stuff
    with open('tokens/mention.txt','r') as file:
        MENTION = file.read()
    with open('tokens/prefix.txt','r') as file:
        PREFIXFORCOMMANDS = file.read()
    if message.content.lower() == MENTION:
            await message.channel.send("The Prefix is: ``" + PREFIXFORCOMMANDS + "``")

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


    # Do not allow to use the bots in private messages.
    with open('tokens/prefix.txt','r') as file:
        PREFIXFORCOMMANDS = file.read()
    if message.content.startswith(PREFIXFORCOMMANDS):
        if message.guild:
            await client.process_commands(message)
        else:
            await message.channel.send("This Bot is not available in private chats")

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

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    print (f'Yea, so I just banned {member} if that\'s okay :)')

@client.command()
async def updates(ctx):
    await ctx.send('``Added a few new commands!``')

# Rich Presence Changer
# Only limited to the Owner (byZero)
@client.command(aliases=['ps', 'status'])
@commands.is_owner()
async def presence(ctx, presence_type, presence):
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
        TOKEN = file.read()

    g = Github(TOKEN)
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
    await ctx.send('If you wanna make a Feature / Command-Request, look here: https://byzer0.ml/Q7vZJu')

@client.command()
@commands.has_permissions(manage_messages=True)
async def commandclear(ctx):
    def is_me(m):
      return m.author == client.user

    deleted = await ctx.channel.purge(limit=100, check=is_me)
    await ctx.send('Deleted {} message(s)'.format(len(deleted)))

@client.command()
@commands.has_role('Giveaways')
async def giveaway(ctx, mins : int, *, prize: str):
    await ctx.channel.purge(limit=1)
    embed=discord.Embed(title="🎉 GIVEAWAY!!!", description=f"{prize}", color=0xee1153)
    embed.set_thumbnail(url="https://i.imgur.com/ONvsLto.jpg")
    end = datetime.datetime.utcnow() + datetime.timedelta(seconds = mins*60)
    embed.add_field(name="How to:", value="React to the message with the :tada:-Emoji so you can enter the giveaway.", inline=True)
    embed.set_footer(text = "Giveaway is ending at: " f"{end} UTC")
    sent_message = await ctx.send(embed = embed)
    await sent_message.add_reaction("🎉")
    await asyncio.sleep(mins*60)
    new_message = await ctx.channel.fetch_message(sent_message.id)
    users = await new_message.reactions[0].users().flatten()
    users.pop(users.index(client.user))
    theoneandonly = random.choice(users)
    member = theoneandonly
    await ctx.send(member.mention)
    embed=discord.Embed(title="🎉 Congratulations!")
    embed.set_thumbnail(url="https://media.giphy.com/media/g9582DNuQppxC/giphy.gif")
    embed.add_field(name="Winner:", value=member.mention + f"You have won {prize}!", inline=True)
    embed.set_footer(text="Coded by byZero#4840")
    await ctx.send(embed=embed)

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

@client.command()
@commands.guild_only()
async def question(ctx, *, question):
    response = ['Ja', 'Nein', 'Vielleicht', 'Wahrscheinlich', 'Wahrscheinlich nicht']
    response_embed = discord.Embed(title="Deine Frage: \"" + str(question) + "\" Die Antwort: " + str(random.choice(response)), color=0x1affbe)
    response_embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)
    await ctx.send(embed=response_embed)

@commands.command(aliases = ['bing'])
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
    ctx.author.send('I updated the Presence :D')

# Token-File located in /home/discord/bots/ZeroBot/dctoken/token.txt
with open('tokens/token.txt','r') as file:
    TOKEN = file.read()
client.run(TOKEN)
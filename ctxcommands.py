import discord
from discord.ext import commands
import datetime
import time 
import requests
import json
import subprocess
import typing
import random

#config :

prefix = ';'
token = 'NzA1MTc2NjYyMzY2NDg2NTI5.Xqn5AQ.FUYBk7XlBP-6RglVFrNLAC8lDVA'
#the bot's game it is playing.
botgame = 'on your mother'
#This is your id for your logs channel so the bot logs what happens.
log = 711736896832929862

#-----------------------------------------

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

client = commands.Bot(command_prefix = prefix)

@client.command()
async def roll(ctx):
  number = random.randint(1, 1000)
  await ctx.send(f"{number} out of 1000")
'''
@client.command()
async def say(ctx, *, arg):
  await ctx.send(arg)
'''
@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)} ms")
'''
@client.command()
async def akatsuki(ctx, *, arg):
  r = requests.get(f"https://akatsuki.pw/api/v1/users/rxfull?id={arg}")
  x = r.json()
  df = pandas.DataFrame(x['????'])
  await ctx.send(f"{df}")
'''
@client.command()
async def ban(ctx, members: commands.Greedy[discord.Member],
                   delete_days: typing.Optional[int] = 0, *,
                   reason: str):
    """Mass bans members with an optional delete_days parameter"""
    for member in members:
        timeStr = time.ctime()
        await member.ban(delete_message_days=delete_days, reason=reason)
        channel = client.get_channel(log)
        await channel.send(f"``{member}`` was banned for ``{reason}`` at ``{timeStr}``")

@client.command()
async def unban(ctx, *, member):
  banned_users = await ctx.guild.bans()
  member_name, member_discriminator = member.split('#')

  for ban_entry in banned_users:
    user = ban_entry.user
  
  if (user.name, user.discriminator) == (member_name, member_discriminator):
    timeStr = time.ctime()
    await ctx.guild.unban(user)
    await ctx.send(f"done.")
    channel = client.get_channel(log)
    await channel.reply(f" has unbanned ``{user}`` on ``{timeStr}``")

@client.command()
async def kick(ctx, user: discord.Member, *, reason=None):
  await user.kick(reason=reason)
  await ctx.send(f"{user} have been kicked sucessfully")

##Logging status etc

@client.event
async def on_message(message):
  await client.wait_until_ready()  
  await client.process_commands(message)
  print(f"{bcolors.OKGREEN}[{datetime.datetime.now().time()}] [#{message.channel}] {message.author}: {message.content}")

@client.event
async def on_ready():
  print('CTX Commands are online!')
  await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing,
                                                                               name=botgame))
client.run(token)
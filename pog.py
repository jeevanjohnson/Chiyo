import discord
import os
from discord.ext import commands
import datetime
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

client = commands.Bot(command_prefix = ';', case_insensitive=True)

@client.command()
async def load(ctx, extension):
	client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f"cogs.{filename[:-3]}")
		
@client.event
async def on_message(message):
  await client.wait_until_ready()  
  await client.process_commands(message)
  print(f"{bcolors.OKGREEN}[{datetime.datetime.now().time()}] [#{message.channel}] {message.author}: {message.content}")

@client.event
async def on_ready():
  print('Pog..')
  timeStr = time.ctime()
  channel = client.get_channel(705683011160637440)
  await channel.send(f"New Update to Pogbot! ``{timeStr}``")
  await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing,
                                                                               name='on your mother'))

client.run('token')
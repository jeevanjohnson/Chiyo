import discord
import config
import os
import datetime
import requests
from discord.ext import commands
import enum
from enum import IntEnum

client = commands.Bot(command_prefix=config.prefix, case_insensitive=True)

@client.event
async def on_ready():
	print('Ready!')
	await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing,
                                                                               name=config.game))

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f"cogs.{filename[:-3]}")

@client.event
async def on_message(message):
  await client.wait_until_ready()  
  await client.process_commands(message)
  print(f"[{datetime.datetime.now().time()}] [#{message.channel}] {message.author}: {message.content}")

client.run(config.token)
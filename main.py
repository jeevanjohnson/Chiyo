import os
import uvloop
import config
import asyncio
from ext import glob
from pymongo import MongoClient
from discord.ext import commands

bot = glob.bot = commands.Bot(
    command_prefix = config.default_prefix, # TODO: Custom prefix
    help_command = None,
    description = 'another osu! discord bot that exist but tiny and owo already exist so shrug'
)

files = os.listdir('./cogs')
for file in files:
    # Load all commands
    if not file.endswith('.py'):
        continue
    
    __import__(f'cogs.{file[:-3]}')

# Load events
__import__('events')

# Connects to Database
db = MongoClient(
    config.connection_access
)
for p in config.collection_path:
    db = db[p]

glob.db = db

from bg_loops import (
    mainbgtask
)
loop = asyncio.get_event_loop()
loop.create_task(mainbgtask())

import uvloop
uvloop.install()
bot.run(config.token)
import os
import time
import config
import asyncio
from ext import glob
from WebLamp import log
from WebLamp import Fore
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

async def background_task():
    while True:
        await asyncio.sleep(120)
        log('Running Background Task!', Fore.YELLOW)

        for k, v in glob.cache.copy().items():
            if time.time() >= v[1]:
                del glob.cache[k]
                log(f'Removed {v} from cache!', Fore.YELLOW)

loop = asyncio.get_event_loop()
loop.create_task(background_task())

bot.run(config.token)
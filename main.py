import os
import uvloop
import config
from ext import glob
from objects import Mongo
from discord.message import Message
from discord.ext.commands import Bot

def get_prefix(bot: Bot, msg: Message) -> str:
    guild_id = msg.guild.id
    db = glob.db.prefixes
    if guild_id in glob.cache.prefixes:
        return glob.cache.prefixes[guild_id]
    
    # Kinda long
    if not (p := db.find_one({"_id": guild_id})):
        return config.default_prefix
    else:
        glob.cache.prefixes[guild_id] = p['prefix']
        return p['prefix']

bot = glob.bot = Bot(
    command_prefix = get_prefix,
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
glob.db = Mongo()

from bg_loops import mainbgtask
glob.loop.create_task(mainbgtask())

import uvloop
uvloop.install()
bot.run(config.token)
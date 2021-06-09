import aiohttp
import asyncio
from objects import Cache
from discord.ext.commands import Bot
from pymongo.collation import Collation

bot: Bot
db: Collation
mode = True

cache = Cache()
http = aiohttp.ClientSession()
loop = asyncio.get_event_loop()
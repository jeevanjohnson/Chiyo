import aiohttp
from objects import Cache
from discord.ext.commands import Bot
from pymongo.collation import Collation

bot: Bot
db: Collation
mode = True

cache = Cache()
http = aiohttp.ClientSession()
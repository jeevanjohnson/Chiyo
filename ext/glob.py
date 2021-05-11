import aiohttp
from discord.ext.commands import Bot
from pymongo.collation import Collation

bot: Bot
db: Collation
mode = True

cache = {}
http = aiohttp.ClientSession()
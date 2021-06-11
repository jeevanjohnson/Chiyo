import aiohttp
import asyncio
from objects import Cache
from typing import TYPE_CHECKING
from discord.ext.commands import Bot

if TYPE_CHECKING:
    from objects import Mongo

bot: Bot
db: 'Mongo'
mode = True

cache = Cache()
http = aiohttp.ClientSession()
loop = asyncio.get_event_loop()
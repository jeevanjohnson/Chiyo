import time
import discord
import asyncio
from ext import glob
from ext.glob import bot
from varname import nameof
from WebLamp import (Fore, log)

cache = glob.cache
async def mainbgtask():
    while True:
        await asyncio.sleep(120)
        log('Running Background Task!', Fore.YELLOW)

        cache_tuple = (cache.channel_beatmaps, cache.scores)
        for i, dictionary in enumerate(cache_tuple):
            index = int(i == 1) + 1
            
            for k, v in dictionary.copy().items():
                if time.time() >= v[index]:
                    del dictionary[k]
                    log(f'Removed {v} from {nameof(dictionary)} cache!', 
                        Fore.YELLOW)
        
        servers = len(bot.guilds)
        await bot.change_presence(
            status = discord.Status.online, 
            activity = discord.Activity(
            type = discord.ActivityType.playing, 
            name = f"in {servers} Servers! | Supports Akatsuki & Bancho!")
        )
        log('Updated Presence!', Fore.YELLOW)
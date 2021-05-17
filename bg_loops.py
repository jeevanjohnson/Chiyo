import time
import discord
import asyncio
from ext import glob
from ext.glob import bot
from WebLamp import (Fore, log)

async def mainbgtask():
    while True:
        await asyncio.sleep(120)
        log('Running Background Task!', Fore.YELLOW)

        for k, v in glob.cache.channel_beatmaps.copy().items():
            if time.time() >= v[1]:
                del glob.cache.channel_beatmaps[k]
                log(f'Removed {v} from channel_beatmaps cache!', Fore.YELLOW)
        
        servers = len(bot.guilds)
        await bot.change_presence(
            status = discord.Status.online, 
            activity = discord.Activity(
            type = discord.ActivityType.playing, 
            name = f"in {servers} Servers!")
        )
        log('Updated Presence!', Fore.YELLOW)
import re
import time
import config
import discord
from ext import glob
from WebLamp import log
from ext.glob import bot
from WebLamp import Fore
from typing import Union
from pprint import pformat
from objects import Beatmap
from discord.message import Message
from discord.ext.commands import Context
from discord.ext.commands.errors import (
    CommandNotFound, CommandOnCooldown
)

BEATMAP = re.compile(
    r"https://(akatsuki\.pw|osu\.ppy\.sh)/b/(?P<id>[0-9]*)|"
    r"https://osu\.ppy\.sh/beatmapsets/(?P<setid>[0-9]*)#(osu|fruits|taiko|mania)/(?P<bid>[0-9]*)|"
    r"https://(osu\.ppy\.sh/beatmapsets|akatsuki\.pw/d)/(?P<setidd>[0-9]*)"
)
TWELVEHOURS = 12 * 60 * 60

async def get_id_from_set(setid: Union[str, int]) -> int:
    """Returns the highest difficulty of a set's id"""
    base = 'https://osu.ppy.sh/api'
    path = 'get_beatmaps'
    params = {
        'k': config.api_key,
        's': setid,
        'a': 1
    }

    async with glob.http.get(
        url = f'{base}/{path}',
        params = params
    ) as resp:
        if not resp or resp.status != 200:
            return
        
        if not (json := await resp.json()):
            return
    
    key = lambda x: float(x['difficultyrating'])
    json = sorted(json, key = key, reverse = True)
    
    return int(json[0]['beatmap_id'])

@bot.event
async def on_ready():
    servers = len(bot.guilds)
    msg = f'{bot.user} is online! | Currently in {servers} server(s)!'
    log(msg, Fore.GREEN)

    await bot.change_presence(
        status = discord.Status.online, 
        activity = discord.Activity(
        type = discord.ActivityType.playing, 
        name = f"in {servers} Servers!")
    )

@bot.event
async def on_message(message: Message):
    await bot.wait_until_ready()
    await bot.process_commands(message)

    m = f'{message.content}'
    if message.embeds:
        m += f' | Embeds: {message.embeds}'
    
    if message.attachments:
        m += f' | Attachments: {message.attachments}'

    log(
        f'[{message.guild}] [{message.channel}] {message.author}: {m}',
        Fore.BLUE
    )
    
    beatmapids = BEATMAP.match(message.content)
    if not beatmapids:
        return
    
    bmapdict = beatmapids.groupdict()
    for key, bid in bmapdict.items():
        if not bid:
            continue
        
        if key == 'setidd':
            bid = await get_id_from_set(bid)
            if not bid:
                return
        
        bmap = await Beatmap.from_id(
            int(bid)
        )

        if not bmap:
            continue

        e = bmap.embed
        e.colour = message.author.color

        glob.cache[message.channel.id] = (bmap, time.time() + TWELVEHOURS)
        await message.channel.send(embed=e)
        return

@bot.event
async def on_command_error(ctx: Context, error) -> None:
    if isinstance(error, CommandNotFound):
        return
    
    if isinstance(error, CommandOnCooldown):
        await ctx.send(*error.args)
        return

    ctxdict = ctx.__dict__
    cover = bot.get_channel(713072038557777942)
    msg = (
        '<@343508538246561796>\n'
        f'```py\n{pformat(ctxdict)}\n\n'
        f'{repr(error)}```'
    )
    await cover.send(msg)

# Code passed this point is
# meant for my server that 
# can help with my development

# drag vc: 784646271838191616
# private vc: 743562646795714667
# Hideout guild id: 705649421857325139

@bot.event
async def on_voice_state_update(member, before, after) -> None:
    if member.guild.id != 705649421857325139:
        return
    
    private_vc = bot.get_channel(743562646795714667)
    if not glob.mode or not (channel := after.channel):
        return
    
    channel = after.channel
    if channel.id != 784646271838191616:
        return
    
    await member.move_to(private_vc)
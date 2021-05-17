import re
import config
from ext import glob
from typing import Any
from typing import Union
from pprint import pformat
from discord import Message
from discord import TextChannel

TWELVEHOURS = 12 * 60 * 60
BEATMAP = re.compile(
    r"https://(akatsuki\.pw|osu\.ppy\.sh)/b/(?P<id>[0-9]*)|"
    r"https://osu\.ppy\.sh/beatmapsets/(?P<setid>[0-9]*)#(osu|fruits|taiko|mania)/(?P<bid>[0-9]*)|"
    r"https://(osu\.ppy\.sh/beatmapsets|akatsuki\.pw/d)/(?P<setidd>[0-9]*)"
)

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

# Another word for log lol
async def note(**kwargs: tuple[Any]) -> None:
    msg = ['None Type was found!', '```py\n']
    for k, _obj in kwargs.items():
        if isinstance(_obj, Message):
            ...
        elif isinstance(_obj, dict):
            ...
        else:
            obj = f'{k} = {pformat(_obj)}'[:200]
        
        msg.append(obj)
    
    msg.append('```')
    cover: TextChannel = glob.bot.get_channel(713072038557777942)

    m = '\n'.join(msg)[:1997]
    if not m.endswith('```'):
        m += '```'

    await cover.send(content=m)
    return

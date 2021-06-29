import re
from ext import glob
from typing import Any
from pprint import pformat
from discord import Message
from discord import TextChannel

TWELVEHOURS = 12 * 60 * 60

BEATMAP = re.compile(
    r"https://osu\.ppy\.sh/beatmapsets/(?P<setid>[0-9]*)#(osu|fruits|taiko|mania)/(?P<bid>[0-9]*)|"
    r"https://(osu\.ppy\.sh/beatmapsets|akatsuki\.pw/d)/(?P<setidd>[0-9]*)|"
    r"https://(akatsuki\.pw|osu\.ppy\.sh)/b/(?P<id>[0-9]*)"
)

USERS = re.compile(
    r"https://(osu)\.ppy\.sh/users/([0-9A-Za-z]*)|"
    r"https://(osu).ppy.sh/u/([0-9A-Za-z]*)|"
    r"https://(akatsuki)\.pw/u/([0-9A-Za-z]*)"
)

SCORE_FMT = re.compile(
    r"https://osu\.ppy\.sh/scores/osu/(?P<id>[0-9]*)"
)

JSON_SCORE_FINDER = re.compile(
    r"<script id=\"json-show\" type=\"application/json\">\n(.*)\n    </script>"
)

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

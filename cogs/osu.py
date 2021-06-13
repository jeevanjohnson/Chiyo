import time
import config
from ext import glob
from json import loads
from ext.glob import bot
from objects import Mods
from objects import Score
from discord import Embed
from objects import Server
from objects import Beatmap
from typing import Optional
from objects import MsgContent
from helpers import TWELVEHOURS
from discord.message import Message
from discord.ext.commands import Context

arrows = ('⬅️', '➡️')

@bot.command()
async def connect(ctx: Context) -> None:
    parsed: Optional[MsgContent] = await MsgContent.from_discord_msg(ctx, 'connect')
    if not parsed:
        return
    
    db = glob.db.users
    user = db.find_one({'_id': ctx.author.id})
    server_name = parsed.server.name.lower()
    p = parsed.player
    
    if user is None:
        post = {
            "_id": ctx.author.id,
            server_name: p.id
        }
        db.insert_one(post)
    else:
        new_values = {
            "$set": {
                server_name: p.id
            }
        }
        db.update_one(user, new_values)

    e = Embed(
        colour = ctx.author.color
    )

    e.set_author(
        name = f'{p.name} was connected to your discord account!',
        url = bot.user.avatar_url
    )

    e.set_image(
        url = p.avatar
    )

    await ctx.send(
        content = f'{time.time()-parsed.start_time:.2f}',
        embed = e
    )
    return

@bot.command(aliases=['c'])
async def compare(ctx: Context) -> None:
    if ctx.message.channel.id not in glob.cache.channel_beatmaps:
        await ctx.send("No map was found.")
        return

    bmap: Beatmap = glob.cache.channel_beatmaps[ctx.message.channel.id][0]
    
    parsed: Optional[MsgContent] = await MsgContent.from_discord_msg(ctx)
    if not parsed:
        return

    if parsed.server == Server.Akatsuki:
        s = await Score.from_akatsuki(
            user = parsed.player,
            mode = parsed.mode,
            index = parsed.page,
            relax = parsed.relax,
            bmap = bmap
        )
    else:
        s = await Score.from_bancho(
            user = parsed.player,
            mode = parsed.mode,
            index = parsed.page,
            bmap = bmap
        )
    
    if not s:
        await ctx.send("Score or Player couldn't be found!")
        return

    key = (s.player.id, s.server)
    glob.cache.scores[key] = (
        s, 'c', time.time() + TWELVEHOURS
    )

    e = s.embed
    e.colour = ctx.author.color
    msg: Message = await ctx.send(
        content = f'{time.time()-parsed.start_time:.2f}s',
        embed = e
    )

    for emoji in arrows:
        await msg.add_reaction(emoji)
    
    return

@bot.command(aliases=['t'])
async def top(ctx: Context) -> None:
    parsed: Optional[MsgContent] = await MsgContent.from_discord_msg(ctx)
    if not parsed:
        return
    
    if parsed.server == Server.Akatsuki:
        s = await Score.from_akatsuki_top(
            user = parsed.player,
            mode = parsed.mode,
            index = parsed.page,
            relax = parsed.relax
        )
    else:
        s = await Score.from_bancho_top(
            user = parsed.player,
            mode = parsed.mode,
            index = parsed.page,
        ) 
    
    if not s:
        await ctx.send("Score or Player couldn't be found!")
        return
    
    msg_id = ctx.message.channel.id
    glob.cache.channel_beatmaps[msg_id] = (
        s.bmap, time.time() + TWELVEHOURS
    )

    key = (s.player.id, s.server)
    glob.cache.scores[key] = (
        s, 't', time.time() + TWELVEHOURS
    )

    e = s.embed
    e.colour = ctx.author.color
    msg: Message = await ctx.send(
        content = f'{time.time()-parsed.start_time:.2f}s',
        embed = e
    )

    for emoji in arrows:
        await msg.add_reaction(emoji)
    
    return

@bot.command(aliases=['r', 'rs', 'rc'])
async def recent(ctx: Context) -> None:
    parsed: Optional[MsgContent] = await MsgContent.from_discord_msg(ctx)
    if not parsed:
        return
    
    if parsed.server == Server.Akatsuki:
        s = await Score.from_akatsuki_recent(
            user = parsed.player,
            mode = parsed.mode,
            index = parsed.page,
            relax = parsed.relax
        )
    else:
        s = await Score.from_bancho_recent(
            user = parsed.player,
            mode = parsed.mode,
            index = parsed.page
        ) 
    
    if not s:
        await ctx.send("Score or Player couldn't be found from the last 24 hours.")
        return
    
    msg_id = ctx.message.channel.id
    glob.cache.channel_beatmaps[msg_id] = (
        s.bmap, time.time() + TWELVEHOURS
    )
    
    key = (s.player.id, s.server)
    glob.cache.scores[key] = (
        s, 'r', time.time() + TWELVEHOURS
    )

    e = s.embed
    e.colour = ctx.author.color
    msg: Message = await ctx.send(
        content = f'{time.time()-parsed.start_time:.2f}s',
        embed = e
    )

    for emoji in arrows:
        await msg.add_reaction(emoji)
    
    return

@bot.command(aliases=['p', 'osu'])
async def profile(ctx: Context) -> None:
    parsed: Optional[MsgContent] = await MsgContent.from_discord_msg(ctx)
    if not parsed:
        return
    
    p = parsed.player

    if not p:
        await ctx.send("User couldn't be found!")
        return
    
    e = p.embed
    e.colour = ctx.author.color
    await ctx.send(
        content = f'{time.time()-parsed.start_time:.2f}s',
        embed = e
    )
    return

@bot.command()
async def ar(ctx: Context) -> None:
    msg = ctx.message.content.lower().split()[1:]
    if not msg:
        await ctx.send(
            'Please return ar & mod combination (optional)'
        )
        return
    
    aproach_rate: float = None
    mods: Mods = Mods.NOMOD
    for m in msg:
        if m.isalpha():
            mods = Mods.from_str(m)
        else:
            try: aproach_rate = float(m)
            except: pass
        
    if not aproach_rate:
        await ctx.send('Return an aproach rate.')
        return
    
    speed_multiplier = 1.0
    if mods & (Mods.DOUBLETIME | Mods.NIGHTCORE):
        speed_multiplier = 1.5
    elif mods & Mods.HALFTIME:
        speed_multiplier = 0.75
    
    if mods & Mods.HARDROCK:
        aproach_rate *= 1.4
    elif mods & Mods.EASY:
        aproach_rate /= 2

    AR0_MS = 1800
    AR5_MS = 1200
    AR10_MS = 450

    AR_MS_STEP1 = (AR0_MS - AR5_MS) / 5.0
    AR_MS_STEP2 = (AR5_MS - AR10_MS) / 5.0

    ar_in_ms = AR0_MS

    if aproach_rate < 5:
        ar_in_ms = AR0_MS - AR_MS_STEP1 * aproach_rate
    else:
        ar_in_ms = AR5_MS - AR_MS_STEP2 * (aproach_rate - 5)
    
    ar_in_ms = min(AR0_MS, max(AR10_MS, ar_in_ms))
    ar_in_ms /= speed_multiplier

    if ar_in_ms > AR5_MS:
        aproach_rate = (AR0_MS - ar_in_ms) / AR_MS_STEP1
    else:
        aproach_rate = 5.0 + (AR5_MS - ar_in_ms) / AR_MS_STEP2
    
    await ctx.send(f'Ar: {aproach_rate:.2f}')
    return

@bot.command(aliases=['map'])
async def m(ctx: Context) -> None:
    start_time = time.time()
    mods = Mods.NOMOD
    acc: Optional[float] = None
    channel_id: int = ctx.message.channel.id
    if channel_id not in glob.cache.channel_beatmaps:
        await ctx.send("No map was found.")
        return

    bmap: Beatmap = glob.cache.channel_beatmaps[channel_id][0]
    msg: list[str] = ctx.message.content.lower().replace('%', '').split()[1:]

    for m in msg:
        if m.isalpha():
            mods = Mods.from_str(m)
            continue
        else:
            try: acc = float(m)
            except: pass

    bmap.mods = mods
    kwargs = {}

    if acc:
        kwargs['acc'] = (acc,)
    
    bmap.set_embed_pp(**kwargs)

    e = bmap.embed
    e.colour = ctx.author.color
    await ctx.send(
        content = f'{time.time()-start_time:.2f}s',
        embed = e
    )
    return

@bot.command(aliases=['pp_for_rank'])
async def ppfr(ctx: Context) -> None:
    mode = 0
    msg: list[str] = ctx.message.content.lower().split()[1:]
    if not msg:
        await ctx.send('Please provide a rank amount.')
        return
    
    if '-m' in msg:
        index = msg.index('-m') + 1
        if index > len(msg) - 1:
            await ctx.send('Please provide a mode. (as an integer)')
            return
        
        m: str = msg[index]
        if not m.isdecimal():
            await ctx.send(
                'Please provide the mode as a number\n'
                '0 = osu!, 1 = taiko, 2 = ctb, 3 = osu!mania\n'
            )
            return
        
        mode = int(m)
        del msg[index]
        del msg[index - 1]
    
    rank: str = msg[0]
    if not rank.isdecimal():
        await ctx.send('Ranking needs to be a number.')
        return
    
    url = f'https://osudaily.net/api/pp.php'
    params = {
        'k': config.osu_daily_api_key,
        't': 'rank',
        'v': rank,
        'm': mode
    }

    async with glob.http.get(url, params=params) as resp:
        if not resp or resp.status != 200:
            await ctx.send("Couldn't get any values.")
            return
        
        json = loads(await resp.text())
        if not json:
            await ctx.send("Couldn't get any values.")
            return

    mode_str = ('osu!std', 'osu!taiko', 'osu!ctb', 'osu!mania')[mode]
    await ctx.send(
        'You would need `{pp:,.2f}PP` to reach rank `{rank:,}` on {mode}.'.format(
            **json, mode = mode_str
        )
    )
    return

@bot.command(aliases=['rank_for_pp'])
async def rfpp(ctx: Context) -> None:
    mode = 0
    msg: list[str] = ctx.message.content.lower().split()[1:]
    if not msg:
        await ctx.send('Please provide a pp amount.')
        return
    
    if '-m' in msg:
        index = msg.index('-m') + 1
        if index > len(msg) - 1:
            await ctx.send('Please provide a mode. (as an integer)')
            return
        
        m: str = msg[index]
        if not m.isdecimal():
            await ctx.send(
                'Please provide the mode as a number\n'
                '0 = osu!, 1 = taiko, 2 = ctb, 3 = osu!mania\n'
            )
            return
        
        mode = int(m)
        del msg[index]
        del msg[index - 1]
    
    pp: str = msg[0]
    if not pp.isdecimal():
        await ctx.send('PP amount needs to be a number.')
        return
    
    url = f'https://osudaily.net/api/pp.php'
    params = {
        'k': config.osu_daily_api_key,
        't': 'pp',
        'v': pp,
        'm': mode
    }

    async with glob.http.get(url, params=params) as resp:
        if not resp or resp.status != 200:
            await ctx.send("Couldn't get any values.")
            return
        
        json = loads(await resp.text())
        if not json:
            await ctx.send("Couldn't get any values.")
            return

    mode_str = ('osu!std', 'osu!taiko', 'osu!ctb', 'osu!mania')[mode]
    await ctx.send(
        'You would be rank `{rank:,}` for `{pp:,.2f}PP` on {mode}.'.format(
            **json, mode = mode_str
        )
    )
    return
import time
from ext import glob
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
    
    arms = min(AR0_MS, max(AR10_MS, ar_in_ms))
    arms /= speed_multiplier

    if arms > AR5_MS:
        aproach_rate = (AR0_MS - arms) / AR_MS_STEP1
    else:
        aproach_rate = 5.0 + (AR5_MS - arms) / AR_MS_STEP2
    
    await ctx.send(f'Ar: {aproach_rate:.2f}')
    return
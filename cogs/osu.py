import time
from ext import glob
from ext.glob import bot
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
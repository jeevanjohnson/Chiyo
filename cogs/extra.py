from ext import glob
from ext.glob import bot
from discord import Embed
from discord.ext.commands import has_permissions
from discord.ext.commands.context import Context

FAQ = '\n'.join([
    '**Top**',
    '{prefix}t | {prefix}top',
    "Shows a top play from a user's profile",
    'Args: name of player | -p (a whole number) | '
    '-std | -taiko | -ctb | -mania | -rx | -akatsuki',
    '',
    '**Recent**',
    '{prefix}r | {prefix}rs | {prefix}rc | {prefix}recent',
    "Shows a recent score from a user's profile",
    'Args: name of player | -p (a whole number) | '
    '-std | -taiko | -ctb | -mania | -rx | -akatsuki',
    '',
    '**Profile**',
    '{prefix}p | {prefix}osu | {prefix}profile',
    "Shows a profile for a user.",
    'Args: name of player | -std | -taiko | '
    '-ctb | -mania | -rx | -akatsuki',
    '',
    '**Compare**',
    '{prefix}c | {prefix}compare',
    "Compares a score from a recently posted beatmap.",
    'Args: name of player | -p (a whole number) | -std | -taiko | '
    '-ctb | -mania | -rx | -akatsuki',
    '',
    '**Connect**',
    '{prefix}connect',
    "Connects a profile to your discord account.",
    "Args: name of player | -akatsuki",
    '',
    '**Approach Rate**',
    '{prefix}ar',
    'Calculates ar depending on the mods given.',
    'Args: original ar number | mod combination (ex. dthdhrfl)',
    '',
    '**Rank for pp**',
    '{prefix}rfpp | {prefix}rank_for_pp',
    'Gets rank for the pp amount given.',
    'Args: pp number | -m (a whole number)',
    '',
    '**Map**',
    '{prefix}m | {prefix}map',
    'Sends an embed with details of the given map.',
    '**These args only work on std**',
    'Args: mod combination (ex. dthdhrfl) | acc (ex. 100 or 98.5)'
    '',
    '**PP for rank**',
    '{prefix}ppfr | {prefix}pp_for_rank',
    'Gets pp for the rank given.',
    'Args: rank number | -m (a whole number)',
])

@bot.command(aliases=["changeprefix", "change_prefix"])
@has_permissions(administrator=True)
async def prefix(ctx: Context) -> None:
    p = ''.join(ctx.message.content.split()[1:])
    db = glob.db.prefixes

    if not p:
        await ctx.send(
            'Please provide a prefix!'
        )
        return

    pre = db.find_one({"_id": ctx.guild.id})
    if pre is None:
        post = {
            "_id": ctx.guild.id,
            "prefix": p
        }
        db.insert_one(post)
    else:
        new_values = {
            "$set": {
                "prefix": p
            }
        }
        db.update_one(pre, new_values)
    
    glob.cache.prefixes[ctx.guild.id] = p
    
    await ctx.send(
        f'Prefix has been changed to {p}'
    )

    return

@bot.command(aliases=['h', 'faq', 'commands'])
async def help(ctx: Context) -> None:

    p = await glob.bot.get_prefix(ctx.message)
    e = Embed(
        description = FAQ.format(prefix = p),
        color = ctx.author.color
    )

    e.set_author(
        name = 'Chiyo! Another osu! discord bot.',
        url = 'https://github.com/coverosu/Chiyo',
        icon_url = 'https://southportlandlibrary.com/wp-content/uploads/2020/11/discord-logo-1024x1024.jpg'
    )

    e.set_thumbnail(
        url = bot.user.avatar_url
    )

    e.set_footer(
        text = 'All commands for Chiyo!'
    )

    await ctx.send(embed=e)
    return
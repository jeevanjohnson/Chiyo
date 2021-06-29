from ext import glob
from ext.glob import bot
from discord import Embed
from random import randint
from typing import Optional
from functools import cache
from discord.ext.commands.core import Command
from discord.ext.commands import has_permissions
from discord.ext.commands.context import Context

@bot.command(aliases=["changeprefix", "change_prefix"])
@has_permissions(administrator=True)
async def prefix(ctx: Context) -> None:
    """
    Changes prefix used for a certain server
    (for example ;help can become !help)
    (You need administrator permissions in order to user this command)
    Args: prefix
    """
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

@cache
def faq(prefix: str) -> str:
    msg = ''
    for cmd in glob.bot.commands:
        cmd: Command
        m = ''
        if cmd.module == 'cogs.hideout':
            continue

        m += f'**{cmd.name.replace("_", " ").title()}**\n'
        m += f'{prefix}{cmd.name}'

        if cmd.aliases:
            m += ' |'
            for name in cmd.aliases:
                m += f' {prefix}{name} |'
        
        docs = cmd._callback.__doc__
        if docs is None:
            docs = "No documentation set!"
        else:
            docs = docs[5:][:-5]
        
        m += f'\n{docs}\n\n'
        msg += m

    return msg

@bot.command(aliases=['h', 'faq', 'commands'])
async def help(ctx: Context) -> None:
    """
    Shows documentation for all commands!
    """
    p = await glob.bot.get_prefix(ctx.message)
    
    e = Embed(
        description = faq(p),
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

@bot.command()
async def roll(ctx: Context) -> None:
    """
    Returns a number between 1/100
    """
    await ctx.send(
        f"{randint(1,100)}/100\n{ctx.author.mention}"
    )
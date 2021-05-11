from ext import glob
from ext.glob import bot
from discord.ext import commands
from discord.ext.commands import Context

@bot.command()
@commands.has_role("perms")
async def enable(ctx: Context) -> None:
    if ctx.guild.id != 705649421857325139:
        return
    glob.mode = True
    await ctx.message.add_reaction('👍')

@bot.command()
@commands.has_role("perms")
async def disable(ctx: Context) -> None:
    if ctx.guild.id != 705649421857325139:
        return
    glob.mode = False
    await ctx.message.add_reaction('👍')
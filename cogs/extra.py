from ext.glob import bot
from discord import Embed
from discord.ext.commands.context import Context

@bot.command(aliases=['h', 'faq', 'commands'])
async def help(ctx: Context) -> None:
    h = [
        '**Top**',
        ';t | ;top',
        "Shows a top play from a user's profile",
        'Args: name of player | -p (a whole number) | '
        '-std | -taiko | -ctb | -mania | -rx | -akatsuki',
        '',
        '**Recent**',
        ';r | ;rs | ;rc | ;recent',
        "Shows a recent score from a user's profile",
        'Args: name of player | -p (a whole number) | '
        '-std | -taiko | -ctb | -mania | -rx | -akatsuki',
        '',
        '**Profile**',
        ';p | ;osu | ;profile',
        "Shows a profile for a user.",
        'Args: name of player | -std | -taiko | '
        '-ctb | -mania | -rx | -akatsuki',
        '',
        '**Compare**',
        ';c | ;compare',
        "Compares a score from a recently posted beatmap.",
        'Args: name of player | -p (a whole number) | -std | -taiko | '
        '-ctb | -mania | -rx | -akatsuki',
        '',
        '**Connect**',
        ';connect',
        "Connects a profile to your discord account.",
        "Args: name of player | -akatsuki",
        '',
        '**Osucard**',
        ';osucard | ;oc | ;card',
        'Shows your overall stats of certain skill sets on an embed.',
        "**HUGE work in progress wouldn't suggest using for now**",
        "Args: player name | -std | -taiko | "
        "-ctb | -mania | -rx | -akatsuki"
    ]

    e = Embed(
        description = '\n'.join(h),
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
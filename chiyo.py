import discord
from discord.ext import commands
import os
import requests
import config
import pymongo
import akatsukiapi

global cache
# 0 = guild id | 1 = channel id | 2 = beatmap id | 3 = mode
# 4 = beatmap set id | 5 = songname | 6 = userid | 7 = difficulty
# 8 = ar | 9 = od | 10 = full combo | 11 = rx will be 1 no rx will be 0
cache = ['', '', '', '', '', '', '', '', '', '', '', '']

# pip3 install -r requirment.txt

# save the bot some time by connecting the database before starting
cluster = pymongo.MongoClient(
    f"mongodb+srv://{config.dbuser}:{config.dbpassword}@chiyo-y6grb.mongodb.net/{config.dbname}?retryWrites=true&w=majority")
db = cluster['Akatsuki']
collation = db['Akatsuki']

client = commands.Bot(command_prefix=config.prefix, case_insensitive=True)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.event
async def on_ready():
    print(
        f'Kimitzuni Today at 12:20 PM "UwUUUUUU Im online daddyyyy"\nChiyo is currently in {str(len(client.guilds))} servers!')
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing,
                                                                                         name=f'in {str(len(client.guilds))} Servers!'))
# @client.event
# async def on_command_error(ctx, error):
#	if isinstance(error, commands.CommandNotFound):
#		await ctx.message.channel.send('command not found!')


@client.event
async def on_message(message):
    await client.wait_until_ready()
    await client.process_commands(message)

    if message.content.startswith(';cb') == True:
        msg = message.content.replace(';cb', '')
        comepletemessage = len(msg)
        if message.mentions[0].id:
            b = collation.find_one({"_id": message.mentions[0].id})
            if b == None:
                await message.channel.send(f"User couldn't be found for {message.mentions[0]}!\n{message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
            method = 0
        elif comepletemessage == 0:
            b = collation.find_one({"_id": message.author.id})
            if b == None:
                await message.channel.send(f"User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
            method = 0
        else:
            c = msg
            method = 1

        if message.channel.id not in cache:
            await message.channel.send('Couldnt find map in this place!')

        beatmapid = cache[2].replace(' -taiko','')
        mode = cache[3]
        beatmapset_id = cache[4]
        songname = cache[5]
        difficulty = cache[7]
        rx = cache[11]
        ar = cache[8]
        od = cache[9]
        full_combo = cache[10]

        if method == 1:
        	info = akatsukiapi.compare(c[1:], beatmapid, mode)
        else:
        	info = akatsukiapi.compare(c, beatmapid, mode)
        
        if info == 'no user found':
            return await message.channel.send('No user found!')

        if info == 'no score found':
            return await message.channel.send('No score found for this user on this map!')

        if int(info['enabled_mods']) == 0:
            mods = 'NM'
        else:
            just_some_mods_lol = akatsukiapi.readableMods(
                int(info['enabled_mods']))
            if 'NC' in just_some_mods_lol:
                mods = just_some_mods_lol.replace('DT', '')
            else:
                mods = just_some_mods_lol

        userid = int(info['user_id'])
        rank = info['rank']
        pppp = info['pp']
        ppp = float(pppp)
        pp = round(ppp, 2)
        score = info['score']
        max_combo = info['maxcombo']
        count_300 = info['count300']
        count_100 = info['count100']
        count_50 = info['count50']
        count_miss = info['countmiss']
        username = info['username']
        if mode == 0:
            total = sum((int(count_300), int(count_100),
                         int(count_50), int(count_miss)))
            accc = 100.0 * sum((
                int(count_50) * 50.0,
                int(count_100) * 100.0,
                int(count_300) * 300.0
            )) / (total * 300.0)
        elif mode == 1:
            total = sum((int(count_300), int(count_100), int(count_miss)))
            accc = 100.0 * sum((
                int(count_100) * 150.0,
                int(count_300) * 300.0
            )) / (total * 300.0)

        acc = round(accc, 2)
        embed = discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR: {ar} OD: {od}] ▸ {acc}%\n▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{count_300}/{count_100}/{count_50}/{count_miss}]', color=0xb6ebf1)
        embed.set_author(name=f"{songname} +{mods} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmapid}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
        embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapset_id}l.jpg")
        embed.set_footer(text=f"Top Play for {username} on this map!")
        await message.channel.send(embed=embed)

    if 'https://akatsuki.pw/b/' in message.content and '-taiko' in message.content:
        c = message.content
        b = c.replace('https://akatsuki.pw/b/', '')
        d = b.replace('?mode=0', '')
        e = d.replace('?mode=1', '')
        f = e.replace('?mode=2', '')
        fyusagfa = f.replace('-taiko', '')
        g = f.replace('?mode=3', '')
        t = requests.get(
            f'https://akatsuki.pw/api/get_beatmaps?limit=1&b={g}&m=1')
        if not t:
            return
        title = t.json()[0]['title']
        id_b = t.json()[0]['beatmap_id']
        id_sb = t.json()[0]['beatmapset_id']
        artist = t.json()[0]['artist']
        max_combo = t.json()[0]['max_combo']
        bpm = t.json()[0]['bpm']
        difficulty = t.json()[0]['difficultyrating']

        cache[1] = message.channel.id
        cache[2] = g
        cache[3] = 1
        cache[4] = id_sb
        cache[5] = title
        cache[7] = round(float(difficulty), 2)
        cache[8] = t.json()[0]['diff_approach']
        cache[9] = t.json()[0]['diff_overall']
        cache[10] = max_combo
        cache[11] = 1

        embed = discord.Embed(
            description=f'▸ Bloodcat: https://bloodcat.com/osu/{id_b} \n▸ Old Osu: https://old.ppy.sh/s/{id_sb}\n▸ Osu: https://osu.ppy.sh/b/{id_b} \n▸ Gatari: https://osu.gatari.pw/b/{id_b} \n▸ Max Combo: {max_combo} \n▸ BPM: {bpm}', color=0xb6ebf1)
        embed.set_author(name=f"{artist} - {title}", url=f"https://akatsuki.pw/b/{id_b}",
                         icon_url=f"https://avatars0.githubusercontent.com/u/45724130?s=200&v=4.png")
        embed.set_image(
            url=f'https://assets.ppy.sh/beatmaps/{id_sb}/covers/cover.jpg')
        await message.channel.send(embed=embed)
    if 'https://akatsuki.pw/b/' in message.content and '-taiko' not in message.content:
        c = message.content
        b = c.replace('https://akatsuki.pw/b/', '')
        d = b.replace('?mode=0', '')
        e = d.replace('?mode=1', '')
        f = e.replace('?mode=2', '')
        fyusagfa = f.replace('-taiko', '')
        g = f.replace('?mode=3', '')
        t = requests.get(
            f'https://akatsuki.pw/api/get_beatmaps?limit=1&b={g}&m=0')
        if not t:
            return
        title = t.json()[0]['title']
        id_b = t.json()[0]['beatmap_id']
        id_sb = t.json()[0]['beatmapset_id']
        artist = t.json()[0]['artist']
        max_combo = t.json()[0]['max_combo']
        bpm = t.json()[0]['bpm']

        difficulty = t.json()[0]['difficultyrating']

        cache[1] = message.channel.id
        cache[2] = g
        cache[3] = 0
        cache[4] = id_sb
        cache[5] = title
        cache[7] = round(float(difficulty), 2)
        cache[8] = t.json()[0]['diff_approach']
        cache[9] = t.json()[0]['diff_overall']
        cache[10] = max_combo
        cache[11] = 1

        embed = discord.Embed(
            description=f'▸ Bloodcat: https://bloodcat.com/osu/{id_b} \n▸ Old Osu: https://old.ppy.sh/s/{id_sb}\n▸ Osu: https://osu.ppy.sh/b/{id_b} \n▸ Gatari: https://osu.gatari.pw/b/{id_b} \n▸ Max Combo: {max_combo} \n▸ BPM: {bpm}', color=0xb6ebf1)
        embed.set_author(name=f"{artist} - {title}", url=f"https://akatsuki.pw/b/{id_b}",
                         icon_url=f"https://avatars0.githubusercontent.com/u/45724130?s=200&v=4.png")
        embed.set_image(
            url=f'https://assets.ppy.sh/beatmaps/{id_sb}/covers/cover.jpg')
        await message.channel.send(embed=embed)
    if 'https://akatsuki.pw/d/' in message.content and '-taiko' not in message.content:
        c = message.content
        b = c.replace('https://akatsuki.pw/d/', '')
        d = b.replace('?mode=0', '')
        e = d.replace('?mode=1', '')
        f = e.replace('?mode=2', '')
        g = f.replace('?mode=3', '')
        t = requests.get(
            f'https://akatsuki.pw/api/get_beatmaps?limit=1&s={g}&m=0')
        if not t:
            return
        title = t.json()[0]['title']
        id_b = t.json()[0]['beatmap_id']
        id_sb = t.json()[0]['beatmapset_id']
        artist = t.json()[0]['artist']
        max_combo = t.json()[0]['max_combo']
        bpm = t.json()[0]['bpm']

        difficulty = t.json()[0]['difficultyrating']

        cache[1] = message.channel.id
        cache[2] = g
        cache[3] = 0
        cache[4] = id_sb
        cache[5] = title
        cache[7] = round(float(difficulty), 2)
        cache[8] = t.json()[0]['diff_approach']
        cache[9] = t.json()[0]['diff_overall']
        cache[10] = max_combo
        cache[11] = 1

        embed = discord.Embed(
            description=f'▸ Bloodcat: https://bloodcat.com/osu/{id_b} \n▸ Old Osu: https://old.ppy.sh/s/{id_sb}\n▸ Osu: https://osu.ppy.sh/b/{id_b} \n▸ Gatari: https://osu.gatari.pw/b/{id_b} \n▸ Max Combo: {max_combo} \n▸ BPM: {bpm}', color=0xb6ebf1)
        embed.set_author(name=f"{artist} - {title}", url=f"https://akatsuki.pw/b/{id_b}",
                         icon_url=f"https://avatars0.githubusercontent.com/u/45724130?s=200&v=4.png")
        embed.set_image(
            url=f'https://assets.ppy.sh/beatmaps/{id_sb}/covers/cover.jpg')
        await message.channel.send(embed=embed)
    if 'https://akatsuki.pw/d/' in message.content and '-taiko' in message.content:
        c = message.content
        b = c.replace('https://akatsuki.pw/d/', '')
        d = b.replace('?mode=0', '')
        e = d.replace('?mode=1', '')
        f = e.replace('?mode=2', '')
        ysfusf = f.replace('-taiko', '')
        g = ysfusf.replace('?mode=3', '')
        t = requests.get(
            f'https://akatsuki.pw/api/get_beatmaps?limit=1&s={g}&m=1')
        if not t:
            return
        title = t.json()[0]['title']
        id_b = t.json()[0]['beatmap_id']
        id_sb = t.json()[0]['beatmapset_id']
        artist = t.json()[0]['artist']
        max_combo = t.json()[0]['max_combo']
        bpm = t.json()[0]['bpm']

        difficulty = t.json()[0]['difficultyrating']

        cache[1] = message.channel.id
        cache[2] = g
        cache[3] = 1
        cache[4] = id_sb
        cache[5] = title
        cache[7] = round(float(difficulty), 2)
        cache[8] = t.json()[0]['diff_approach']
        cache[9] = t.json()[0]['diff_overall']
        cache[10] = max_combo
        cache[11] = 1

        embed = discord.Embed(
            description=f'▸ Bloodcat: https://bloodcat.com/osu/{id_b} \n▸ Old Osu: https://old.ppy.sh/s/{id_sb}\n▸ Osu: https://osu.ppy.sh/b/{id_b} \n▸ Gatari: https://osu.gatari.pw/b/{id_b} \n▸ Max Combo: {max_combo} \n▸ BPM: {bpm}', color=0xb6ebf1)
        embed.set_author(name=f"{artist} - {title}", url=f"https://akatsuki.pw/b/{id_b}",
                         icon_url=f"https://avatars0.githubusercontent.com/u/45724130?s=200&v=4.png")
        embed.set_image(
            url=f'https://assets.ppy.sh/beatmaps/{id_sb}/covers/cover.jpg')
        await message.channel.send(embed=embed)

client.run(config.token)

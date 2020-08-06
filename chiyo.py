import discord
from discord.ext import commands
import os
import requests
import config
import pymongo
import akatsukiapi

#save the bot some time by connecting the database before starting
cluster = pymongo.MongoClient(f"mongodb+srv://{config.dbuser}:{config.dbpassword}@{config.dbname}-y6grb.mongodb.net/{config.dbname}?retryWrites=true&w=majority")
db = cluster['Akatsuki']
collation = db['Akatsuki']

client = commands.Bot(command_prefix=config.prefix, case_insensitive=True)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_ready():
    print(f'Chiyo V3 soon\nChiyo is currently in {str(len(client.guilds))} servers!')
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing,
                                                                               name=config.game))
@client.event
async def on_message(message):
	await client.wait_until_ready()  
	await client.process_commands(message)

	if 'https://akatsuki.pw/b/' in message.content and '-taiko' in message.content:
		c = message.content
		b = c.replace('https://akatsuki.pw/b/','')
		d = b.replace('?mode=0','')
		e = d.replace('?mode=1','')
		f = e.replace('?mode=2','')
		fyusagfa = f.replace('-taiko','')
		g = f.replace('?mode=3','')
		t = requests.get(f'https://akatsuki.pw/api/get_beatmaps?limit=1&b={g}&m=1')
		if not t:
			return
		title = t.json()[0]['title']
		id_b = t.json()[0]['beatmap_id']
		id_sb = t.json()[0]['beatmapset_id']
		artist = t.json()[0]['artist']
		max_combo = t.json()[0]['max_combo']
		bpm = t.json()[0]['bpm']
		embed=discord.Embed(description=f'▸ Bloodcat: https://bloodcat.com/osu/{id_b} \n▸ Old Osu: https://old.ppy.sh/s/{id_sb}\n▸ Osu: https://osu.ppy.sh/b/{id_b} \n▸ Max Combo: {max_combo} \n▸ BPM: {bpm}', color=0xb6ebf1)
		embed.set_author(name=f"{artist} - {title}", url=f"https://akatsuki.pw/b/{id_b}", icon_url=f"https://avatars0.githubusercontent.com/u/45724130?s=200&v=4.png")
		embed.set_image(url=f'https://assets.ppy.sh/beatmaps/{id_sb}/covers/cover.jpg')
		await message.channel.send(embed=embed)
	elif 'https://akatsuki.pw/b/' in message.content:
		c = message.content
		b = c.replace('https://akatsuki.pw/b/','')
		d = b.replace('?mode=0','')
		e = d.replace('?mode=1','')
		f = e.replace('?mode=2','')
		g = f.replace('?mode=3','')
		t = requests.get(f'https://akatsuki.pw/api/get_beatmaps?limit=1&b={g}')
		if not t:
			return
		title = t.json()[0]['title']
		id_b = t.json()[0]['beatmap_id']
		id_sb = t.json()[0]['beatmapset_id']
		artist = t.json()[0]['artist']
		max_combo = t.json()[0]['max_combo']
		bpm = t.json()[0]['bpm']
		embed=discord.Embed(description=f'▸ Bloodcat: https://bloodcat.com/osu/{id_b} \n▸ Old Osu: https://old.ppy.sh/s/{id_sb}\n▸ Osu: https://osu.ppy.sh/b/{id_b} \n▸ Max Combo: {max_combo} \n▸ BPM: {bpm}', color=0xb6ebf1)
		embed.set_author(name=f"{artist} - {title}", url=f"https://akatsuki.pw/b/{id_b}", icon_url=f"https://avatars0.githubusercontent.com/u/45724130?s=200&v=4.png")
		embed.set_image(url=f'https://assets.ppy.sh/beatmaps/{id_sb}/covers/cover.jpg')
		await message.channel.send(embed=embed)

client.run(config.token)

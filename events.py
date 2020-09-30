import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from tinydb import TinyDB, Query
import config
from datetime import datetime
import requests
import osuhelper
import random
import re

beatmap = r'\b\d+\b'

class Chiyo:

	def __init__(self, token):
		self.token = token

	def Nyoko(self):

		cache = {}
		man = {0: 'std', 1: 'taiko', 2: 'ctb', 3: 'mania'}
		switcher = {0: 'Standard', 1: 'Taiko', 2: 'Catch The Beat', 3: 'Mania'}
		another_switcher = {0: '', 1: ' Relax'}
		db = TinyDB('db.json')
		User = Query()
		print('Connected to database!')

		def get_prefix(client, message):

			how = db.get(User.guild_id == message.guild.id)

			if how == None:
				return config.prefix
			else:
				return how['prefix']

		Chiyo = commands.Bot(command_prefix = get_prefix, case_insensitive=True, help_command=None)

		@Chiyo.event
		async def on_ready():
			amount_of_servers = str(len(Chiyo.guilds))
			print('Chiyo is on and running in {} servers!'.format(amount_of_servers))
			await Chiyo.change_presence(
				status=discord.Status.online, 
				activity=discord.Activity(
				type=discord.ActivityType.playing, 
				name=f"in {amount_of_servers} Servers!"))
		
		@Chiyo.event
		async def on_message(message):
			await Chiyo.wait_until_ready()  
			await Chiyo.process_commands(message)
			print(f"[{datetime.now().time()}] [{message.guild}] [{message.channel}] {message.author}: {message.content}")
			
			if message.content == f'<@!{Chiyo.user.id}>':
				await message.channel.send(f'The prefix for this server is `{get_prefix(Chiyo, message)}`')

			if 'https://akatsuki.pw/' in message.content and message.author.id != Chiyo.user.id:
				color = message.author.roles[len(message.author.roles) - 1].color

				for mapid in re.findall(beatmap, message.content):
					mode = 0
					if '-taiko' in message.content:
						mode = 1
					elif '-std' in message.content:
						mode = 0
					if '/b/' in message.content:
						how = 'b'
					elif '/d/' in message.content:
						how = 's'
					params = {
						'limit': 1,
						f'{how}': int(mapid),
						'm': mode
					}
					t = requests.get(f'https://akatsuki.pw/api/get_beatmaps?', params=params)
					
					if not t:
						continue
					
					dude = t.json()[0]

					title = dude['title']
					id_b = dude['beatmap_id']
					id_sb = dude['beatmapset_id']
					artist = dude['artist']
					max_combo = dude['max_combo']
					bpm = dude['bpm']
					difficulty = round(float(dude['difficultyrating']), 2)

					cache[message.channel.id] = dude

					embed = discord.Embed(
					description=f'▸ Bloodcat: https://bloodcat.com/osu/{id_b}\n'\
					f'▸ Old Osu: https://old.ppy.sh/s/{id_sb}\n'\
					f'▸ Osu: https://osu.ppy.sh/b/{id_b}\n'\
					f'▸ Gatari: https://osu.gatari.pw/b/{id_b}\n' \
					f'▸ Max Combo: {max_combo}\n' \
					f'▸ BPM: {bpm}', 
					color=color)
					embed.set_author(
					name=f"{artist} - {title}", url=f"https://akatsuki.pw/b/{id_b}",
					icon_url=config.server_icon_url)
					embed.set_image(
					url=f'https://assets.ppy.sh/beatmaps/{id_sb}/covers/cover.jpg'
					)
					await message.channel.send(embed=embed)

		@Chiyo.command(aliases=['prefix'])
		@has_permissions(administrator=True)
		async def custom_prefix(ctx, *args):

			if len(args) == 0:
				return await ctx.send("Must provide a prefix!")

			owo = db.search(User.guild_id == ctx.guild.id)

			something = ''.join(args)

			if str(owo) == '[]':
				db.insert({'guild_id': ctx.guild.id, 'prefix': something})
			else:
				db.update({'prefix': something}, User.guild_id == ctx.guild.id)

			return await ctx.send(f'Prefix was changed! The new prefix is: {something}')

		@Chiyo.command(aliases=['compare', 'c'])
		async def _compare(ctx, *args):
			color = ctx.message.author.roles[len(ctx.message.author.roles) - 1].color
			try:	
				relax, mode, scoreid = 0, int(cache[ctx.message.channel.id]['mode']), 0
			except:
				return await ctx.send("Couldn't find a map in this channel!")
			msg = ctx.message.content.split(' ')[1:]

			if '-rx' in msg:
				msg.remove('-rx')
				relax = 1
			if '-p' in msg:
				scoreid = int(msg[msg.index('-p') + 1])
				msg.remove(msg[msg.index('-p') + 1])
				msg.remove('-p')
			if '-std' in msg:
				msg.remove('-std')
				mode = 0
			elif '-taiko' in msg:
				msg.remove('-taiko')
				mode = 1
			elif '-ctb' in msg:
				msg.remove('-ctb')
				mode = 2
			elif '-mania' in msg:
				msg.remove('-mania')
				mode, relax = 3, 0

			hahaha = another_switcher.get(relax)
			text = switcher.get(mode)

			if ctx.message.mentions:
				e = db.get(User.id == ctx.message.mentions[0].id)
				if e == None:
					return await ctx.send(f"User couldn't be found in our database! Try connecting a user to our database by doing `{get_prefix(Chiyo, ctx.message)}connect user`")
				userid = e['akatsuki']
			elif len(msg) == 0:
				e = db.get(User.id == ctx.message.author.id)
				if e == None:
					return await ctx.send(f"User couldn't be found in our database! Try connecting a user to our database by doing `{get_prefix(Chiyo, ctx.message)}connect user`")
				userid = e['akatsuki']
			else:
				if osuhelper.get_id(' '.join(msg)) == "Couldn't find user!":
					return await ctx.send("Couldn't find this user!")
				userid = osuhelper.get_id(' '.join(msg))

			info = osuhelper.Helper(userid)
			if ctx.message.channel.id not in cache:
				return await ctx.send("Couldn't find a map here")
			
			stats = info.compare(beatmapid=cache[ctx.message.channel.id]['beatmap_id'], mode=mode, relax=relax, scoreid=scoreid)
			
			if stats == 'no score found':
				return await ctx.send("Couldn't find a score for this user!")

			rank = config.letters.get(stats['rank'])
			pp = round(float(stats['pp']), 2)
			ar = cache[ctx.message.channel.id]['diff_approach']
			od = cache[ctx.message.channel.id]['diff_overall']
			score = stats['score']
			max_combo = stats['maxcombo']
			full_combo = cache[ctx.message.channel.id]['max_combo']
			count_300 = stats['count300']
			count_100 = stats['count100']
			count_50 = stats['count50']
			count_miss = stats['countmiss']
			songname = cache[ctx.message.channel.id]['title']
			mods = 'NM' if int(stats['enabled_mods']) == 0 else osuhelper.readableMods(int(stats['enabled_mods']))
			difficulty = round(float(cache[ctx.message.channel.id]['difficultyrating']), 2)
			beatmap_id = cache[ctx.message.channel.id]['beatmap_id']
			beatmapset_id = cache[ctx.message.channel.id]['beatmapset_id']
			if mode == 0:
				total = sum((int(count_300), int(count_100), int(count_50), int(count_miss)))
				d = 100.0 * sum((
						int(count_50) * 50.0,
						int(count_100) * 100.0,
						int(count_300) * 300.0
					)) / (total * 300.0)
				accuracy = round(d, 2)
			elif mode == 1:
				total = sum((int(count_300), int(count_100), int(count_miss)))
				d = 100.0 * sum((
				int(count_100) * 150.0,
				int(count_300) * 300.0
			   )) / (total * 300.0)
				accuracy = round(d, 2)
			else:
				accuracy = '0'

			username = osuhelper.get_username(userid)

			embed=discord.Embed(description=f'▸ {pp}PP [AR: {ar} OD: {od}] ▸ {accuracy}%\n▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{count_300}/{count_100}/{count_50}/{count_miss}]', color=color)
			embed.set_author(name=f"{songname} +{mods} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmap_id}", icon_url=rank)
			embed.set_thumbnail(url=f"https://a.akatsuki.pw/{userid}.png")
			embed.set_image(url=f"https://assets.ppy.sh/beatmaps/{beatmapset_id}/covers/cover.jpg")
			embed.set_footer(text=f"osu!{hahaha} {text} Plays for {username} ")
			await ctx.send(embed=embed)

		@Chiyo.command(aliases=['top','t','osutop'])
		async def _top(ctx, *args):
			color = ctx.message.author.roles[len(ctx.message.author.roles) - 1].color

			relax, mode, scoreid = 0, 0, 0
			msg = ctx.message.content.split(' ')[1:]

			if '-rx' in msg:
				msg.remove('-rx')
				relax = 1
			if '-p' in msg:
				scoreid = int(msg[msg.index('-p') + 1])
				msg.remove(msg[msg.index('-p') + 1])
				msg.remove('-p')
			if '-std' in msg:
				msg.remove('-std')
				mode = 0
			elif '-taiko' in msg:
				msg.remove('-taiko')
				mode = 1
			elif '-ctb' in msg:
				msg.remove('-ctb')
				mode = 2
			elif '-mania' in msg:
				msg.remove('-mania')
				mode, relax = 3, 0

			hahaha = another_switcher.get(relax)
			text = switcher.get(mode)

			if ctx.message.mentions:
				e = db.get(User.id == ctx.message.mentions[0].id)
				if e == None:
					return await ctx.send(f"User couldn't be found in our database! Try connecting a user to our database by doing `{get_prefix()}connect user`")
				userid = e['akatsuki']
			elif len(msg) == 0:
				e = db.get(User.id == ctx.message.author.id)
				if e == None:
					return await ctx.send(f"User couldn't be found in our database! Try connecting a user to our database by doing `{get_prefix(Chiyo, ctx.message)}connect user`")
				userid = e['akatsuki']
			else:
				c = osuhelper.get_id(' '.join(msg))
				if c == "Couldn't find user!":
					return await ctx.send("Couldn't find this user!")
				userid = c

			info = osuhelper.Helper(userid)
			stats = info.top(mode=mode, relax=relax, scoreid=scoreid)
			if stats == 'error':
				return await ctx.send("Error has occured!")
			
			rank = config.letters.get(stats['rank'])
			pp = round(stats['pp'], 2)
			ar = stats['beatmap']['ar']
			od = stats['beatmap']['od']
			accuracy = round(stats['accuracy'], 2)
			score = stats['score']
			max_combo = stats['max_combo']
			full_combo = stats['beatmap']['max_combo']
			count_300 = stats['count_300']
			count_100 = stats['count_100']
			count_50 = stats['count_50']
			count_miss = stats['count_miss']
			completed = 'Yes' if stats['completed'] == 3 or stats['completed'] == 2 else 'No'
			songname = stats['beatmap']['song_name']
			mods = 'NM' if stats['mods'] == 0 else osuhelper.readableMods(stats['mods'])
			difficulty = round(stats['beatmap']['difficulty2'][man.get(mode)], 2)
			beatmap_id = stats['beatmap']['beatmap_id']
			beatmapset_id = stats['beatmap']['beatmapset_id']
			username = osuhelper.get_username(userid)

			cache[ctx.message.channel.id] = osuhelper.get_beatmap(beatmap_id, mode)
			
			embed=discord.Embed(description=f'▸ {pp}PP [AR: {ar} OD: {od}] ▸ {accuracy}%\n▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{count_300}/{count_100}/{count_50}/{count_miss}]\n▸ Map Completed: {completed}', color=color)
			embed.set_author(name=f"{songname} +{mods} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmap_id}", icon_url=rank)
			embed.set_thumbnail(url=f"https://a.akatsuki.pw/{userid}.png")
			embed.set_image(url=f"https://assets.ppy.sh/beatmaps/{beatmapset_id}/covers/cover.jpg")
			embed.set_footer(text=f"Top osu!{hahaha} {text} Play for {username} ")
			await ctx.send(embed=embed)

		@Chiyo.command(aliases=['recent','rs','rc','r'])
		async def _recent(ctx, *args):
			color = ctx.message.author.roles[len(ctx.message.author.roles) - 1].color

			relax, mode, scoreid = 0, 0, 0
			msg = ctx.message.content.split(' ')[1:]

			if '-rx' in msg:
				msg.remove('-rx')
				relax = 1
			if '-p' in msg:
				scoreid = int(msg[msg.index('-p') + 1])
				msg.remove(msg[msg.index('-p') + 1])
				msg.remove('-p')
			if '-std' in msg:
				msg.remove('-std')
				mode = 0
			elif '-taiko' in msg:
				msg.remove('-taiko')
				mode = 1
			elif '-ctb' in msg:
				msg.remove('-ctb')
				mode = 2
			elif '-mania' in msg:
				msg.remove('-mania')
				mode, relax = 3, 0

			hahaha = another_switcher.get(relax)
			text = switcher.get(mode)

			if ctx.message.mentions:
				e = db.get(User.id == ctx.message.mentions[0].id)
				if e == None:
					return await ctx.send(f"User couldn't be found in our database! Try connecting a user to our database by doing `{get_prefix(Chiyo, ctx.message)}connect user`")
				userid = e['akatsuki']
			elif len(msg) == 0:
				e = db.get(User.id == ctx.message.author.id)
				if e == None:
					return await ctx.send(f"User couldn't be found in our database! Try connecting a user to our database by doing `{get_prefix(Chiyo, ctx.message)}connect user`")
				userid = e['akatsuki']
			else:
				e = osuhelper.get_id(' '.join(msg))
				if e == "Couldn't find user!":
					return await ctx.send("Couldn't find this user!")
				userid = e

			info = osuhelper.Helper(userid)
			stats = info.recent(mode=mode, relax=relax, scoreid=scoreid)
			if stats == 'error':
				return await ctx.send("Error has occured!")

			rank = config.letters.get(stats['rank'])
			pp = round(stats['pp'], 2)
			ar = stats['beatmap']['ar']
			od = stats['beatmap']['od']
			accuracy = round(stats['accuracy'], 2)
			score = stats['score']
			max_combo = stats['max_combo']
			full_combo = stats['beatmap']['max_combo']
			count_300 = stats['count_300']
			count_100 = stats['count_100']
			count_50 = stats['count_50']
			count_miss = stats['count_miss']
			completed = 'Yes' if stats['completed'] == 3 or stats['completed'] == 2 else 'No'
			songname = stats['beatmap']['song_name']
			mods = 'NM' if stats['mods'] == 0 else osuhelper.readableMods(stats['mods'])
			difficulty = round(stats['beatmap']['difficulty2'][man.get(mode)], 2)
			beatmap_id = stats['beatmap']['beatmap_id']
			beatmapset_id = stats['beatmap']['beatmapset_id']
			username = osuhelper.get_username(userid)

			cache[ctx.message.channel.id] = osuhelper.get_beatmap(beatmap_id, mode)

			embed=discord.Embed(description=f'▸ {pp}PP [AR: {ar} OD: {od}] ▸ {accuracy}%\n▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{count_300}/{count_100}/{count_50}/{count_miss}]\n▸ Map Completed: {completed}', color=color)
			embed.set_author(name=f"{songname} +{mods} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmap_id}", icon_url=rank)
			embed.set_thumbnail(url=f"https://a.akatsuki.pw/{userid}.png")
			embed.set_image(url=f"https://assets.ppy.sh/beatmaps/{beatmapset_id}/covers/cover.jpg")
			embed.set_footer(text=f"Most Recent osu!{hahaha} {text} Play for {username} ")
			await ctx.send(embed=embed)
		
		@Chiyo.command(aliases=['osu', 'p', 'profile'])
		async def _profile(ctx, *args):
			color = ctx.message.author.roles[len(ctx.message.author.roles) - 1].color

			relax, mode = 0, 0
			msg = ctx.message.content.split(' ')[1:]

			if '-rx' in msg:
				msg.remove('-rx')
				relax = 1
			if '-std' in msg:
				msg.remove('-std')
				mode = 0
			elif '-taiko' in msg:
				msg.remove('-taiko')
				mode = 1
			elif '-ctb' in msg:
				msg.remove('-ctb')
				mode = 2
			elif '-mania' in msg:
				msg.remove('-mania')
				mode, relax = 3, 0

			hahaha = another_switcher.get(relax)
			text = switcher.get(mode)

			if ctx.message.mentions:
				e = db.get(User.id == ctx.message.mentions[0].id)
				if e == None:
					return await ctx.send(f"User couldn't be found in our database! Try connecting a user to our database by doing `{get_prefix(Chiyo, ctx.message)}connect user`")
				userid = e['akatsuki']
			elif len(msg) == 0:
				e = db.get(User.id == ctx.message.author.id)
				if e == None:
					return await ctx.send(f"User couldn't be found in our database! Try connecting a user to our database by doing `{get_prefix(Chiyo, ctx.message)}connect user`")
				userid = e['akatsuki']
			else:
				if osuhelper.get_id(' '.join(msg)) == "Couldn't find user!":
					return await ctx.send("Couldn't find this user!")
				userid = osuhelper.get_id(' '.join(msg))

			e = osuhelper.Helper(userid)
			
			b = e.profile(mode=mode, relax=relax)
			if b == 'error':
				return await ctx.send("Error has occured!")
			official_rank = b['stats']['global_leaderboard_rank']
			country = b['country']
			country_rank = b['stats']['country_leaderboard_rank']
			level = round(b['stats']['level'], 2)
			pp = b['stats']['pp']
			accuracy = round(b['stats']['accuracy'], 2)
			playcount = b['stats']['playcount']
			username = b['username']
			embed=discord.Embed(description=f'▸ Official Rank: {official_rank} ({country}#{country_rank}) \n▸ Level: {level}\n▸ Total PP: {pp} \n▸ Accuracy: {accuracy}% \n▸ Playcount: {playcount}', color=color)
			embed.set_author(name=f"osu!{hahaha} {text} Profile for {username} ", url=f"https://akatsuki.pw/u/{userid}", icon_url=config.server_icon_url)
			embed.set_thumbnail(url=f"https://a.akatsuki.pw/{userid}.png")
			embed.set_footer(text=f"Player on Akatsuki!")
			return await ctx.send(embed=embed)

		@Chiyo.command()
		async def connect(ctx, *args):
			color = ctx.message.author.roles[len(ctx.message.author.roles) - 1].color

			if len(args) == 0:
				return await ctx.send('Must provide a username!')

			msg = '{}'.format(' '.join(args))

			if osuhelper.get_id(msg) == "Couldn't find user!":
				return await ctx.send("Couldn't find this user!")
			userid = osuhelper.get_id(msg)

			owo = db.search(User.id == ctx.message.author.id)
			
			if str(owo) == '[]':
				db.insert({'id': ctx.message.author.id, 'akatsuki': userid})
			else:
				db.update({'akatsuki': userid}, User.id == ctx.message.author.id)

			embed=discord.Embed(colour = color)
			embed.set_author(name=f"User {msg} was connected to your discord account!", url=f"https://akatsuki.pw/u/{userid}")
			embed.set_image(url="https://a.akatsuki.pw/{}.png".format(userid))
			return await ctx.send(embed=embed)

		@Chiyo.command(aliases=['help','faq'])
		async def _faq(ctx, *args):
			color = ctx.message.author.roles[len(ctx.message.author.roles) - 1].color
			embed=discord.Embed(colour = color)
			embed.set_author(name="Chiyo | osu!Akatsuki discord bot!", url="https://coverosu.tk/chiyo", icon_url=config.bot_icon_url)
			embed.add_field(name="Commands!", value="""
			```
			Optional = () Required = []
			{hi}connect [username]
			{hi}slots
			{hi}roll
			{hi}[recent | rc | rs | r] [top | t] [osu | p | profile]
			(-p (number)) (@someone | username) (-taiko | -mania | -ctb | by default it is Standard) (-rx)
			```
			""".format(hi=get_prefix(Chiyo, ctx.message)), inline=False)
			embed.set_footer(text=f"Made by Cover#8860 dm if there is any problems")
			return await ctx.send(embed=embed)

		@Chiyo.command()
		async def about(ctx, *args):
			await ctx.send('https://coverosu.tk/chiyo')

		@Chiyo.command()
		async def roll(ctx, *args):
			number = random.randint(1, 100)
			await ctx.send(f'{number} out of 100 <@!{ctx.message.author.id}>')

		@Chiyo.command()
		async def slots(ctx, *args):

			h = ['🍎','🍊','🍐','🍋','🍉','🍇','🍓','🍒']

			b = random.choice(h)
			c = random.choice(h)
			d = random.choice(h)

			if b == c == d:
				return await ctx.send(f'[{b}{c}{d}] \n 3/3! <@!{ctx.message.author.id}>')
			elif b == c or b == d or c == b or c == d or d == b or d == c:
				return await ctx.send(f'[{b}{c}{d}] \n 2/3! <@!{ctx.message.author.id}>')
			else:
				return await ctx.send(f'[{b}{c}{d}] \n lol you suck <@!{ctx.message.author.id}>')	
			
		Chiyo.run(self.token)

	def run(self):
		self.Nyoko()

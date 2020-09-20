import discord
from discord.ext import commands
import sys
from tinydb import TinyDB, Query
from config import ownerid, apikey
from datetime import datetime
import requests
import osuhelper

class Chiyo:

	def __init__(self, token, client):
		super().__init__()
		self.token = token
		self.client = client
		global Chiyo # don't do this find another way im just retarded to use this
		Chiyo = self.client

	def Nyoko(self):

		cache = {}
		db = TinyDB('db.json')
		User = Query()
		print('Connected to database!')

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
			print(f"[{datetime.now().time()}] [{message.channel}] {message.author}: {message.content}")
			# this was old code that worked I could make it cleaner but im so lazy lol
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
				difficulty = round(float(t.json()[0]['difficultyrating']), 2)

				cache[message.guild.id] = {message.channel.id: {'beatmap_id': id_b, 'ar': t.json()[0]['diff_approach'], 'od': t.json()[0]['diff_overall'], 'full_combo': max_combo, 'songname': '{title} [{bruh}]'.format(title=title, bruh=t.json()[0]['version']) , 'difficulty': difficulty, 'beatmapset_id': id_sb}}

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

				difficulty = round(float(t.json()[0]['difficultyrating']), 2)

				cache[message.guild.id] = {message.channel.id: {'beatmap_id': id_b, 'ar': t.json()[0]['diff_approach'], 'od': t.json()[0]['diff_overall'], 'full_combo': max_combo, 'songname': '{title} [{bruh}]'.format(title=title, bruh=t.json()[0]['version']) , 'difficulty': difficulty, 'beatmapset_id': id_sb}}

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

				difficulty = round(float(t.json()[0]['difficultyrating']), 2)

				cache[message.guild.id] = {message.channel.id: {'beatmap_id': id_b, 'ar': t.json()[0]['diff_approach'], 'od': t.json()[0]['diff_overall'], 'full_combo': max_combo, 'songname': '{title} [{bruh}]'.format(title=title, bruh=t.json()[0]['version']) , 'difficulty': difficulty, 'beatmapset_id': id_sb}}

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

				difficulty = round(float(t.json()[0]['difficultyrating']), 2)

				cache[message.guild.id] = {message.channel.id: {'beatmap_id': id_b, 'ar': t.json()[0]['diff_approach'], 'od': t.json()[0]['diff_overall'], 'full_combo': max_combo, 'songname': '{title} [{bruh}]'.format(title=title, bruh=t.json()[0]['version']) , 'difficulty': difficulty, 'beatmapset_id': id_sb}}

				embed = discord.Embed(
					description=f'▸ Bloodcat: https://bloodcat.com/osu/{id_b} \n▸ Old Osu: https://old.ppy.sh/s/{id_sb}\n▸ Osu: https://osu.ppy.sh/b/{id_b} \n▸ Gatari: https://osu.gatari.pw/b/{id_b} \n▸ Max Combo: {max_combo} \n▸ BPM: {bpm}', color=0xb6ebf1)
				embed.set_author(name=f"{artist} - {title}", url=f"https://akatsuki.pw/b/{id_b}",
								 icon_url=f"https://avatars0.githubusercontent.com/u/45724130?s=200&v=4.png")
				embed.set_image(
					url=f'https://assets.ppy.sh/beatmaps/{id_sb}/covers/cover.jpg')
				await message.channel.send(embed=embed)		

		@Chiyo.command(aliases=['compare', 'c'])
		async def _compare(ctx, *args):
			relax, mode, scoreid = 0, 0, 0
			msg = ctx.message.content.split(' ')[1:]

			if '-rx' in msg:
				msg.remove('-rx')
				relax = 1
			if '-p' in msg:
				scoreid = int(msg[msg.index('-p') + 1])
				msg.remove(msg[msg.index('-p') + 1])
				msg.remove('-p')
			if '-taiko' in msg:
				msg.remove('-taiko')
				mode = 1
			if '-ctb' in msg:
				msg.remove('-ctb')
				mode = 2
			if '-mania' in msg:
				msg.remove('-mania')
				mode, relax = 3, 0

			switcher = {
				0: 'Standard',
				1: 'Taiko',
				2: 'Catch The Beat',
				3: 'Mania'
			}

			another_switcher = {
				0: '',
				1: ' Relax'
			}
			hahaha = another_switcher.get(relax)
			text = switcher.get(mode)

			if ctx.message.mentions:
				e = db.get(User.id == ctx.message.mentions[0].id)
				if e == None:
					return await ctx.send("User couldn't be found in our database! Try connecting a user to our database by doing `;connect user`")
				userid = e['akatsuki']
			elif len(msg) == 0:
				e = db.get(User.id == ctx.message.author.id)
				if e == None:
					return await ctx.send("User couldn't be found in our database! Try connecting a user to our database by doing `;connect user`")
				userid = e['akatsuki']
			else:
				if osuhelper.get_id(' '.join(msg)) == "Couldn't find user!":
					return await ctx.send("Couldn't find this user!")
				userid = osuhelper.get_id(' '.join(msg))

			info = osuhelper.Helper(userid)
			if ctx.guild.id not in cache and not ctx.message.channel.id in cache:
				return await ctx.send("Couldn't find a map here")
			
			stats = info.compare(beatmapid=cache[ctx.guild.id][ctx.message.channel.id]['beatmap_id'], mode=mode, relax=relax, scoreid=scoreid)
			
			if stats == 'no score found':
				return await ctx.send("Couldn't find a score for this user!")
			
			letters = {
				'SSH': 'https://cdn.discordapp.com/emojis/724849277406281728.png?v=1',
				'SH': 'https://cdn.discordapp.com/emojis/724847645142810624.png?v=1',
				'SS': 'https://cdn.discordapp.com/emojis/724849299300548680.png?v=1',
				'S': 'https://cdn.discordapp.com/emojis/724847668953874493.png?v=1',
				'A': 'https://cdn.discordapp.com/emojis/724841194517037137.png?v=1',
				'B': 'https://cdn.discordapp.com/emojis/724841229602521109.png?v=1',
				'C': 'https://cdn.discordapp.com/emojis/724841244530049095.png?v=1',
				'D': 'https://cdn.discordapp.com/emojis/724841263727116379.png?v=1'
			}
			man = {
				0: 'std',
				1: 'taiko',
				2: 'ctb',
				3: 'mania'
			}

			rank = letters.get(stats['rank'])
			pp = round(float(stats['pp']), 2)
			ar = cache[ctx.guild.id][ctx.message.channel.id]['ar']
			od = cache[ctx.guild.id][ctx.message.channel.id]['od']
			score = stats['score']
			max_combo = stats['maxcombo']
			full_combo = cache[ctx.guild.id][ctx.message.channel.id]['full_combo']
			count_300 = stats['count300']
			count_100 = stats['count100']
			count_50 = stats['count50']
			count_miss = stats['countmiss']
			songname = cache[ctx.guild.id][ctx.message.channel.id]['songname']
			mods = 'NM' if int(stats['enabled_mods']) == 0 else osuhelper.readableMods(int(stats['enabled_mods']))
			difficulty = cache[ctx.guild.id][ctx.message.channel.id]['difficulty']
			beatmap_id = cache[ctx.guild.id][ctx.message.channel.id]['beatmap_id']
			beatmapset_id = cache[ctx.guild.id][ctx.message.channel.id]['beatmapset_id']
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

			embed=discord.Embed(description=f'▸ {pp}PP [AR: {ar} OD: {od}] ▸ {accuracy}%\n▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{count_300}/{count_100}/{count_50}/{count_miss}]', color=0xb6ebf1)
			embed.set_author(name=f"{songname} +{mods} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmap_id}", icon_url=rank)
			embed.set_thumbnail(url=f"https://a.akatsuki.pw/{userid}.png")
			embed.set_image(url=f"https://assets.ppy.sh/beatmaps/{beatmapset_id}/covers/cover.jpg")
			embed.set_footer(text=f"osu!{hahaha} {text} Plays for {username} ")
			await ctx.send(embed=embed)

		@Chiyo.command(aliases=['top','t'])
		async def _top(ctx, *args):
			relax, mode, scoreid = 0, 0, 0
			msg = ctx.message.content.split(' ')[1:]

			if '-rx' in msg:
				msg.remove('-rx')
				relax = 1
			if '-p' in msg:
				scoreid = int(msg[msg.index('-p') + 1])
				msg.remove(msg[msg.index('-p') + 1])
				msg.remove('-p')
			if '-taiko' in msg:
				msg.remove('-taiko')
				mode = 1
			if '-ctb' in msg:
				msg.remove('-ctb')
				mode = 2
			if '-mania' in msg:
				msg.remove('-mania')
				mode, relax = 3, 0

			switcher = {
				0: 'Standard',
				1: 'Taiko',
				2: 'Catch The Beat',
				3: 'Mania'
			}

			another_switcher = {
				0: '',
				1: ' Relax'
			}
			hahaha = another_switcher.get(relax)
			text = switcher.get(mode)

			if ctx.message.mentions:
				e = db.get(User.id == ctx.message.mentions[0].id)
				if e == None:
					return await ctx.send("User couldn't be found in our database! Try connecting a user to our database by doing `;connect user`")
				userid = e['akatsuki']
			elif len(msg) == 0:
				e = db.get(User.id == ctx.message.author.id)
				if e == None:
					return await ctx.send("User couldn't be found in our database! Try connecting a user to our database by doing `;connect user`")
				userid = e['akatsuki']
			else:
				if osuhelper.get_id(' '.join(msg)) == "Couldn't find user!":
					return await ctx.send("Couldn't find this user!")
				userid = osuhelper.get_id(' '.join(msg))

			info = osuhelper.Helper(userid)
			stats = info.top(mode=mode, relax=relax, scoreid=scoreid)

			letters = {
				'SSH': 'https://cdn.discordapp.com/emojis/724849277406281728.png?v=1',
				'SH': 'https://cdn.discordapp.com/emojis/724847645142810624.png?v=1',
				'SS': 'https://cdn.discordapp.com/emojis/724849299300548680.png?v=1',
				'S': 'https://cdn.discordapp.com/emojis/724847668953874493.png?v=1',
				'A': 'https://cdn.discordapp.com/emojis/724841194517037137.png?v=1',
				'B': 'https://cdn.discordapp.com/emojis/724841229602521109.png?v=1',
				'C': 'https://cdn.discordapp.com/emojis/724841244530049095.png?v=1',
				'D': 'https://cdn.discordapp.com/emojis/724841263727116379.png?v=1'
			}
			man = {
				0: 'std',
				1: 'taiko',
				2: 'ctb',
				3: 'mania'
			}
			rank = letters.get(stats['rank'])
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

			cache[ctx.guild.id] = {ctx.message.channel.id: {'beatmap_id': beatmap_id, 'ar': ar, 'od': od, 'full_combo': full_combo, 'songname': songname, 'difficulty': difficulty, 'beatmapset_id': beatmapset_id}}

			embed=discord.Embed(description=f'▸ {pp}PP [AR: {ar} OD: {od}] ▸ {accuracy}%\n▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{count_300}/{count_100}/{count_50}/{count_miss}]\n▸ Map Completed: {completed}', color=0xb6ebf1)
			embed.set_author(name=f"{songname} +{mods} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmap_id}", icon_url=rank)
			embed.set_thumbnail(url=f"https://a.akatsuki.pw/{userid}.png")
			embed.set_image(url=f"https://assets.ppy.sh/beatmaps/{beatmapset_id}/covers/cover.jpg")
			embed.set_footer(text=f"Top osu!{hahaha} {text} Play for {username} ")
			await ctx.send(embed=embed)

		@Chiyo.command(aliases=['recent','rs','rc','r'])
		async def _recent(ctx, *args):
			relax, mode, scoreid = 0, 0, 0
			msg = ctx.message.content.split(' ')[1:]

			if '-rx' in msg:
				msg.remove('-rx')
				relax = 1
			if '-p' in msg:
				scoreid = int(msg[msg.index('-p') + 1])
				msg.remove(msg[msg.index('-p') + 1])
				msg.remove('-p')
			if '-taiko' in msg:
				msg.remove('-taiko')
				mode = 1
			if '-ctb' in msg:
				msg.remove('-ctb')
				mode = 2
			if '-mania' in msg:
				msg.remove('-mania')
				mode, relax = 3, 0

			switcher = {
				0: 'Standard',
				1: 'Taiko',
				2: 'Catch The Beat',
				3: 'Mania'
			}

			another_switcher = {
				0: '',
				1: ' Relax'
			}
			hahaha = another_switcher.get(relax)
			text = switcher.get(mode)

			if ctx.message.mentions:
				e = db.get(User.id == ctx.message.mentions[0].id)
				if e == None:
					return await ctx.send("User couldn't be found in our database! Try connecting a user to our database by doing `;connect user`")
				userid = e['akatsuki']
			elif len(msg) == 0:
				e = db.get(User.id == ctx.message.author.id)
				if e == None:
					return await ctx.send("User couldn't be found in our database! Try connecting a user to our database by doing `;connect user`")
				userid = e['akatsuki']
			else:
				if osuhelper.get_id(' '.join(msg)) == "Couldn't find user!":
					return await ctx.send("Couldn't find this user!")
				userid = osuhelper.get_id(' '.join(msg))

			info = osuhelper.Helper(userid)
			stats = info.recent(mode=mode, relax=relax, scoreid=scoreid)

			letters = {
				'SSH': 'https://cdn.discordapp.com/emojis/724849277406281728.png?v=1',
				'SH': 'https://cdn.discordapp.com/emojis/724847645142810624.png?v=1',
				'SS': 'https://cdn.discordapp.com/emojis/724849299300548680.png?v=1',
				'S': 'https://cdn.discordapp.com/emojis/724847668953874493.png?v=1',
				'A': 'https://cdn.discordapp.com/emojis/724841194517037137.png?v=1',
				'B': 'https://cdn.discordapp.com/emojis/724841229602521109.png?v=1',
				'C': 'https://cdn.discordapp.com/emojis/724841244530049095.png?v=1',
				'D': 'https://cdn.discordapp.com/emojis/724841263727116379.png?v=1'
			}
			man = {
				0: 'std',
				1: 'taiko',
				2: 'ctb',
				3: 'mania'
			}
			rank = letters.get(stats['rank'])
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

			cache[ctx.guild.id] = {ctx.message.channel.id: {'beatmap_id': beatmap_id, 'ar': ar, 'od': od, 'full_combo': full_combo, 'songname': songname, 'difficulty': difficulty, 'beatmapset_id': beatmapset_id}}

			embed=discord.Embed(description=f'▸ {pp}PP [AR: {ar} OD: {od}] ▸ {accuracy}%\n▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{count_300}/{count_100}/{count_50}/{count_miss}]\n▸ Map Completed: {completed}', color=0xb6ebf1)
			embed.set_author(name=f"{songname} +{mods} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmap_id}", icon_url=rank)
			embed.set_thumbnail(url=f"https://a.akatsuki.pw/{userid}.png")
			embed.set_image(url=f"https://assets.ppy.sh/beatmaps/{beatmapset_id}/covers/cover.jpg")
			embed.set_footer(text=f"Most Recent osu!{hahaha} {text} Play for {username} ")
			await ctx.send(embed=embed)
		
		@Chiyo.command(aliases=['osu', 'p', 'profile'])
		async def _profile(ctx, *args):
			relax, mode = 0, 0
			msg = ctx.message.content.split(' ')[1:]

			if '-rx' in msg:
				msg.remove('-rx')
				relax = 1
			if '-taiko' in msg:
				msg.remove('-taiko')
				mode = 1
			if '-ctb' in msg:
				msg.remove('-ctb')
				mode = 2
			if '-mania' in msg:
				msg.remove('-mania')
				mode, relax = 3, 0

			switcher = {
				0: 'Standard',
				1: 'Taiko',
				2: 'Catch The Beat',
				3: 'Mania'
			}

			another_switcher = {
				0: '',
				1: 'Relax'
			}
			hahaha = another_switcher.get(relax)
			text = switcher.get(mode)

			if ctx.message.mentions:
				e = db.get(User.id == ctx.message.mentions[0].id)
				if e == None:
					return await ctx.send("User couldn't be found in our database! Try connecting a user to our database by doing `;connect user`")
				userid = e['akatsuki']
			elif len(msg) == 0:
				e = db.get(User.id == ctx.message.author.id)
				if e == None:
					return await ctx.send("User couldn't be found in our database! Try connecting a user to our database by doing `;connect user`")
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
			embed=discord.Embed(description=f'▸ Official Rank: {official_rank} ({country}#{country_rank}) \n▸ Level: {level}\n▸ Total PP: {pp} \n▸ Accuracy: {accuracy}% \n▸ Playcount: {playcount}', color=0xb6ebf1)
			embed.set_author(name=f"osu!{hahaha} {text} Profile for {username} ", url=f"https://akatsuki.pw/u/{userid}", icon_url=f"https://avatars0.githubusercontent.com/u/45724130?s=200&v=4.png")
			embed.set_thumbnail(url=f"https://a.akatsuki.pw/{userid}.png")
			embed.set_footer(text=f"Player on Akatsuki!")
			return await ctx.send(embed=embed)

		@Chiyo.command()
		async def connect(ctx, *args):

			if len(args) == 0:
				return await ctx.send('Must provide a username!')

			msg = '{}'.format(' '.join(args))

			if osuhelper.get_id(msg) == "Couldn't find user!":
				return await ctx.send("Couldn't find this user!")
			userid = osuhelper.get_id(msg)

			owo = db.search(User.id == ctx.message.author.id)
			
			if str(owo) == '[]': #https://a.ppy.sh/13028687
				db.insert({'id': ctx.message.author.id, 'akatsuki': userid})
				embed=discord.Embed(colour = 0xb6ebf1)
				embed.set_author(name=f"User {msg} was connected to your discord account!", url=f"https://akatsuki.pw/u/{userid}")
				embed.set_image(url="https://a.akatsuki.pw/{}.png".format(userid))
				return await ctx.send(embed=embed)
			else:
				db.update({'akatsuki': userid}, User.id == ctx.message.author.id)
				embed=discord.Embed(colour = 0xb6ebf1)
				embed.set_author(name=f"User {msg} was connected to your discord account!", url=f"https://akatsuki.pw/u/{userid}")
				embed.set_image(url="https://a.akatsuki.pw/{}.png".format(userid))
				return await ctx.send(embed=embed)

		@Chiyo.command()
		async def about(ctx):
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
						
	def run(self):
		self.Nyoko()
		Chiyo.run(self.token)

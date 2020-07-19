import discord
import config
import requests
import pymongo
from pymongo import *
from discord.ext import commands
import enum
import os
from enum import IntEnum

cluster = pymongo.MongoClient(f'mongodb+srv://Cover:{config.dbpassword}@chiyo-y6grb.mongodb.net/{config.dbname}?retryWrites=true&w=majority')
db = cluster['Akatsuki']
collation = db['Akatsuki']

class Akatsuki(commands.Cog):

	def __init___(self, client):
		self.client = client

	@commands.command()
	async def recent(self, ctx, *args):
		
		yo = len(args)

		if yo == 0:
			
			u = collation.find_one({"_id": ctx.message.author.id})
			ouo = u['name']
			omgogmogmogmogmogm = str(ouo)

			stats = requests.get(f'https://akatsuki.pw/api/v1/users/scores/recent?name={omgogmogmogmogmogm}&mode=0')

			if not stats:
				await ctx.send(f'Couldnt find user {omgogmogmogmogmogm}!')
			else:
				userinfo = requests.get(f'https://akatsuki.pw/api/v1/users?name={omgogmogmogmogmogm}')
			if not userinfo:
				await ctx.send(f'Couldnt find user {omgogmogmogmogmogm}!')
			else:
				acc = stats.json()['scores'][0]['accuracy']
			accuracy = round(acc, 2)
			mapname = stats.json()['scores'][0]['beatmap']['song_name']
			beatmapid = stats.json()['scores'][0]['beatmap']['beatmap_id']
			beatmapsetid = stats.json()['scores'][0]['beatmap']['beatmapset_id']
			mods = stats.json()['scores'][0]['mods']
			setdifficulty = stats.json()['scores'][0]['beatmap']['difficulty']
			difficulty = round(setdifficulty, 2)
			rank = stats.json()['scores'][0]['rank']
			ppp = stats.json()['scores'][0]['pp']
			pp = round(ppp, 2)
			score = stats.json()['scores'][0]['score']
			combo = stats.json()['scores'][0]['max_combo']
			beatmapcombo = stats.json()['scores'][0]['beatmap']['max_combo']
			Three = stats.json()['scores'][0]['count_300']
			one = stats.json()['scores'][0]['count_100']
			five = stats.json()['scores'][0]['count_50']
			misses = stats.json()['scores'][0]['count_miss']
			completed = stats.json()['scores'][0]['completed']
			ranked = stats.json()['scores'][0]['beatmap']['ranked']
			ar = stats.json()['scores'][0]['beatmap']['ar']
			od = stats.json()['scores'][0]['beatmap']['od']
			time = stats.json()['scores'][0]['time']
			
			if 'Z' in time:
				timee = time.replace('T',' ')
				currenttime = timee.replace('Z',' ')

			if ranked == 2:
				status = 'Yes'
			else:
				status = 'No'

			if mods == 0:
				modsletters = 'NM'
			else:
				modsletters = config.readableMods(mods)

			if 'NC' in modsletters:
				modsCheck = modsletters.replace('DT','')
			else:
				modsCheck = modsletters

			if completed == 3:
				msgcompleted = 'Yes'
			else:
				msgcompleted = 'No'

			userid = userinfo.json()['id']
			username = userinfo.json()['username']

			await ctx.send(f'Most Recent osu! Standard Play for {username}')
			embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR:{ar} OD:{od}] ▸ {accuracy}%\n▸ {score} ▸ {combo}x/{beatmapcombo}x ▸ [{Three}/{one}/{five}/{misses}]\n▸ Map Completed: {msgcompleted}', color=0xb6ebf1)
			embed.set_author(name=f"{mapname} +{modsCheck} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmapid}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
			embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapsetid}l.jpg")
			embed.set_footer(text=f"This score was set on {currenttime}")
			await ctx.send(embed=embed)
		else:

			msg = '{}'.format(' '.join(args))

			stats = requests.get(f'https://akatsuki.pw/api/v1/users/scores/recent?name={msg}&mode=0')

			if not stats:
				return await ctx.send(f'Couldnt find user {msg}!')
			else:
				userinfo = requests.get(f'https://akatsuki.pw/api/v1/users?name={msg}')
			if not userinfo:
				return await ctx.send(f'Couldnt find user {msg}!')
			else:
				acc = stats.json()['scores'][0]['accuracy']
				accuracy = round(acc, 2)
				mapname = stats.json()['scores'][0]['beatmap']['song_name']
				beatmapid = stats.json()['scores'][0]['beatmap']['beatmap_id']
				beatmapsetid = stats.json()['scores'][0]['beatmap']['beatmapset_id']
				mods = stats.json()['scores'][0]['mods']
				setdifficulty = stats.json()['scores'][0]['beatmap']['difficulty']
				difficulty = round(setdifficulty, 2)
				rank = stats.json()['scores'][0]['rank']
				ppp = stats.json()['scores'][0]['pp']
				pp = round(ppp, 2)
				score = stats.json()['scores'][0]['score']
				combo = stats.json()['scores'][0]['max_combo']
				beatmapcombo = stats.json()['scores'][0]['beatmap']['max_combo']
				Three = stats.json()['scores'][0]['count_300']
				one = stats.json()['scores'][0]['count_100']
				five = stats.json()['scores'][0]['count_50']
				misses = stats.json()['scores'][0]['count_miss']
				completed = stats.json()['scores'][0]['completed']
				ranked = stats.json()['scores'][0]['beatmap']['ranked']
				ar = stats.json()['scores'][0]['beatmap']['ar']
				od = stats.json()['scores'][0]['beatmap']['od']
				time = stats.json()['scores'][0]['time']

				if 'Z' in time:
					timee = time.replace('T',' ')
					currenttime = timee.replace('Z',' ')

				if ranked == 2:
					status = 'Yes'
				else:
					status = 'No'

				if mods == 0:
					modsletters = 'NM'
				else:
					modsletters = config.readableMods(mods)

				if 'NC' in modsletters:
					modsCheck = modsletters.replace('DT','')
				else:
					modsCheck = modsletters

				if completed == 3:
					msgcompleted = 'Yes'
				else:
					msgcompleted = 'No'

				userid = userinfo.json()['id']
				username = userinfo.json()['username']

				await ctx.send(f'Most Recent osu! Standard Play for {username}')
				embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR:{ar} OD:{od}] ▸ {accuracy}%\n▸ {score} ▸ {combo}x/{beatmapcombo}x ▸ [{Three}/{one}/{five}/{misses}]\n▸ Map Completed: {msgcompleted}', color=0xb6ebf1)
				embed.set_author(name=f"{mapname} +{modsCheck} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmapid}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
				embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapsetid}l.jpg")
				embed.set_footer(text=f"This score was set on {currenttime}")
				await ctx.send(embed=embed)

	@commands.command()
	async def relaxrecent(self, ctx, *args):

		yo = len(args)

		if yo == 0:
			
			u = collation.find_one({"_id": ctx.message.author.id})
			ouo = u['name']
			omg = str(ouo)
		
			stats = requests.get(f'https://akatsuki.pw/api/v1/users/scores/recent?rx=1&name={omg}&mode=0')
			if not stats:
				await ctx.send(f'Couldnt find user {omg}!')
			else:
				userinfo = requests.get(f'https://akatsuki.pw/api/v1/users?name={omg}')
			if not userinfo:
				await ctx.send(f'Couldnt find user {omg}!')
			else:
				acc = stats.json()['scores'][0]['accuracy']
			accuracy = round(acc, 2)
			mapname = stats.json()['scores'][0]['beatmap']['song_name']
			beatmapid = stats.json()['scores'][0]['beatmap']['beatmap_id']
			beatmapsetid = stats.json()['scores'][0]['beatmap']['beatmapset_id']
			mods = stats.json()['scores'][0]['mods']
			setdifficulty = stats.json()['scores'][0]['beatmap']['difficulty']
			difficulty = round(setdifficulty, 2)
			rank = stats.json()['scores'][0]['rank']
			ppp = stats.json()['scores'][0]['pp']
			pp = round(ppp, 2)
			score = stats.json()['scores'][0]['score']
			combo = stats.json()['scores'][0]['max_combo']
			beatmapcombo = stats.json()['scores'][0]['beatmap']['max_combo']
			Three = stats.json()['scores'][0]['count_300']
			one = stats.json()['scores'][0]['count_100']
			five = stats.json()['scores'][0]['count_50']
			misses = stats.json()['scores'][0]['count_miss']
			completed = stats.json()['scores'][0]['completed']
			ranked = stats.json()['scores'][0]['beatmap']['ranked']
			ar = stats.json()['scores'][0]['beatmap']['ar']
			od = stats.json()['scores'][0]['beatmap']['od']
			time = stats.json()['scores'][0]['time']

			if 'Z' in time:
				timee = time.replace('T',' ')
				currenttime = timee.replace('Z',' ')

			if ranked == 2:
				status = 'Yes'
			else:
				status = 'No'

			if mods == 0:
				modsletters = 'NM'
			else:
				modsletters = config.readableMods(mods)

			if 'NC' in modsletters:
				modsCheck = modsletters.replace('DT','')
			else:
				modsCheck = modsletters

			if completed == 3:
				msgcompleted = 'Yes'
			else:
				msgcompleted = 'No'

			userid = userinfo.json()['id']
			username = userinfo.json()['username']

			await ctx.send(f'Most Recent osu! Relax Standard Play for {username}')
			embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR: {ar} OD: {od}] ▸ {accuracy}%\n▸ {score} ▸ {combo}x/{beatmapcombo}x ▸ [{Three}/{one}/{five}/{misses}]\n▸ Map Completed: {msgcompleted}', color=0xb6ebf1)
			embed.set_author(name=f"{mapname} +{modsCheck} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmapid}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
			embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapsetid}l.jpg")
			embed.set_footer(text=f"This score was set on {currenttime}")
			await ctx.send(embed=embed)
		else:
			
			msg = '{}'.format(' '.join(args))

			stats = requests.get(f'https://akatsuki.pw/api/v1/users/scores/recent?rx=1&name={msg}&mode=0')
			
			if not stats:
				await ctx.send(f'Couldnt find user {msg}!')
			else:
				userinfo = requests.get(f'https://akatsuki.pw/api/v1/users?name={msg}')
			if not userinfo:
				await ctx.send(f'Couldnt find user {msg}!')
			else:
				acc = stats.json()['scores'][0]['accuracy']
			accuracy = round(acc, 2)
			mapname = stats.json()['scores'][0]['beatmap']['song_name']
			beatmapid = stats.json()['scores'][0]['beatmap']['beatmap_id']
			beatmapsetid = stats.json()['scores'][0]['beatmap']['beatmapset_id']
			mods = stats.json()['scores'][0]['mods']
			setdifficulty = stats.json()['scores'][0]['beatmap']['difficulty']
			difficulty = round(setdifficulty, 2)
			rank = stats.json()['scores'][0]['rank']
			ppp = stats.json()['scores'][0]['pp']
			pp = round(ppp, 2)
			score = stats.json()['scores'][0]['score']
			combo = stats.json()['scores'][0]['max_combo']
			beatmapcombo = stats.json()['scores'][0]['beatmap']['max_combo']
			Three = stats.json()['scores'][0]['count_300']
			one = stats.json()['scores'][0]['count_100']
			five = stats.json()['scores'][0]['count_50']
			misses = stats.json()['scores'][0]['count_miss']
			completed = stats.json()['scores'][0]['completed']
			ranked = stats.json()['scores'][0]['beatmap']['ranked']
			ar = stats.json()['scores'][0]['beatmap']['ar']
			od = stats.json()['scores'][0]['beatmap']['od']
			time = stats.json()['scores'][0]['time']

			if 'Z' in time:
				timee = time.replace('T',' ')
				currenttime = timee.replace('Z',' ')

			if ranked == 2:
				status = 'Yes'
			else:
				status = 'No'

			if mods == 0:
				modsletters = 'NM'
			else:
				modsletters = config.readableMods(mods)

			if 'NC' in modsletters:
				modsCheck = modsletters.replace('DT','')
			else:
				modsCheck = modsletters

			if completed == 3:
				msgcompleted = 'Yes'
			else:
				msgcompleted = 'No'

			userid = userinfo.json()['id']
			username = userinfo.json()['username']

			await ctx.send(f'Most Recent osu! Relax Standard Play for {username}')
			embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR: {ar} OD: {od}] ▸ {accuracy}%\n▸ {score} ▸ {combo}x/{beatmapcombo}x ▸ [{Three}/{one}/{five}/{misses}]\n▸ Map Completed: {msgcompleted}', color=0xb6ebf1)
			embed.set_author(name=f"{mapname} +{modsCheck} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmapid}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
			embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapsetid}l.jpg")
			embed.set_footer(text=f"This score was set on {currenttime}")
			await ctx.send(embed=embed)

	@commands.command()
	async def top(self, ctx, *args):

		yo = len(args)

		if yo == 0:
			
			u = collation.find_one({"_id": ctx.message.author.id})
			ouo = u['name']
			omg = str(ouo)
		
			stats = requests.get(f'https://akatsuki.pw/api/v1/users/scores/best?rx=0&name={omg}&mode=0')
			if not stats:
				await ctx.send(f'Couldnt find user {omg}!')
			else:
				userinfo = requests.get(f'https://akatsuki.pw/api/v1/users?name={omg}')
			if not userinfo:
				await ctx.send(f'Couldnt find user {omg}!')
			else:
				acc = stats.json()['scores'][0]['accuracy']
			accuracy = round(acc, 2)
			mapname = stats.json()['scores'][0]['beatmap']['song_name']
			beatmapid = stats.json()['scores'][0]['beatmap']['beatmap_id']
			beatmapsetid = stats.json()['scores'][0]['beatmap']['beatmapset_id']
			mods = stats.json()['scores'][0]['mods']
			setdifficulty = stats.json()['scores'][0]['beatmap']['difficulty']
			difficulty = round(setdifficulty, 2)
			rank = stats.json()['scores'][0]['rank']
			ppp = stats.json()['scores'][0]['pp']
			pp = round(ppp, 2)
			score = stats.json()['scores'][0]['score']
			combo = stats.json()['scores'][0]['max_combo']
			beatmapcombo = stats.json()['scores'][0]['beatmap']['max_combo']
			Three = stats.json()['scores'][0]['count_300']
			one = stats.json()['scores'][0]['count_100']
			five = stats.json()['scores'][0]['count_50']
			misses = stats.json()['scores'][0]['count_miss']
			completed = stats.json()['scores'][0]['completed']
			ranked = stats.json()['scores'][0]['beatmap']['ranked']
			ar = stats.json()['scores'][0]['beatmap']['ar']
			od = stats.json()['scores'][0]['beatmap']['od']
			time = stats.json()['scores'][0]['time']

			if 'Z' in time:
				timee = time.replace('T',' ')
				currenttime = timee.replace('Z',' ')

			if ranked == 2:
				status = 'Yes'
			else:
				status = 'No'

			if mods == 0:
				modsletters = 'NM'
			else:
				modsletters = config.readableMods(mods)

			if 'NC' in modsletters:
				modsCheck = modsletters.replace('DT','')
			else:
				modsCheck = modsletters

			if completed == 3:
				msgcompleted = 'Yes'
			else:
				msgcompleted = 'No'

			userid = userinfo.json()['id']
			username = userinfo.json()['username']

			await ctx.send(f'Top osu! Standard Play for {username}')
			embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR:{ar} OD:{od}] ▸ {accuracy}%\n▸ {score} ▸ {combo}x/{beatmapcombo}x ▸ [{Three}/{one}/{five}/{misses}]\n▸ Map Completed: {msgcompleted}', color=0xb6ebf1)
			embed.set_author(name=f"{mapname} +{modsCheck} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmapid}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
			embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapsetid}l.jpg")
			embed.set_footer(text=f"This score was set on {currenttime}")
			await ctx.send(embed=embed)
		else:
			msg = '{}'.format(' '.join(args))

			stats = requests.get(f'https://akatsuki.pw/api/v1/users/scores/best?rx=0&name={msg}&mode=0')
			if not stats:
				await ctx.send(f'Couldnt find user {msg}!')
			else:
				userinfo = requests.get(f'https://akatsuki.pw/api/v1/users?name={msg}')
			if not userinfo:
				await ctx.send(f'Couldnt find user {msg}!')
			else:
				acc = stats.json()['scores'][0]['accuracy']
			accuracy = round(acc, 2)
			mapname = stats.json()['scores'][0]['beatmap']['song_name']
			beatmapid = stats.json()['scores'][0]['beatmap']['beatmap_id']
			beatmapsetid = stats.json()['scores'][0]['beatmap']['beatmapset_id']
			mods = stats.json()['scores'][0]['mods']
			setdifficulty = stats.json()['scores'][0]['beatmap']['difficulty']
			difficulty = round(setdifficulty, 2)
			rank = stats.json()['scores'][0]['rank']
			ppp = stats.json()['scores'][0]['pp']
			pp = round(ppp, 2)
			score = stats.json()['scores'][0]['score']
			combo = stats.json()['scores'][0]['max_combo']
			beatmapcombo = stats.json()['scores'][0]['beatmap']['max_combo']
			Three = stats.json()['scores'][0]['count_300']
			one = stats.json()['scores'][0]['count_100']
			five = stats.json()['scores'][0]['count_50']
			misses = stats.json()['scores'][0]['count_miss']
			completed = stats.json()['scores'][0]['completed']
			ranked = stats.json()['scores'][0]['beatmap']['ranked']
			ar = stats.json()['scores'][0]['beatmap']['ar']
			od = stats.json()['scores'][0]['beatmap']['od']
			time = stats.json()['scores'][0]['time']

			if 'Z' in time:
				timee = time.replace('T',' ')
				currenttime = timee.replace('Z',' ')

			if ranked == 2:
				status = 'Yes'
			else:
				status = 'No'

			if mods == 0:
				modsletters = 'NM'
			else:
				modsletters = config.readableMods(mods)

			if 'NC' in modsletters:
				modsCheck = modsletters.replace('DT','')
			else:
				modsCheck = modsletters

			if completed == 3:
				msgcompleted = 'Yes'
			else:
				msgcompleted = 'No'

			userid = userinfo.json()['id']
			username = userinfo.json()['username']

			await ctx.send(f'Top osu! Standard Play for {username}')
			embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR:{ar} OD:{od}] ▸ {accuracy}%\n▸ {score} ▸ {combo}x/{beatmapcombo}x ▸ [{Three}/{one}/{five}/{misses}]\n▸ Map Completed: {msgcompleted}', color=0xb6ebf1)
			embed.set_author(name=f"{mapname} +{modsCheck} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmapid}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
			embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapsetid}l.jpg")
			embed.set_footer(text=f"This score was set on {currenttime}")
			await ctx.send(embed=embed)

	@commands.command()
	async def relaxtop(self, ctx, *args):
		
		yo = len(args)

		if yo == 0:
			
			u = collation.find_one({"_id": ctx.message.author.id})
			ouo = u['name']
			omg = str(ouo)
		
			stats = requests.get(f'https://akatsuki.pw/api/v1/users/scores/best?rx=1&name={omg}&mode=0')
			if not stats:
				await ctx.send(f'Couldnt find user {omg}!')
			else:
				userinfo = requests.get(f'https://akatsuki.pw/api/v1/users?name={omg}')
			if not userinfo:
				await ctx.send(f'Couldnt find user {omg}!')
			else:
				acc = stats.json()['scores'][0]['accuracy']
			accuracy = round(acc, 2)
			mapname = stats.json()['scores'][0]['beatmap']['song_name']
			beatmapid = stats.json()['scores'][0]['beatmap']['beatmap_id']
			beatmapsetid = stats.json()['scores'][0]['beatmap']['beatmapset_id']
			mods = stats.json()['scores'][0]['mods']
			setdifficulty = stats.json()['scores'][0]['beatmap']['difficulty']
			difficulty = round(setdifficulty, 2)
			rank = stats.json()['scores'][0]['rank']
			ppp = stats.json()['scores'][0]['pp']
			pp = round(ppp, 2)
			score = stats.json()['scores'][0]['score']
			combo = stats.json()['scores'][0]['max_combo']
			beatmapcombo = stats.json()['scores'][0]['beatmap']['max_combo']
			Three = stats.json()['scores'][0]['count_300']
			one = stats.json()['scores'][0]['count_100']
			five = stats.json()['scores'][0]['count_50']
			misses = stats.json()['scores'][0]['count_miss']
			completed = stats.json()['scores'][0]['completed']
			ranked = stats.json()['scores'][0]['beatmap']['ranked']
			ar = stats.json()['scores'][0]['beatmap']['ar']
			od = stats.json()['scores'][0]['beatmap']['od']
			time = stats.json()['scores'][0]['time']

			if 'Z' in time:
				timee = time.replace('T',' ')
				currenttime = timee.replace('Z',' ')

			if ranked == 2:
				status = 'Yes'
			else:
				status = 'No'

			if mods == 0:
				modsletters = 'NM'
			else:
				modsletters = config.readableMods(mods)

			if 'NC' in modsletters:
				modsCheck = modsletters.replace('DT','')
			else:
				modsCheck = modsletters

			if completed == 3:
				msgcompleted = 'Yes'
			else:
				msgcompleted = 'No'

			userid = userinfo.json()['id']
			username = userinfo.json()['username']

			await ctx.send(f'Top osu! Relax Standard Play for {username}')
			embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR:{ar} OD:{od}] ▸ {accuracy}%\n▸ {score} ▸ {combo}x/{beatmapcombo}x ▸ [{Three}/{one}/{five}/{misses}]\n▸ Map Completed: {msgcompleted}', color=0xb6ebf1)
			embed.set_author(name=f"{mapname} +{modsCheck} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmapid}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
			embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapsetid}l.jpg")
			embed.set_footer(text=f"This score was set on {currenttime}")
			await ctx.send(embed=embed)
		else:
			msg = '{}'.format(' '.join(args))

			stats = requests.get(f'https://akatsuki.pw/api/v1/users/scores/best?rx=1&name={msg}&mode=0')
			if not stats:
				await ctx.send(f'Couldnt find user {msg}!')
			else:
				userinfo = requests.get(f'https://akatsuki.pw/api/v1/users?name={msg}')
			if not userinfo:
				await ctx.send(f'Couldnt find user {msg}!')
			else:
				acc = stats.json()['scores'][0]['accuracy']
			accuracy = round(acc, 2)
			mapname = stats.json()['scores'][0]['beatmap']['song_name']
			beatmapid = stats.json()['scores'][0]['beatmap']['beatmap_id']
			beatmapsetid = stats.json()['scores'][0]['beatmap']['beatmapset_id']
			mods = stats.json()['scores'][0]['mods']
			setdifficulty = stats.json()['scores'][0]['beatmap']['difficulty']
			difficulty = round(setdifficulty, 2)
			rank = stats.json()['scores'][0]['rank']
			ppp = stats.json()['scores'][0]['pp']
			pp = round(ppp, 2)
			score = stats.json()['scores'][0]['score']
			combo = stats.json()['scores'][0]['max_combo']
			beatmapcombo = stats.json()['scores'][0]['beatmap']['max_combo']
			Three = stats.json()['scores'][0]['count_300']
			one = stats.json()['scores'][0]['count_100']
			five = stats.json()['scores'][0]['count_50']
			misses = stats.json()['scores'][0]['count_miss']
			completed = stats.json()['scores'][0]['completed']
			ranked = stats.json()['scores'][0]['beatmap']['ranked']
			ar = stats.json()['scores'][0]['beatmap']['ar']
			od = stats.json()['scores'][0]['beatmap']['od']
			time = stats.json()['scores'][0]['time']

			if 'Z' in time:
				timee = time.replace('T',' ')
				currenttime = timee.replace('Z',' ')

			if ranked == 2:
				status = 'Yes'
			else:
				status = 'No'

			if mods == 0:
				modsletters = 'NM'
			else:
				modsletters = config.readableMods(mods)

			if 'NC' in modsletters:
				modsCheck = modsletters.replace('DT','')
			else:
				modsCheck = modsletters

			if completed == 3:
				msgcompleted = 'Yes'
			else:
				msgcompleted = 'No'

			userid = userinfo.json()['id']
			username = userinfo.json()['username']

			await ctx.send(f'Top osu! Relax Standard Play for {username}')
			embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR:{ar} OD:{od}] ▸ {accuracy}%\n▸ {score} ▸ {combo}x/{beatmapcombo}x ▸ [{Three}/{one}/{five}/{misses}]\n▸ Map Completed: {msgcompleted}', color=0xb6ebf1)
			embed.set_author(name=f"{mapname} +{modsCheck} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmapid}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
			embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapsetid}l.jpg")
			embed.set_footer(text=f"This score was set on {currenttime}")
			await ctx.send(embed=embed)

	@commands.command()
	async def taikotop(self, ctx, *args):
		
		yo = len(args)

		if yo == 0:
			
			u = collation.find_one({"_id": ctx.message.author.id})
			ouo = u['name']
			omg = str(ouo)
		
			stats = requests.get(f'https://akatsuki.pw/api/v1/users/scores/best?rx=0&name={omg}&mode=1')
			if not stats:
				await ctx.send(f'Couldnt find user {omg}!')
			else:
				userinfo = requests.get(f'https://akatsuki.pw/api/v1/users?name={omg}')
			if not userinfo:
				await ctx.send(f'Couldnt find user {omg}!')
			else:
				acc = stats.json()['scores'][0]['accuracy']
			accuracy = round(acc, 2)
			mapname = stats.json()['scores'][0]['beatmap']['song_name']
			beatmapid = stats.json()['scores'][0]['beatmap']['beatmap_id']
			beatmapsetid = stats.json()['scores'][0]['beatmap']['beatmapset_id']
			mods = stats.json()['scores'][0]['mods']
			setdifficulty = stats.json()['scores'][0]['beatmap']['difficulty2']['taiko']
			difficulty = round(setdifficulty, 2)
			rank = stats.json()['scores'][0]['rank']
			ppp = stats.json()['scores'][0]['pp']
			pp = round(ppp, 2)
			score = stats.json()['scores'][0]['score']
			combo = stats.json()['scores'][0]['max_combo']
			beatmapcombo = stats.json()['scores'][0]['beatmap']['max_combo']
			Three = stats.json()['scores'][0]['count_300']
			one = stats.json()['scores'][0]['count_100']
			five = stats.json()['scores'][0]['count_50']
			misses = stats.json()['scores'][0]['count_miss']
			completed = stats.json()['scores'][0]['completed']
			ranked = stats.json()['scores'][0]['beatmap']['ranked']
			ar = stats.json()['scores'][0]['beatmap']['ar']
			od = stats.json()['scores'][0]['beatmap']['od']
			time = stats.json()['scores'][0]['time']

			if 'Z' in time:
				timee = time.replace('T',' ')
				currenttime = timee.replace('Z',' ')

			if ranked == 2:
				status = 'Yes'
			else:
				status = 'No'

			if mods == 0:
				modsletters = 'NM'
			else:
				modsletters = config.readableMods(mods)

			if 'NC' in modsletters:
				modsCheck = modsletters.replace('DT','')
			else:
				modsCheck = modsletters

			if completed == 3:
				msgcompleted = 'Yes'
			else:
				msgcompleted = 'No'

			userid = userinfo.json()['id']
			username = userinfo.json()['username']

			await ctx.send(f'Top osu! Taiko Play for {username}')
			embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR:{ar} OD:{od}] ▸ {accuracy}%\n▸ {score} ▸ {combo}x/{beatmapcombo}x ▸ [{Three}/{one}/{five}/{misses}]\n▸ Map Completed: {msgcompleted}', color=0xb6ebf1)
			embed.set_author(name=f"{mapname} +{modsCheck} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmapid}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
			embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapsetid}l.jpg")
			embed.set_footer(text=f"This score was set on {currenttime}")
			await ctx.send(embed=embed)
		else:
			msg = '{}'.format(' '.join(args))

			stats = requests.get(f'https://akatsuki.pw/api/v1/users/scores/best?rx=0&name={msg}&mode=1')
			if not stats:
				await ctx.send(f'Couldnt find user {msg}!')
			else:
				userinfo = requests.get(f'https://akatsuki.pw/api/v1/users?name={msg}')
			if not userinfo:
				await ctx.send(f'Couldnt find user {msg}!')
			else:
				acc = stats.json()['scores'][0]['accuracy']
			accuracy = round(acc, 2)
			mapname = stats.json()['scores'][0]['beatmap']['song_name']
			beatmapid = stats.json()['scores'][0]['beatmap']['beatmap_id']
			beatmapsetid = stats.json()['scores'][0]['beatmap']['beatmapset_id']
			mods = stats.json()['scores'][0]['mods']
			setdifficulty = stats.json()['scores'][0]['beatmap']['difficulty']
			difficulty = round(setdifficulty, 2)
			rank = stats.json()['scores'][0]['rank']
			ppp = stats.json()['scores'][0]['pp']
			pp = round(ppp, 2)
			score = stats.json()['scores'][0]['score']
			combo = stats.json()['scores'][0]['max_combo']
			beatmapcombo = stats.json()['scores'][0]['beatmap']['max_combo']
			Three = stats.json()['scores'][0]['count_300']
			one = stats.json()['scores'][0]['count_100']
			five = stats.json()['scores'][0]['count_50']
			misses = stats.json()['scores'][0]['count_miss']
			completed = stats.json()['scores'][0]['completed']
			ranked = stats.json()['scores'][0]['beatmap']['ranked']
			ar = stats.json()['scores'][0]['beatmap']['ar']
			od = stats.json()['scores'][0]['beatmap']['od']
			time = stats.json()['scores'][0]['time']

			if 'Z' in time:
				timee = time.replace('T',' ')
				currenttime = timee.replace('Z',' ')

			if ranked == 2:
				status = 'Yes'
			else:
				status = 'No'

			if mods == 0:
				modsletters = 'NM'
			else:
				modsletters = config.readableMods(mods)

			if 'NC' in modsletters:
				modsCheck = modsletters.replace('DT','')
			else:
				modsCheck = modsletters

			if completed == 3:
				msgcompleted = 'Yes'
			else:
				msgcompleted = 'No'

			userid = userinfo.json()['id']
			username = userinfo.json()['username']

			await ctx.send(f'Top osu! Taiko Play for {username}')
			embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR:{ar} OD:{od}] ▸ {accuracy}%\n▸ {score} ▸ {combo}x/{beatmapcombo}x ▸ [{Three}/{one}/{five}/{misses}]\n▸ Map Completed: {msgcompleted}', color=0xb6ebf1)
			embed.set_author(name=f"{mapname} +{modsCheck} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmapid}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
			embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapsetid}l.jpg")
			embed.set_footer(text=f"This score was set on {currenttime}")
			await ctx.send(embed=embed)

	@commands.command()
	async def relaxtaikotop(self, ctx, *args):
		yo = len(args)

		if yo == 0:
			
			u = collation.find_one({"_id": ctx.message.author.id})
			ouo = u['name']
			omg = str(ouo)
		
			stats = requests.get(f'https://akatsuki.pw/api/v1/users/scores/best?rx=1&name={omg}&mode=1')
			if not stats:
				await ctx.send(f'Couldnt find user {omg}!')
			else:
				userinfo = requests.get(f'https://akatsuki.pw/api/v1/users?name={omg}')
			if not userinfo:
				await ctx.send(f'Couldnt find user {omg}!')
			else:
				acc = stats.json()['scores'][0]['accuracy']
			accuracy = round(acc, 2)
			mapname = stats.json()['scores'][0]['beatmap']['song_name']
			beatmapid = stats.json()['scores'][0]['beatmap']['beatmap_id']
			beatmapsetid = stats.json()['scores'][0]['beatmap']['beatmapset_id']
			mods = stats.json()['scores'][0]['mods']
			setdifficulty = stats.json()['scores'][0]['beatmap']['difficulty2']['taiko']
			difficulty = round(setdifficulty, 2)
			rank = stats.json()['scores'][0]['rank']
			ppp = stats.json()['scores'][0]['pp']
			pp = round(ppp, 2)
			score = stats.json()['scores'][0]['score']
			combo = stats.json()['scores'][0]['max_combo']
			beatmapcombo = stats.json()['scores'][0]['beatmap']['max_combo']
			Three = stats.json()['scores'][0]['count_300']
			one = stats.json()['scores'][0]['count_100']
			five = stats.json()['scores'][0]['count_50']
			misses = stats.json()['scores'][0]['count_miss']
			completed = stats.json()['scores'][0]['completed']
			ranked = stats.json()['scores'][0]['beatmap']['ranked']
			ar = stats.json()['scores'][0]['beatmap']['ar']
			od = stats.json()['scores'][0]['beatmap']['od']
			time = stats.json()['scores'][0]['time']

			if 'Z' in time:
				timee = time.replace('T',' ')
				currenttime = timee.replace('Z',' ')

			if ranked == 2:
				status = 'Yes'
			else:
				status = 'No'

			if mods == 0:
				modsletters = 'NM'
			else:
				modsletters = config.readableMods(mods)

			if 'NC' in modsletters:
				modsCheck = modsletters.replace('DT','')
			else:
				modsCheck = modsletters

			if completed == 3:
				msgcompleted = 'Yes'
			else:
				msgcompleted = 'No'

			userid = userinfo.json()['id']
			username = userinfo.json()['username']

			await ctx.send(f'Top osu! Standard Play for {username}')
			embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR:{ar} OD:{od}] ▸ {accuracy}%\n▸ {score} ▸ {combo}x/{beatmapcombo}x ▸ [{Three}/{one}/{five}/{misses}]\n▸ Map Completed: {msgcompleted}', color=0xb6ebf1)
			embed.set_author(name=f"{mapname} +{modsCheck} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmapid}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
			embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapsetid}l.jpg")
			embed.set_footer(text=f"This score was set on {currenttime}")
			await ctx.send(embed=embed)
		else:
			msg = '{}'.format(' '.join(args))

			stats = requests.get(f'https://akatsuki.pw/api/v1/users/scores/best?rx=0&name={msg}&mode=0')
			if not stats:
				await ctx.send(f'Couldnt find user {msg}!')
			else:
				userinfo = requests.get(f'https://akatsuki.pw/api/v1/users?name={msg}')
			if not userinfo:
				await ctx.send(f'Couldnt find user {msg}!')
			else:
				acc = stats.json()['scores'][0]['accuracy']
			accuracy = round(acc, 2)
			mapname = stats.json()['scores'][0]['beatmap']['song_name']
			beatmapid = stats.json()['scores'][0]['beatmap']['beatmap_id']
			beatmapsetid = stats.json()['scores'][0]['beatmap']['beatmapset_id']
			mods = stats.json()['scores'][0]['mods']
			setdifficulty = stats.json()['scores'][0]['beatmap']['difficulty']
			difficulty = round(setdifficulty, 2)
			rank = stats.json()['scores'][0]['rank']
			ppp = stats.json()['scores'][0]['pp']
			pp = round(ppp, 2)
			score = stats.json()['scores'][0]['score']
			combo = stats.json()['scores'][0]['max_combo']
			beatmapcombo = stats.json()['scores'][0]['beatmap']['max_combo']
			Three = stats.json()['scores'][0]['count_300']
			one = stats.json()['scores'][0]['count_100']
			five = stats.json()['scores'][0]['count_50']
			misses = stats.json()['scores'][0]['count_miss']
			completed = stats.json()['scores'][0]['completed']
			ranked = stats.json()['scores'][0]['beatmap']['ranked']
			ar = stats.json()['scores'][0]['beatmap']['ar']
			od = stats.json()['scores'][0]['beatmap']['od']
			time = stats.json()['scores'][0]['time']

			if 'Z' in time:
				timee = time.replace('T',' ')
				currenttime = timee.replace('Z',' ')

			if ranked == 2:
				status = 'Yes'
			else:
				status = 'No'

			if mods == 0:
				modsletters = 'NM'
			else:
				modsletters = config.readableMods(mods)

			if 'NC' in modsletters:
				modsCheck = modsletters.replace('DT','')
			else:
				modsCheck = modsletters

			if completed == 3:
				msgcompleted = 'Yes'
			else:
				msgcompleted = 'No'

			userid = userinfo.json()['id']
			username = userinfo.json()['username']

			await ctx.send(f'Top osu! Standard Play for {username}')
			embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR:{ar} OD:{od}] ▸ {accuracy}%\n▸ {score} ▸ {combo}x/{beatmapcombo}x ▸ [{Three}/{one}/{five}/{misses}]\n▸ Map Completed: {msgcompleted}', color=0xb6ebf1)
			embed.set_author(name=f"{mapname} +{modsCheck} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmapid}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
			embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapsetid}l.jpg")
			embed.set_footer(text=f"This score was set on {currenttime}")
			await ctx.send(embed=embed)

	@commands.command()
	async def relaxtaikorecent(self, ctx, *args):
		yo = len(args)

		if yo == 0:
			
			u = collation.find_one({"_id": ctx.message.author.id})
			ouo = u['name']
			omg = str(ouo)
		
			stats = requests.get(f'https://akatsuki.pw/api/v1/users/scores/recent?rx=1&name={omg}&mode=1')
			if not stats:
				await ctx.send(f'Couldnt find user {omg}!')
			else:
				userinfo = requests.get(f'https://akatsuki.pw/api/v1/users?name={omg}')
			if not userinfo:
				await ctx.send(f'Couldnt find user {omg}!')
			else:
				acc = stats.json()['scores'][0]['accuracy']
			accuracy = round(acc, 2)
			mapname = stats.json()['scores'][0]['beatmap']['song_name']
			beatmapid = stats.json()['scores'][0]['beatmap']['beatmap_id']
			beatmapsetid = stats.json()['scores'][0]['beatmap']['beatmapset_id']
			mods = stats.json()['scores'][0]['mods']
			setdifficulty = stats.json()['scores'][0]['beatmap']['difficulty2']['taiko']
			difficulty = round(setdifficulty, 2)
			rank = stats.json()['scores'][0]['rank']
			ppp = stats.json()['scores'][0]['pp']
			pp = round(ppp, 2)
			score = stats.json()['scores'][0]['score']
			combo = stats.json()['scores'][0]['max_combo']
			beatmapcombo = stats.json()['scores'][0]['beatmap']['max_combo']
			Three = stats.json()['scores'][0]['count_300']
			one = stats.json()['scores'][0]['count_100']
			five = stats.json()['scores'][0]['count_50']
			misses = stats.json()['scores'][0]['count_miss']
			completed = stats.json()['scores'][0]['completed']
			ranked = stats.json()['scores'][0]['beatmap']['ranked']
			ar = stats.json()['scores'][0]['beatmap']['ar']
			od = stats.json()['scores'][0]['beatmap']['od']
			time = stats.json()['scores'][0]['time']

			if 'Z' in time:
				timee = time.replace('T',' ')
				currenttime = timee.replace('Z',' ')

			if ranked == 2:
				status = 'Yes'
			else:
				status = 'No'

			if mods == 0:
				modsletters = 'NM'
			else:
				modsletters = config.readableMods(mods)

			if 'NC' in modsletters:
				modsCheck = modsletters.replace('DT','')
			else:
				modsCheck = modsletters

			if completed == 3:
				msgcompleted = 'Yes'
			else:
				msgcompleted = 'No'

			userid = userinfo.json()['id']
			username = userinfo.json()['username']

			await ctx.send(f'Recent osu! Relax Taiko Play for {username}')
			embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR:{ar} OD:{od}] ▸ {accuracy}%\n▸ {score} ▸ {combo}x/{beatmapcombo}x ▸ [{Three}/{one}/{five}/{misses}]\n▸ Map Completed: {msgcompleted}', color=0xb6ebf1)
			embed.set_author(name=f"{mapname} +{modsCheck} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmapid}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
			embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapsetid}l.jpg")
			embed.set_footer(text=f"This score was set on {currenttime}")
			await ctx.send(embed=embed)
		else:
			msg = '{}'.format(' '.join(args))

			stats = requests.get(f'https://akatsuki.pw/api/v1/users/scores/recent?rx=1&name={msg}&mode=1')
			if not stats:
				await ctx.send(f'Couldnt find user {msg}!')
			else:
				userinfo = requests.get(f'https://akatsuki.pw/api/v1/users?name={msg}')
			if not userinfo:
				await ctx.send(f'Couldnt find user {msg}!')
			else:
				acc = stats.json()['scores'][0]['accuracy']
			accuracy = round(acc, 2)
			mapname = stats.json()['scores'][0]['beatmap']['song_name']
			beatmapid = stats.json()['scores'][0]['beatmap']['beatmap_id']
			beatmapsetid = stats.json()['scores'][0]['beatmap']['beatmapset_id']
			mods = stats.json()['scores'][0]['mods']
			setdifficulty = stats.json()['scores'][0]['beatmap']['difficulty']
			difficulty = round(setdifficulty, 2)
			rank = stats.json()['scores'][0]['rank']
			ppp = stats.json()['scores'][0]['pp']
			pp = round(ppp, 2)
			score = stats.json()['scores'][0]['score']
			combo = stats.json()['scores'][0]['max_combo']
			beatmapcombo = stats.json()['scores'][0]['beatmap']['max_combo']
			Three = stats.json()['scores'][0]['count_300']
			one = stats.json()['scores'][0]['count_100']
			five = stats.json()['scores'][0]['count_50']
			misses = stats.json()['scores'][0]['count_miss']
			completed = stats.json()['scores'][0]['completed']
			ranked = stats.json()['scores'][0]['beatmap']['ranked']
			ar = stats.json()['scores'][0]['beatmap']['ar']
			od = stats.json()['scores'][0]['beatmap']['od']
			time = stats.json()['scores'][0]['time']

			if 'Z' in time:
				timee = time.replace('T',' ')
				currenttime = timee.replace('Z',' ')

			if ranked == 2:
				status = 'Yes'
			else:
				status = 'No'

			if mods == 0:
				modsletters = 'NM'
			else:
				modsletters = config.readableMods(mods)

			if 'NC' in modsletters:
				modsCheck = modsletters.replace('DT','')
			else:
				modsCheck = modsletters

			if completed == 3:
				msgcompleted = 'Yes'
			else:
				msgcompleted = 'No'

			userid = userinfo.json()['id']
			username = userinfo.json()['username']

			await ctx.send(f'Top osu! Standard Play for {username}')
			embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR:{ar} OD:{od}] ▸ {accuracy}%\n▸ {score} ▸ {combo}x/{beatmapcombo}x ▸ [{Three}/{one}/{five}/{misses}]\n▸ Map Completed: {msgcompleted}', color=0xb6ebf1)
			embed.set_author(name=f"{mapname} +{modsCheck} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmapid}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
			embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapsetid}l.jpg")
			embed.set_footer(text=f"This score was set on {currenttime}")
			await ctx.send(embed=embed)

	@commands.command()
	async def taikorecent(self, ctx, *args):
		yo = len(args)

		if yo == 0:
			
			u = collation.find_one({"_id": ctx.message.author.id})
			ouo = u['name']
			omg = str(ouo)
		
			stats = requests.get(f'https://akatsuki.pw/api/v1/users/scores/recent?rx=0&name={omg}&mode=1')
			if not stats:
				await ctx.send(f'Couldnt find user {omg}!')
			else:
				userinfo = requests.get(f'https://akatsuki.pw/api/v1/users?name={omg}')
			if not userinfo:
				await ctx.send(f'Couldnt find user {omg}!')
			else:
				acc = stats.json()['scores'][0]['accuracy']
			accuracy = round(acc, 2)
			mapname = stats.json()['scores'][0]['beatmap']['song_name']
			beatmapid = stats.json()['scores'][0]['beatmap']['beatmap_id']
			beatmapsetid = stats.json()['scores'][0]['beatmap']['beatmapset_id']
			mods = stats.json()['scores'][0]['mods']
			setdifficulty = stats.json()['scores'][0]['beatmap']['difficulty2']['taiko']
			difficulty = round(setdifficulty, 2)
			rank = stats.json()['scores'][0]['rank']
			ppp = stats.json()['scores'][0]['pp']
			pp = round(ppp, 2)
			score = stats.json()['scores'][0]['score']
			combo = stats.json()['scores'][0]['max_combo']
			beatmapcombo = stats.json()['scores'][0]['beatmap']['max_combo']
			Three = stats.json()['scores'][0]['count_300']
			one = stats.json()['scores'][0]['count_100']
			five = stats.json()['scores'][0]['count_50']
			misses = stats.json()['scores'][0]['count_miss']
			completed = stats.json()['scores'][0]['completed']
			ranked = stats.json()['scores'][0]['beatmap']['ranked']
			ar = stats.json()['scores'][0]['beatmap']['ar']
			od = stats.json()['scores'][0]['beatmap']['od']
			time = stats.json()['scores'][0]['time']

			if 'Z' in time:
				timee = time.replace('T',' ')
				currenttime = timee.replace('Z',' ')

			if ranked == 2:
				status = 'Yes'
			else:
				status = 'No'

			if mods == 0:
				modsletters = 'NM'
			else:
				modsletters = config.readableMods(mods)

			if 'NC' in modsletters:
				modsCheck = modsletters.replace('DT','')
			else:
				modsCheck = modsletters

			if completed == 3:
				msgcompleted = 'Yes'
			else:
				msgcompleted = 'No'

			userid = userinfo.json()['id']
			username = userinfo.json()['username']

			await ctx.send(f'Recent osu! Taiko Play for {username}')
			embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR:{ar} OD:{od}] ▸ {accuracy}%\n▸ {score} ▸ {combo}x/{beatmapcombo}x ▸ [{Three}/{one}/{five}/{misses}]\n▸ Map Completed: {msgcompleted}', color=0xb6ebf1)
			embed.set_author(name=f"{mapname} +{modsCheck} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmapid}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
			embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapsetid}l.jpg")
			embed.set_footer(text=f"This score was set on {currenttime}")
			await ctx.send(embed=embed)
		else:
			msg = '{}'.format(' '.join(args))

			stats = requests.get(f'https://akatsuki.pw/api/v1/users/scores/recent?rx=0&name={msg}&mode=1')
			if not stats:
				await ctx.send(f'Couldnt find user {msg}!')
			else:
				userinfo = requests.get(f'https://akatsuki.pw/api/v1/users?name={msg}')
			if not userinfo:
				await ctx.send(f'Couldnt find user {msg}!')
			else:
				acc = stats.json()['scores'][0]['accuracy']
			accuracy = round(acc, 2)
			mapname = stats.json()['scores'][0]['beatmap']['song_name']
			beatmapid = stats.json()['scores'][0]['beatmap']['beatmap_id']
			beatmapsetid = stats.json()['scores'][0]['beatmap']['beatmapset_id']
			mods = stats.json()['scores'][0]['mods']
			setdifficulty = stats.json()['scores'][0]['beatmap']['difficulty']
			difficulty = round(setdifficulty, 2)
			rank = stats.json()['scores'][0]['rank']
			ppp = stats.json()['scores'][0]['pp']
			pp = round(ppp, 2)
			score = stats.json()['scores'][0]['score']
			combo = stats.json()['scores'][0]['max_combo']
			beatmapcombo = stats.json()['scores'][0]['beatmap']['max_combo']
			Three = stats.json()['scores'][0]['count_300']
			one = stats.json()['scores'][0]['count_100']
			five = stats.json()['scores'][0]['count_50']
			misses = stats.json()['scores'][0]['count_miss']
			completed = stats.json()['scores'][0]['completed']
			ranked = stats.json()['scores'][0]['beatmap']['ranked']
			ar = stats.json()['scores'][0]['beatmap']['ar']
			od = stats.json()['scores'][0]['beatmap']['od']
			time = stats.json()['scores'][0]['time']

			if 'Z' in time:
				timee = time.replace('T',' ')
				currenttime = timee.replace('Z',' ')

			if ranked == 2:
				status = 'Yes'
			else:
				status = 'No'

			if mods == 0:
				modsletters = 'NM'
			else:
				modsletters = config.readableMods(mods)

			if 'NC' in modsletters:
				modsCheck = modsletters.replace('DT','')
			else:
				modsCheck = modsletters

			if completed == 3:
				msgcompleted = 'Yes'
			else:
				msgcompleted = 'No'

			userid = userinfo.json()['id']
			username = userinfo.json()['username']

			await ctx.send(f'Top osu! Standard Play for {username}')
			embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR:{ar} OD:{od}] ▸ {accuracy}%\n▸ {score} ▸ {combo}x/{beatmapcombo}x ▸ [{Three}/{one}/{five}/{misses}]\n▸ Map Completed: {msgcompleted}', color=0xb6ebf1)
			embed.set_author(name=f"{mapname} +{modsCheck} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmapid}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
			embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapsetid}l.jpg")
			embed.set_footer(text=f"This score was set on {currenttime}")
			await ctx.send(embed=embed)

	@commands.command()
	async def reg(self, ctx, *args):
		yo = len(args)

		if yo == 0:
			
			u = collation.find_one({"_id": ctx.message.author.id})
			ouo = u['name']
			omg = str(ouo)
		
			userinfo  = requests.get(f'https://akatsuki.pw/api/v1/users?name={omg}')
			if not userinfo:
				return await ctx.send(f'Couldnt find user {omg}!')
			else:
				userid = userinfo.json()['id']
			stats = requests.get(f"https://akatsuki.pw/api/v1/users/full?id={userid}")
			if not stats:
				await ctx.send(f'Couldnt find user {omg}!')
			else:
				rank = stats.json()['stats'][0]['std']['global_leaderboard_rank']
			countryrank = stats.json()['stats'][0]['std']['country_leaderboard_rank']
			country = stats.json()['country']
			levell = stats.json()['stats'][0]['std']['level']
			level = round(levell, 2)
			acc = stats.json()['stats'][0]['std']['accuracy']
			accuracy = round(acc, 2)
			ppp = stats.json()['stats'][0]['std']['pp']
			pp = round(ppp, 2)
			playcount = stats.json()['stats'][0]['std']['playcount']
			username = stats.json()['username']

			embed=discord.Embed(description=f'▸ Official Rank: {rank} ({country}#{countryrank}) \n▸ Level: {level}\n▸ Total PP: {pp} \n▸ Accuracy: {accuracy}% \n▸ Playcount: {playcount}', color=0xb6ebf1)
			embed.set_author(name=f"osu! Standard Profile for {username}", url=f"https://akatsuki.pw/u/{userid}", icon_url=f"https://avatars0.githubusercontent.com/u/45724130?s=200&v=4.png")
			embed.set_thumbnail(url=f"https://a.akatsuki.pw/{userid}.png")
			embed.set_footer(text=f"Player on Akatsuki!")
			await ctx.send(embed=embed)
		else:
			msg = '{}'.format(' '.join(args))

			userinfo  = requests.get(f'https://akatsuki.pw/api/v1/users?name={msg}')
			if not userinfo:
				return await ctx.send(f'Couldnt find user {msg}!')
			else:
				userid = userinfo.json()['id']
			stats = requests.get(f"https://akatsuki.pw/api/v1/users/full?id={userid}")
			if not stats:
				await ctx.send(f'Couldnt find user {msg}!')
			else:
				rank = stats.json()['stats'][0]['std']['global_leaderboard_rank']
			countryrank = stats.json()['stats'][0]['std']['country_leaderboard_rank']
			country = stats.json()['country']
			levell = stats.json()['stats'][0]['std']['level']
			level = round(levell, 2)
			acc = stats.json()['stats'][0]['std']['accuracy']
			accuracy = round(acc, 2)
			ppp = stats.json()['stats'][0]['std']['pp']
			pp = round(ppp, 2)
			playcount = stats.json()['stats'][0]['std']['playcount']
			username = stats.json()['username']

			embed=discord.Embed(description=f'▸ Official Rank: {rank} ({country}#{countryrank}) \n▸ Level: {level}\n▸ Total PP: {pp} \n▸ Accuracy: {accuracy}% \n▸ Playcount: {playcount}', color=0xb6ebf1)
			embed.set_author(name=f"osu! Standard Profile for {username}", url=f"https://akatsuki.pw/u/{userid}", icon_url=f"https://avatars0.githubusercontent.com/u/45724130?s=200&v=4.png")
			embed.set_thumbnail(url=f"https://a.akatsuki.pw/{userid}.png")
			embed.set_footer(text=f"Player on Akatsuki!")
			await ctx.send(embed=embed)

	@commands.command()
	async def relax(self, ctx, *args):
		yo = len(args)

		if yo == 0:
			
			u = collation.find_one({"_id": ctx.message.author.id})
			ouo = u['name']
			omg = str(ouo)
		
			userinfo  = requests.get(f'https://akatsuki.pw/api/v1/users?name={omg}')
			if not userinfo:
				return await ctx.send(f'Couldnt find user {omg}!')
			else:
				userid = userinfo.json()['id']
			stats = requests.get(f"https://akatsuki.pw/api/v1/users/full?id={userid}")
			if not stats:
				await ctx.send(f'Couldnt find user {omg}!')
			else:
				rank = stats.json()['stats'][1]['std']['global_leaderboard_rank']
			countryrank = stats.json()['stats'][1]['std']['country_leaderboard_rank']
			country = stats.json()['country']
			levell = stats.json()['stats'][1]['std']['level']
			level = round(levell, 2)
			acc = stats.json()['stats'][1]['std']['accuracy']
			accuracy = round(acc, 2)
			ppp = stats.json()['stats'][1]['std']['pp']
			pp = round(ppp, 2)
			playcount = stats.json()['stats'][1]['std']['playcount']
			username = stats.json()['username']

			embed=discord.Embed(description=f'▸ Official Rank: {rank} ({country}#{countryrank}) \n▸ Level: {level}\n▸ Total PP: {pp} \n▸ Accuracy: {accuracy}% \n▸ Playcount: {playcount}', color=0xb6ebf1)
			embed.set_author(name=f"osu! Relax Standard Profile for {username}", url=f"https://akatsuki.pw/u/{userid}", icon_url=f"https://avatars0.githubusercontent.com/u/45724130?s=200&v=4.png")
			embed.set_thumbnail(url=f"https://a.akatsuki.pw/{userid}.png")
			embed.set_footer(text=f"Player on Akatsuki!")
			await ctx.send(embed=embed)	
		else:
			msg = '{}'.format(' '.join(args))

			userinfo  = requests.get(f'https://akatsuki.pw/api/v1/users?name={msg}')
			if not userinfo:
				return await ctx.send(f'Couldnt find user {msg}!')
			else:
				userid = userinfo.json()['id']
			stats = requests.get(f"https://akatsuki.pw/api/v1/users/full?id={userid}")
			if not stats:
				await ctx.send(f'Couldnt find user {msg}!')
			else:
				rank = stats.json()['stats'][1]['std']['global_leaderboard_rank']
			countryrank = stats.json()['stats'][1]['std']['country_leaderboard_rank']
			country = stats.json()['country']
			levell = stats.json()['stats'][1]['std']['level']
			level = round(levell, 2)
			acc = stats.json()['stats'][1]['std']['accuracy']
			accuracy = round(acc, 2)
			ppp = stats.json()['stats'][1]['std']['pp']
			pp = round(ppp, 2)
			playcount = stats.json()['stats'][1]['std']['playcount']
			username = stats.json()['username']

			embed=discord.Embed(description=f'▸ Official Rank: {rank} ({country}#{countryrank}) \n▸ Level: {level}\n▸ Total PP: {pp} \n▸ Accuracy: {accuracy}% \n▸ Playcount: {playcount}', color=0xb6ebf1)
			embed.set_author(name=f"osu! Relax Standard Profile for {username}", url=f"https://akatsuki.pw/u/{userid}", icon_url=f"https://avatars0.githubusercontent.com/u/45724130?s=200&v=4.png")
			embed.set_thumbnail(url=f"https://a.akatsuki.pw/{userid}.png")
			embed.set_footer(text=f"Player on Akatsuki!")
			await ctx.send(embed=embed)

	@commands.command()
	async def relaxtaiko(self, ctx, *args):

		yo = len(args)

		if yo == 0:
			
			u = collation.find_one({"_id": ctx.message.author.id})
			ouo = u['name']
			omg = str(ouo)

			userinfo  = requests.get(f'https://akatsuki.pw/api/v1/users?name={omg}')
			if not userinfo:
				return await ctx.send(f'Couldnt find user {omg}!')
			else:
				userid = userinfo.json()['id']
			stats = requests.get(f"https://akatsuki.pw/api/v1/users/full?id={userid}")
			if not stats:
				await ctx.send(f'Couldnt find user {omg}!')
			else:
				rank = stats.json()['stats'][1]['taiko']['global_leaderboard_rank']
			countryrank = stats.json()['stats'][1]['taiko']['country_leaderboard_rank']
			country = stats.json()['country']
			levell = stats.json()['stats'][1]['taiko']['level']
			level = round(levell, 2)
			acc = stats.json()['stats'][1]['taiko']['accuracy']
			accuracy = round(acc, 2)
			ppp = stats.json()['stats'][1]['taiko']['pp']
			pp = round(ppp, 2)
			playcount = stats.json()['stats'][1]['taiko']['playcount']
			username = stats.json()['username']

			embed=discord.Embed(description=f'▸ Official Rank: {rank} ({country}#{countryrank}) \n▸ Level: {level}\n▸ Total PP: {pp} \n▸ Accuracy: {accuracy}% \n▸ Playcount: {playcount}', color=0xb6ebf1)
			embed.set_author(name=f"osu! Relax Taiko Profile for {username}", url=f"https://akatsuki.pw/u/{userid}", icon_url=f"https://avatars0.githubusercontent.com/u/45724130?s=200&v=4.png")
			embed.set_thumbnail(url=f"https://a.akatsuki.pw/{userid}.png")
			embed.set_footer(text=f"Player on Akatsuki!")
			await ctx.send(embed=embed)	
		else:
			msg = '{}'.format(' '.join(args))

			userinfo  = requests.get(f'https://akatsuki.pw/api/v1/users?name={msg}')
			if not userinfo:
				return await ctx.send(f'Couldnt find user {msg}!')
			else:
				userid = userinfo.json()['id']
			stats = requests.get(f"https://akatsuki.pw/api/v1/users/full?id={userid}")
			if not stats:
				await ctx.send(f'Couldnt find user {msg}!')
			else:
				rank = stats.json()['stats'][1]['taiko']['global_leaderboard_rank']
			countryrank = stats.json()['stats'][1]['taiko']['country_leaderboard_rank']
			country = stats.json()['country']
			levell = stats.json()['stats'][1]['taiko']['level']
			level = round(levell, 2)
			acc = stats.json()['stats'][1]['taiko']['accuracy']
			accuracy = round(acc, 2)
			ppp = stats.json()['stats'][1]['taiko']['pp']
			pp = round(ppp, 2)
			playcount = stats.json()['stats'][1]['taiko']['playcount']
			username = stats.json()['username']

			embed=discord.Embed(description=f'▸ Official Rank: {rank} ({country}#{countryrank}) \n▸ Level: {level}\n▸ Total PP: {pp} \n▸ Accuracy: {accuracy}% \n▸ Playcount: {playcount}', color=0xb6ebf1)
			embed.set_author(name=f"osu! Relax Taiko Profile for {username}", url=f"https://akatsuki.pw/u/{userid}", icon_url=f"https://avatars0.githubusercontent.com/u/45724130?s=200&v=4.png")
			embed.set_thumbnail(url=f"https://a.akatsuki.pw/{userid}.png")
			embed.set_footer(text=f"Player on Akatsuki!")
			await ctx.send(embed=embed)

	@commands.command()
	async def taiko(self, ctx, *args):
		yo = len(args)

		if yo == 0:
			
			u = collation.find_one({"_id": ctx.message.author.id})
			ouo = u['name']
			omg = str(ouo)

			userinfo  = requests.get(f'https://akatsuki.pw/api/v1/users?name={omg}')
			if not userinfo:
				return await ctx.send(f'Couldnt find user {omg}!')
			else:
				userid = userinfo.json()['id']
			stats = requests.get(f"https://akatsuki.pw/api/v1/users/full?id={userid}")
			if not stats:
				await ctx.send(f'Couldnt find user {omg}!')
			else:
				rank = stats.json()['stats'][0]['taiko']['global_leaderboard_rank']
			countryrank = stats.json()['stats'][0]['taiko']['country_leaderboard_rank']
			country = stats.json()['country']
			levell = stats.json()['stats'][0]['taiko']['level']
			level = round(levell, 2)
			acc = stats.json()['stats'][0]['taiko']['accuracy']
			accuracy = round(acc, 2)
			ppp = stats.json()['stats'][0]['taiko']['pp']
			pp = round(ppp, 2)
			playcount = stats.json()['stats'][0]['taiko']['playcount']
			username = stats.json()['username']

			embed=discord.Embed(description=f'▸ Official Rank: {rank} ({country}#{countryrank}) \n▸ Level: {level}\n▸ Total PP: {pp} \n▸ Accuracy: {accuracy}% \n▸ Playcount: {playcount}', color=0xb6ebf1)
			embed.set_author(name=f"osu! Taiko Profile for {username}", url=f"https://akatsuki.pw/u/{userid}", icon_url=f"https://avatars0.githubusercontent.com/u/45724130?s=200&v=4.png")
			embed.set_thumbnail(url=f"https://a.akatsuki.pw/{userid}.png")
			embed.set_footer(text=f"Player on Akatsuki!")
			await ctx.send(embed=embed)
		else:
			msg = '{}'.format(' '.join(args))

			userinfo  = requests.get(f'https://akatsuki.pw/api/v1/users?name={msg}')
			if not userinfo:
				return await ctx.send(f'Couldnt find user {msg}!')
			else:
				userid = userinfo.json()['id']
			stats = requests.get(f"https://akatsuki.pw/api/v1/users/full?id={userid}")
			if not stats:
				await ctx.send(f'Couldnt find user {msg}!')
			else:
				rank = stats.json()['stats'][0]['taiko']['global_leaderboard_rank']
			countryrank = stats.json()['stats'][0]['taiko']['country_leaderboard_rank']
			country = stats.json()['country']
			levell = stats.json()['stats'][0]['taiko']['level']
			level = round(levell, 2)
			acc = stats.json()['stats'][0]['taiko']['accuracy']
			accuracy = round(acc, 2)
			ppp = stats.json()['stats'][0]['taiko']['pp']
			pp = round(ppp, 2)
			playcount = stats.json()['stats'][0]['taiko']['playcount']
			username = stats.json()['username']

			embed=discord.Embed(description=f'▸ Official Rank: {rank} ({country}#{countryrank}) \n▸ Level: {level}\n▸ Total PP: {pp} \n▸ Accuracy: {accuracy}% \n▸ Playcount: {playcount}', color=0xb6ebf1)
			embed.set_author(name=f"osu! Taiko Profile for {username}", url=f"https://akatsuki.pw/u/{userid}", icon_url=f"https://avatars0.githubusercontent.com/u/45724130?s=200&v=4.png")
			embed.set_thumbnail(url=f"https://a.akatsuki.pw/{userid}.png")
			embed.set_footer(text=f"Player on Akatsuki!")
			await ctx.send(embed=embed)

def setup(client):
	client.add_cog(Akatsuki(client))
import discord
import config
import requests
import random
from discord.ext import commands
import enum
import pymongo
from pymongo import *
from enum import IntEnum

cluster = pymongo.MongoClient(f'mongodb+srv://Cover:{config.dbpassword}@chiyo-y6grb.mongodb.net/{config.dbname}?retryWrites=true&w=majority')
db = cluster['Akatsuki']
collation = db['Akatsuki']

class extra(commands.Cog):

	def __init___(self, client):
		self.client = client

	@commands.command()
	async def about(self, ctx):
		await ctx.send('https://coverosu.tk/chiyo')

	@commands.command()
	async def roll(self, ctx):
		number = random.randint(1, 100)
		await ctx.send(f'{number} out of 100')

	@commands.command()
	async def connect(self, ctx, *, arg):

		b = collation.find_one({"_id": ctx.message.author.id})
		yoo = print(b)

		if b == yoo:
			post = {"_id": ctx.message.author.id, "name": arg}
			collation.insert_one(post)
			await ctx.send(f'User {arg} was connected to your discord account!')
		else:
			newvalues = { "$set": { "name": arg } }
			collation.update_one(b, newvalues)
			await ctx.send(f'User {arg} was connected to your discord account!')

	@commands.command()
	async def slots(self, ctx, *args):

		h = ['🍎','🍊','🍐','🍋','🍉','🍇','🍓','🍒']

		b = random.choice(h)
		c = random.choice(h)
		d = random.choice(h)

		if b == c == d:
			return await ctx.send(f'[{b}{c}{d}] \n 3/3!')
		elif b == c or b == d or c == b or c == d or d == b or d == c:
			return await ctx.send(f'[{b}{c}{d}] \n 2/3!')
		else:
			return await ctx.send(f'[{b}{c}{d}] \n lol you suck')
			
def setup(client):
	client.add_cog(extra(client))
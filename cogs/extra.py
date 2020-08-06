import discord
from discord.ext import commands
import requests
import os
import akatsukiapi
import Chiyo

collation = Chiyo.collation

class Extra(commands.Cog):

    def __int__(self, client):
        self.client = client

    @commands.command()
    async def connect(self, ctx, *args):
    	if len(args) == 0:
    		return await ctx.send('You must provide an argument!!')
    	msg = '{}'.format(' '.join(args))
    	b = collation.find_one({"_id": ctx.message.author.id})
    	
    	if b == None:
    		d = requests.get(f'https://akatsuki.pw/api/v1/users/full?name={msg}')
    		if not d:
    			return await ctx.send(f'{msg} is not a valid user!!')
    		post = {"_id": ctx.message.author.id, "name": msg}
    		collation.insert_one(post)
    		return await ctx.send(f'User {msg} was connected to your discord account!')
    	else:
    		d = requests.get(f'https://akatsuki.pw/api/v1/users/full?name={msg}')
    		if not d:
    			return await ctx.send(f'{msg} is not a valid user!!')
    		newvalues = { "$set": { "name": msg } }
    		collation.update_one(b, newvalues)
    		return await ctx.send(f'User {msg} was connected to your discord account!')

    @commands.command()
    async def about(self, ctx):
        await ctx.send('https://coverosu.tk/chiyo')

    @commands.command()
    async def roll(self, ctx, *args):
        number = random.randint(1, 100)
        await ctx.send(f'{number} out of 100 <@!{ctx.message.author.id}>')

    @commands.command()
    async def slots(self, ctx, *args):

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


def setup(client):
    client.add_cog(Extra(client))

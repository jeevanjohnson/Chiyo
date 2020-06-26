import discord
import os
from discord.ext import commands
import datetime
import time 
import requests
import json
import subprocess
import typing
import random
import enum
from enum import IntEnum

class Mods(IntEnum):
    NOMOD = 0
    NOFAIL = 1 << 0
    EASY = 1 << 1
    TOUCHSCREEN = 1 << 2
    HIDDEN = 1 << 3
    HARDROCK = 1 << 4
    SUDDENDEATH = 1 << 5
    DOUBLETIME = 1 << 6
    RELAX = 1 << 7
    HALFTIME = 1 << 8
    NIGHTCORE = 1 << 9
    FLASHLIGHT = 1 << 10
    AUTOPLAY = 1 << 11
    SPUNOUT = 1 << 12
    RELAX2 = 1 << 13
    PERFECT = 1 << 14
    KEY4 = 1 << 15
    KEY5 = 1 << 16
    KEY6 = 1 << 17
    KEY7 = 1 << 18
    KEY8 = 1 << 19
    KEYMOD = 1 << 20
    FADEIN = 1 << 21
    RANDOM = 1 << 22
    LASTMOD = 1 << 23
    KEY9 = 1 << 24
    KEY10 = 1 << 25
    KEY1 = 1 << 26
    KEY3 = 1 << 27
    KEY2 = 1 << 28
    SCOREV2 = 1 << 29

def readableMods(m: int) -> str:
    """
    Return a string with readable std mods.
    Used to convert a mods number for oppai

    :param m: mods bitwise number
    :return: readable mods string, eg HDDT
    """

    if not m: return ''

    r: List[str] = []
    if m & Mods.NOFAIL:      r.append('NF')
    if m & Mods.EASY:        r.append('EZ')
    if m & Mods.TOUCHSCREEN: r.append('TD')
    if m & Mods.HIDDEN:      r.append('HD')
    if m & Mods.HARDROCK:    r.append('HR')
    if m & Mods.DOUBLETIME:  r.append('DT')
    if m & Mods.RELAX:       r.append('RX')
    if m & Mods.HALFTIME:    r.append('HT')
    if m & Mods.NIGHTCORE:   r.append('NC')
    if m & Mods.FLASHLIGHT:  r.append('FL')
    if m & Mods.SPUNOUT:     r.append('SO')
    if m & Mods.SCOREV2:     r.append('V2')
    return ''.join(r)


class test(commands.Cog):

	def __init___(self, client):
		self.client = client

	@commands.command()
	async def relax(self, ctx, *, arg):
	  getakatsukiprofile = requests.get(f"https://akatsuki.pw/api/get_user?u={arg}&m=0")
	  if not getakatsukiprofile:
	    return await ctx.send(f'Couldnt find user!')
	  else:
	    userid = getakatsukiprofile.json()[0]['user_id']

	  getprofile = requests.get(f"https://akatsuki.pw/api/v1/users/full?id={userid}")
	  if not getprofile:
	    return await ctx.send('Akatsuki api error! :c')
	  else:
	    name = getprofile.json()['username']
	    registered = getprofile.json()['registered_on']
	    country = getprofile.json()['country']
	    rank = getprofile.json()['stats'][1]['std']['global_leaderboard_rank']
	    countryrank = getprofile.json()['stats'][1]['std']['country_leaderboard_rank']
	    pp = getprofile.json()['stats'][1]['std']['pp']
	    acc = getprofile.json()['stats'][1]['std']['accuracy']
	    owo = round(acc, 2)
	    playcount = getprofile.json()['stats'][1]['std']['playcount']
	    clantag = getprofile.json()['clan']['name']

	    if clantag == "":
	      clannnnn = 'Not in a clan'
	    else:
	      clannnnn = clantag

	  embed=discord.Embed()
	  embed=discord.Embed(title=f"Relax Stats for {name}", url=f"https://akatsuki.pw/rx/u/{userid}?mode=0", color=0xb6ebf1)
	  embed.set_thumbnail(url=f"https://a.akatsuki.pw/{userid}")
	  embed.add_field(name="Country Ranking:", value=f"Rank ``{countryrank}`` in ``{country}``", inline=True)
	  embed.add_field(name="Global Rank:", value=f"``{rank}``", inline=True)
	  embed.add_field(name="PP:", value=f"``{pp}``", inline=True)
	  embed.add_field(name="Acc:", value=f"``{owo}%``", inline=True)
	  embed.add_field(name="Playcount:", value=f"``{playcount}``", inline=True)
	  embed.add_field(name="Clan:", value=f"``{clannnnn}``", inline=True)
	  embed.set_footer(text=f"This user was created at {registered}")
	  await ctx.send(embed=embed)


def setup(client):
	client.add_cog(test(client))
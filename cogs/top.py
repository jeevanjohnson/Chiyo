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
	async def top(self, ctx, *, arg):
	  
	  akatsukirequestid = requests.get(f"https://akatsuki.pw/api/v1/users/whatid?name={arg}")
	  if not akatsukirequestid:
	    await ctx.send("Couldnt find this user!")
	  else:
	    userid = akatsukirequestid.json()['id']
	  rrecent = requests.get(f"https://akatsuki.pw/api/v1/users/scores/best?rx=0&name={arg}&mode=0")
	  if not rrecent:
	    return await ctx.send(f'failed while finding recent score for {arg}') # return will stop execution of the function here, so you dont need the else: and tab
	  else:
	    rcrank = rrecent.json()['scores'][0]['rank'] # notice how 0 is an int and not a string, since indices for a set are integers, only indices for a dictionary are strings usually
	  rcmapid = rrecent.json()['scores'][0]['beatmap']['beatmap_id']
	  recentcombo = rrecent.json()['scores'][0]['max_combo']
	  pp = rrecent.json()['scores'][0]['pp']
	  rcpp = round(pp)
	  rcacc = rrecent.json()['scores'][0]['accuracy']
	  owo = round(rcacc, 2)
	  rcmisses = rrecent.json()['scores'][0]['count_miss']
	  rcmods = rrecent.json()['scores'][0]['mods']

	  if rcmods == 0:
	    osuhow = 'NM'
	  else:
	    osuhow = readableMods(rcmods)

	  rctime = rrecent.json()['scores'][0]['time']
	  fullcombo = rrecent.json()['scores'][0]['full_combo']
	  completed = rrecent.json()['scores'][0]['completed']
	  songname = rrecent.json()['scores'][0]['beatmap']['song_name']

	  if completed == 3:
	    uwu = 'Yes'
	  else:
	    uwu = 'No'

	  name = requests.get(f"https://akatsuki.pw/api/get_user?u={arg}")
	  if not name:
	    return
	  else:
	    nameName = name.json()[0]['username']

	  beatmaprecent = requests.get(f"https://akatsuki.pw/api/get_beatmaps?limit=1&m=0&b={rcmapid}")
	  if not beatmaprecent:
	    return await ctx.send('Akatsuki api error! :c')
	  else:  
	    beatmaprc = beatmaprecent.json()[0]['beatmapset_id']
	  beatmapnamerc = beatmaprecent.json()[0]['title']
	  beatmapcombo = beatmaprecent.json()[0]['max_combo']
	  beatmapartrc = beatmaprecent.json()[0]['artist']

	  embed=discord.Embed()
	  embed=discord.Embed(title=f"{songname}", url=f"https://akatsuki.pw/b/{rcmapid}", color=0xb6ebf1)
	  embed.set_author(name=f"Recent for {nameName}", url=f"https://akatsuki.pw/u/{userid}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
	  embed.add_field(name="Combo:", value=f"``{recentcombo}x/{beatmapcombo}x``", inline=True)
	  embed.add_field(name="FC?:", value=f"``{fullcombo}``", inline=True)
	  embed.add_field(name="Misses:", value=f"``{rcmisses}``", inline=True)
	  embed.add_field(name="Rank:", value=f"``{rcrank}``", inline=True)
	  embed.add_field(name="PP:", value=f"``{rcpp}``", inline=True)
	  embed.add_field(name="Acc:", value=f"``{owo}``", inline=True)
	  embed.add_field(name="Map Completed?", value=f"``{uwu}``", inline=True)
	  embed.add_field(name="Mods:", value=f"``{osuhow}``", inline=True)
	  embed.set_image(url=f"https://assets.ppy.sh/beatmaps/{beatmaprc}/covers/cover.jpg")
	  embed.set_footer(text=f"This play was set on {rctime}")
	  await ctx.send(embed=embed)


def setup(client):
	client.add_cog(test(client))
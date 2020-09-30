import requests
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
	d = ''.join(r)
	return d.replace('DT','') if 'NC' in d else d

def get_id(username):
	w = requests.get(f'https://akatsuki.pw/api/v1/users/whatid?name={username}')
	if not w:
		return "Couldn't find user!"
	return w.json()['id']

def get_username(userid):
	w = requests.get(f'https://akatsuki.pw/api/v1/users/full?id={userid}')
	if not w:
		return "Couldn't find user!"
	return w.json()['username']

def get_beatmap(beatmapid, mode):

	params = {
		'limit': 1,
		'b': beatmapid,
		'm': mode
	}

	w = requests.get(f'https://akatsuki.pw/api/get_beatmaps?', params=params)
	if not w:
		return 'error'
	return w.json()[0]

class Helper:

	def __init__(self, userid):
		self.userid = userid

	def top(self, mode = 0, relax = 0, scoreid = 0):

		t = requests.get(f'https://akatsuki.pw/api/v1/users/scores/best?id={self.userid}&rx={relax}&mode={mode}')

		if not t:
			return 'error'
		try:
			return t.json()['scores'][scoreid - 1 if scoreid > 0 else scoreid]
		except:
			return 'error'

	def recent(self, mode = 0, relax = 0, scoreid = 0):

		t = requests.get(f'https://akatsuki.pw/api/v1/users/scores/recent?id={self.userid}&rx={relax}&mode={mode}')

		if not t:
			return 'error'
		try:
			return t.json()['scores'][scoreid - 1 if scoreid > 0 else scoreid]
		except:
			return 'error'

	def compare(self, beatmapid, mode = 0, relax = 0, scoreid = 0):

		info = requests.get(f'https://akatsuki.pw/api/get_scores?b={beatmapid}&m={mode}&u={self.userid}&rx={relax}')
		if not info:
			return 'no score found'
		try:
			return info.json()[scoreid - 1 if scoreid > 0 else scoreid]
		except:
			return 'no score found'

	def profile(self, mode = 0, relax = 0):

		t = requests.get(f'https://akatsuki.pw/api/v1/users/full?id={self.userid}')

		if not t:
			return 'error'

		switcher = {
			0: 'std',
			1: 'taiko',
			2: 'ctb',
			3: 'mania'
		}
		
		#e = Helper(1000)
		#how = e.profile()
		#print(how['stats']['ranked_score'])
		try:
			username = t.json()['username']
			registered_on = t.json()['registered_on'].replace('T',' ').replace('Z','')
			latest_activity = t.json()['latest_activity'].replace('T',' ').replace('Z','')
			country = t.json()['country']
			stats = t.json()['stats'][relax][switcher.get(mode)]
			return {
				'username': username,
				'registered_on': registered_on,
				'latest_activity': latest_activity,
				'country': country,
				'stats': stats
			}
		except:
			return 'error'

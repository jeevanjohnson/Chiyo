from coover import Beatmap
from typing import Union
from enum import IntFlag, unique
import time
import config
import requests

BASE_API = 'https://akatsuki.pw/api/v1'

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

GRADE_URLS = {
    'SSH': 'https://cdn.discordapp.com/emojis/724849277406281728.png?v=1',
    'SH': 'https://cdn.discordapp.com/emojis/724847645142810624.png?v=1',
    'SS': 'https://cdn.discordapp.com/emojis/724849299300548680.png?v=1',
    'S': 'https://cdn.discordapp.com/emojis/724847668953874493.png?v=1',
    'A': 'https://cdn.discordapp.com/emojis/724841194517037137.png?v=1',
    'B': 'https://cdn.discordapp.com/emojis/724841229602521109.png?v=1',
    'C': 'https://cdn.discordapp.com/emojis/724841244530049095.png?v=1',
    'D': 'https://cdn.discordapp.com/emojis/724841263727116379.png?v=1',
    'F': 'https://cdn.discordapp.com/emojis/724841280772898906.png?v=1'
}

@unique
class Mods(IntFlag):
    NOMOD = 0
    NOFAIL = 1 << 0
    EASY = 1 << 1
    TOUCHSCREEN = 1 << 2 # old: 'NOVIDEO'
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
    AUTOPILOT = 1 << 13
    PERFECT = 1 << 14
    KEY4 = 1 << 15
    KEY5 = 1 << 16
    KEY6 = 1 << 17
    KEY7 = 1 << 18
    KEY8 = 1 << 19
    FADEIN = 1 << 20
    RANDOM = 1 << 21
    CINEMA = 1 << 22
    TARGET = 1 << 23
    KEY9 = 1 << 24
    KEYCOOP = 1 << 25
    KEY1 = 1 << 26
    KEY3 = 1 << 27
    KEY2 = 1 << 28
    SCOREV2 = 1 << 29
    MIRROR = 1 << 30

    def __repr__(self) -> str:
        """
        Return a string with readable std mods.
        Used to convert a mods number for oppai
        :param m: mods bitwise number
        :return: readable mods string, eg HDDT
        """

        _mod_dict = {
            Mods.NOFAIL: 'NF',
            Mods.EASY: 'EZ',
            Mods.TOUCHSCREEN: 'TD',
            Mods.HIDDEN: 'HD',
            Mods.HARDROCK: 'HR',
            Mods.SUDDENDEATH: 'SD',
            Mods.DOUBLETIME: 'DT',
            Mods.RELAX: 'RX',
            Mods.HALFTIME: 'HT',
            Mods.NIGHTCORE: 'NC',
            Mods.FLASHLIGHT: 'FL',
            Mods.AUTOPLAY: 'AU',
            Mods.SPUNOUT: 'SO',
            Mods.AUTOPILOT: 'AP',
            Mods.PERFECT: 'PF',
            Mods.KEY4: 'K4',
            Mods.KEY5: 'K5',
            Mods.KEY6: 'K6',
            Mods.KEY7: 'K7',
            Mods.KEY8: 'K8',
            Mods.FADEIN: 'FI',
            Mods.RANDOM: 'RN',
            Mods.CINEMA: 'CN',
            Mods.TARGET: 'TP',
            Mods.KEY9: 'K9',
            Mods.KEYCOOP: 'CO',
            Mods.KEY1: 'K1',
            Mods.KEY3: 'K3',
            Mods.KEY2: 'K2',
            Mods.SCOREV2: 'V2',
            Mods.MIRROR: 'MI'
        }

        if not self:
            return 'NM'

        # dt/nc is a special case, as osu! will send
        # the mods as 'DTNC' while only NC is applied.
        if self & Mods.NIGHTCORE:
            self &= ~Mods.DOUBLETIME

        return ''.join(v for k, v in _mod_dict.items() if self & k)

def log(message, color):
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(f"{current_time}:{color} {message}{bcolors.ENDC}")
    return

GAMEMODES = ('std', 'taiko', 'ctb', 'mania')

def fix_time(_time: str) -> str:
    col = _time.index(':') - 2
    yea = [char for char in _time]
    yea[col] = ' '
    return ''.join(yea)

def map_completion_percentage(beatmapid: int, totalhits: int = 0) -> float:
    if not beatmapid:
        return 0.0
    _beatmap = requests.get(f"https://osu.ppy.sh/osu/{beatmapid}")
    if not _beatmap or _beatmap.status_code != 200:
        return 0.0
    beatmap =  Beatmap(_beatmap.text)
    beatmap.get_hit_objects()
    beatmap_total_objects = len(beatmap.hit_objects)
    if not totalhits:
        totalhits = beatmap_total_objects
    return round((totalhits / beatmap_total_objects * 100), 2)

def calc_acc(mode: int, n300: int, n100: int, n50: int,
             nmiss: int, nkatu: int = 0, ngeki: int = 0) -> float:
    if mode == 0:
        # osu!std
        total = sum((n300, n100, n50, nmiss))

        return 100.0 * sum((
            n300 * 300.0,
            n100 * 100.0,
            n50 * 50.0
        )) / (total * 300.0)

    elif mode == 1:
        # osu!taiko
        total = sum((n300, n100, nmiss))

        return 100.0 * sum((
            n300 * 300.0,
            n100 * 150.0
        )) / (total * 300.0)

    elif mode == 2:
        # osu!catch
        return 0.0

    elif mode == 3:
        # osu!mania
        return 0.0

def get_profile(user: Union[int, str], mode: int = 0, relax: int = 0) -> dict:
    with requests.Session() as sess:
        params = {
            'name' if isinstance(user, str) else 'id': user,
        }
        req = sess.get(f'{BASE_API}/users/full?', params=params)

        if not req or req.status_code != 200 or not (json := req.json()):
            return None
        
        mode = GAMEMODES[mode]

        return {
            'username': json['username'],
            'userid': json['id'],
            'country': json['country'],
            'registered_on': (json['registered_on'].replace('T', ' ').replace('Z',' ')),
            'latest_activity': json['latest_activity'].replace('T', ' ').replace('Z',' '),
            'ranked_score': (stats := json['stats'][relax][mode])['ranked_score'],
            'total_score': stats['total_score'],
            'playcount': stats['playcount'],
            'level': round(float(stats['level']), 2),
            'acc': round(float(stats['accuracy']), 2),
            'pp': round(float(stats['pp']), 2),
            'rank': stats['global_leaderboard_rank'],
            'country_rank': stats['country_leaderboard_rank']
        }

def get_recent(user: Union[int, str], mode: int = 0, 
               relax: int = 0, limit: int = 0) -> Union[dict, object]:
    with requests.Session() as sess:
        params = {
            'name' if isinstance(user, str) else 'id': user,
            'mode': mode,
            'rx': relax
        }
        req = sess.get(f'{BASE_API}/users/scores/recent?', params=params)

        if not req or req.status_code != 200 or not (json := req.json()):
            return None

        json = json['scores'][limit - 1 if limit else limit]
        _json = get_profile(user, mode, relax)

        return {
            'username': _json['username'],
            'userid': _json['userid'],
            'score': json['score'],
            'max_combo': json['max_combo'],
            'mods': repr(Mods(int(json['mods']))),
            '300s': json['count_300'],
            '100s': json['count_100'],
            '50s': json['count_50'],
            'misses': json['count_miss'],
            'time': json['time'].replace('T', ' ').replace('Z',' '),
            'acc': round(float(json['accuracy']), 2),
            'pp': round(float(json['pp']), 2),
            'rank': GRADE_URLS.get(json['rank']),
            'beatmap_id': (beatmap_json := json['beatmap'])['beatmap_id'],
            'beatmapset_id': beatmap_json['beatmapset_id'],
            'song_name': beatmap_json['song_name'],
            'ar': beatmap_json['ar'],
            'od': beatmap_json['od'],
            'difficulty': round(float(beatmap_json['difficulty2'][GAMEMODES[mode]]), 2),
            'full_combo': beatmap_json['max_combo'],
            'completion': map_completion_percentage(beatmap_json['beatmap_id'],
                          (int(json['count_300']) + int(json['count_100']) + int(json['count_50']) + int(json['count_miss']))
            )
        }

def get_best(user: Union[int, str], mode: int = 0, 
               relax: int = 0, limit: int = 0) -> Union[dict, object]:
    with requests.Session() as sess:
        params = {
            'name' if isinstance(user, str) else 'id': user,
            'mode': mode,
            'rx': relax
        }
        req = sess.get(f'{BASE_API}/users/scores/best?', params=params)

        if not req or req.status_code != 200 or not (json := req.json()):
            return None

        json = json['scores'][limit - 1 if limit else limit]
        _json = get_profile(user, mode, relax)

        return {
            'username': _json['username'],
            'userid': _json['userid'],
            'score': json['score'],
            'max_combo': json['max_combo'],
            'mods': repr(Mods(int(json['mods']))),
            '300s': json['count_300'],
            '100s': json['count_100'],
            '50s': json['count_50'],
            'misses': json['count_miss'],
            'time': json['time'].replace('T', ' ').replace('Z',' '),
            'acc': round(float(json['accuracy']), 2),
            'pp': round(float(json['pp']), 2),
            'rank': GRADE_URLS.get(json['rank']),
            'beatmap_id': (beatmap_json := json['beatmap'])['beatmap_id'],
            'beatmapset_id': beatmap_json['beatmapset_id'],
            'song_name': beatmap_json['song_name'],
            'ar': beatmap_json['ar'],
            'od': beatmap_json['od'],
            'difficulty': round(float(beatmap_json['difficulty2'][GAMEMODES[mode]]), 2),
            'full_combo': beatmap_json['max_combo'],
        }

def get_scores(user: Union[int, str], beatmapid: int, mode: int = 0, 
               relax: int = 0, limit: int = 0) -> Union[dict, object]:
    with requests.Session() as sess:
        params = {
            'u': user if isinstance(user, int) else get_profile(user)['userid'],
            'b': beatmapid,
            'm': mode,
            'rx': relax
        }
        req = sess.get(f'{BASE_API}/get_scores?', params=params)
        params = {
            'limit': 1,
            'b': beatmapid,
            'm': mode
        }
        _req = sess.get(f'{BASE_API}/get_beatmaps?', params=params)

        if not req or req.status_code != 200 or not (json := req.json()):
            return None
        
        if not _req or _req.status_code != 200 or not (_json := _req.json()):
            return None

        json = json[limit - 1 if limit else limit]

        return {
            'username': json['username'],
            'userid': json['user_id'],
            'score': json['score'],
            'max_combo': json['maxcombo'],
            'mods': repr(Mods(int(json['enabled_mods']))),
            '300s': json['count300'],
            '100s': json['count100'],
            '50s': json['count50'],
            'misses': json['countmiss'],
            'time': json['date'].replace('T', ' ').replace('Z',' '),
            'pp': round(float(json['pp']), 2),
            'rank': GRADE_URLS.get(json['rank']),
            'acc': round(calc_acc(mode, 
            int(json['count300']), int(json['count100']), int(json['count50']), int(json['countmiss'])
            ), 2),
        
            'beatmap_id': beatmapid,
            'beatmapset_id': (_json := _json[0])['beatmapset_id'],
            'song_name': f"{_json['artist']} - {_json['title']} [{_json['version']}]",
            'ar': _json['diff_approach'],
            'od': _json['diff_overall'],
            'difficulty': round(float(_json['difficultyrating']), 2),
            'full_combo': _json['max_combo'],
        }

def get_beatmap(beatmapid: int, mode: int) -> dict:
    with requests.Session() as sess:
        params = {
            'limit': 1,
            'b': beatmapid,
            'm': mode
        }

        req = sess.get(f'{BASE_API}/get_beatmaps?', params=params)

        if not req or req.status_code != 200 or not (json := req.json()):
            return None
        
        return json[0]
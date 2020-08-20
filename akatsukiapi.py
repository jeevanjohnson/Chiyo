from enum import IntEnum
import requests

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

def stats(user: str):
    """
    gets regular stats from akatsuki!
    example: stats('Cover')
    0 = username
    1 = ranked score
    2 = totalscore
    3 = playcount
    4 = playtime
    5 = replayswatched
    6 = levels (rounded)
    7 = accuracy (rounded)
    8 = pp
    9 = global rank
    10 = country rank
    11 = country
    12 = userid
    13 = registered
    14 = last online
    15 = clan name
    16 = clan tag
    17 = clan description
    18 = followers
    19 = clan id
    """
    stats = requests.get(f'https://akatsuki.pw/api/v1/users/full?name={user}')
    if not stats:
        return 'error'
    usernamee = stats.json()['username']

    if ' ' in usernamee:
        username = usernamee.replace(' ','ygfviasfa')
    else:
        username = usernamee
    rankedscore = stats.json()['stats'][0]['std']['ranked_score']
    totalscore = stats.json()['stats'][0]['std']['total_score']
    playcount = stats.json()['stats'][0]['std']['playcount']
    playtime = stats.json()['stats'][0]['std']['playtime']
    replayswatched = stats.json()['stats'][0]['std']['replays_watched']
    levell = stats.json()['stats'][0]['std']['level']
    level = round(levell, 2)
    accuracyy = stats.json()['stats'][0]['std']['accuracy']
    accuracy = round(accuracyy, 2)
    pp = stats.json()['stats'][0]['std']['pp']
    globalrank = stats.json()['stats'][0]['std']['global_leaderboard_rank']
    countryrank = stats.json()['stats'][0]['std']['country_leaderboard_rank']
    country = stats.json()['country']
    userid = stats.json()['id']
    registered = stats.json()['registered_on']
    lastonline = stats.json()['latest_activity']
    clan = stats.json()['clan']['name']
    clantag = stats.json()['clan']['tag']
    clanDescription = stats.json()['clan']['description']
    followers = stats.json()['followers']
    clanid = stats.json()['clan']['id']
    return f'{username} {rankedscore} {totalscore} {playcount} {playtime} {replayswatched} {level} {accuracy} {pp} {globalrank} {countryrank} {country} {userid} {registered} {lastonline} {clan} {clantag} {clanDescription} {followers} {clanid}'.split()

def relaxstats(user: str):
    """
    gets regular stats from akatsuki!
    example: relaxstats('Cover')
    0 = username
    1 = ranked score
    2 = totalscore
    3 = playcount
    4 = playtime
    5 = replayswatched
    6 = levels (rounded)
    7 = accuracy (rounded)
    8 = pp
    9 = global rank
    10 = country rank
    11 = country
    12 = userid
    13 = registered
    14 = last online
    15 = clan name
    16 = clan tag
    17 = clan description
    18 = followers
    19 = clan id
    """
    stats = requests.get(f'https://akatsuki.pw/api/v1/users/full?name={user}')
    if not stats:
        return 'error'
    usernamee = stats.json()['username']

    if ' ' in usernamee:
        username = usernamee.replace(' ','ygfviasfa')
    else:
        username = usernamee
    rankedscore = stats.json()['stats'][1]['std']['ranked_score']
    totalscore = stats.json()['stats'][1]['std']['total_score']
    playcount = stats.json()['stats'][1]['std']['playcount']
    playtime = stats.json()['stats'][1]['std']['playtime']
    replayswatched = stats.json()['stats'][1]['std']['replays_watched']
    levell = stats.json()['stats'][1]['std']['level']
    level = round(levell, 2)
    accuracyy = stats.json()['stats'][1]['std']['accuracy']
    accuracy = round(accuracyy, 2)
    pp = stats.json()['stats'][1]['std']['pp']
    globalrank = stats.json()['stats'][1]['std']['global_leaderboard_rank']
    countryrank = stats.json()['stats'][1]['std']['country_leaderboard_rank']
    country = stats.json()['country']
    userid = stats.json()['id']
    registered = stats.json()['registered_on']
    lastonline = stats.json()['latest_activity']
    clan = stats.json()['clan']['name']
    clantag = stats.json()['clan']['tag']
    clanDescription = stats.json()['clan']['description']
    followers = stats.json()['followers']
    clanid = stats.json()['clan']['id']
    return f'{username} {rankedscore} {totalscore} {playcount} {playtime} {replayswatched} {level} {accuracy} {pp} {globalrank} {countryrank} {country} {userid} {registered} {lastonline} {clan} {clantag} {clanDescription} {followers} {clanid}'.split()

def relaxtaikostats(user):
    """
    gets regular stats from akatsuki!
    example: relaxtaikostats('Cover')
    0 = username
    1 = ranked score
    2 = totalscore
    3 = playcount
    4 = playtime
    5 = replayswatched
    6 = levels (rounded)
    7 = accuracy (rounded)
    8 = pp
    9 = global rank
    10 = country rank
    11 = country
    12 = userid
    13 = registered
    14 = last online
    15 = clan name
    16 = clan tag
    17 = clan description
    18 = followers
    19 = clan id
    """

    stats = requests.get(f'https://akatsuki.pw/api/v1/users/full?name={user}')
    if not stats:
        return 'error'
    usernamee = stats.json()['username']

    if ' ' in usernamee:
        username = usernamee.replace(' ','ygfviasfa')
    else:
        username = usernamee

    rankedscore = stats.json()['stats'][1]['taiko']['ranked_score']
    totalscore = stats.json()['stats'][1]['taiko']['total_score']
    playcount = stats.json()['stats'][1]['taiko']['playcount']
    playtime = stats.json()['stats'][1]['taiko']['playtime']
    replayswatched = stats.json()['stats'][1]['taiko']['replays_watched']
    levell = stats.json()['stats'][1]['taiko']['level']
    level = round(levell, 2)
    accuracyy = stats.json()['stats'][1]['taiko']['accuracy']
    accuracy = round(accuracyy, 2)
    pp = stats.json()['stats'][1]['taiko']['pp']
    globalrank = stats.json()['stats'][1]['taiko']['global_leaderboard_rank']
    countryrank = stats.json()['stats'][1]['taiko']['country_leaderboard_rank']
    country = stats.json()['country']
    userid = stats.json()['id']
    registered = stats.json()['registered_on']
    lastonline = stats.json()['latest_activity']
    clan = stats.json()['clan']['name']
    clantag = stats.json()['clan']['tag']
    clanDescription = stats.json()['clan']['description']
    followers = stats.json()['followers']
    clanid = stats.json()['clan']['id']
    return f'{username} {rankedscore} {totalscore} {playcount} {playtime} {replayswatched} {level} {accuracy} {pp} {globalrank} {countryrank} {country} {userid} {registered} {lastonline} {clan} {clantag} {clanDescription} {followers} {clanid}'.split()

def taikostats(user: str):
    """
    gets regular stats from akatsuki!
    example: taikostats('Cover')
    0 = username
    1 = ranked score
    2 = totalscore
    3 = playcount
    4 = playtime
    5 = replayswatched
    6 = levels (rounded)
    7 = accuracy (rounded)
    8 = pp
    9 = global rank
    10 = country rank
    11 = country
    12 = userid
    13 = registered
    14 = last online
    15 = clan name
    16 = clan tag
    17 = clan description
    18 = followers
    19 = clan id
    """
    stats = requests.get(f'https://akatsuki.pw/api/v1/users/full?name={user}')
    if not stats:
        return 'error'
    usernamee = stats.json()['username']

    if ' ' in usernamee:
        username = usernamee.replace(' ','ygfviasfa')
    else:
        username = usernamee
    rankedscore = stats.json()['stats'][0]['taiko']['ranked_score']
    totalscore = stats.json()['stats'][0]['taiko']['total_score']
    playcount = stats.json()['stats'][0]['taiko']['playcount']
    playtime = stats.json()['stats'][0]['taiko']['playtime']
    replayswatched = stats.json()['stats'][0]['taiko']['replays_watched']
    levell = stats.json()['stats'][0]['taiko']['level']
    level = round(levell, 2)
    accuracyy = stats.json()['stats'][0]['taiko']['accuracy']
    accuracy = round(accuracyy, 2)
    pp = stats.json()['stats'][0]['taiko']['pp']
    globalrank = stats.json()['stats'][0]['taiko']['global_leaderboard_rank']
    countryrank = stats.json()['stats'][0]['taiko']['country_leaderboard_rank']
    country = stats.json()['country']
    userid = stats.json()['id']
    registered = stats.json()['registered_on']
    lastonline = stats.json()['latest_activity']
    clan = stats.json()['clan']['name']
    clantag = stats.json()['clan']['tag']
    clanDescription = stats.json()['clan']['description']
    followers = stats.json()['followers']
    clanid = stats.json()['clan']['id']
    return f'{username} {rankedscore} {totalscore} {playcount} {playtime} {replayswatched} {level} {accuracy} {pp} {globalrank} {countryrank} {country} {userid} {registered} {lastonline} {clan} {clantag} {clanDescription} {followers} {clanid}'.split()

def recent(user: str):
    """
    gets recent reg score stats from akatsuki!
    example: recent('Cover')
    0 = score
    1 = max_combo
    2 = full_combo
    3 = mods (letters)
    4 = count_300
    5 = count_100
    6 = count_50
    7 = count_miss
    8 = accuracy (rounded)
    9 = pp
    10 = rank
    11 = completed (Yes or No)
    12 = beatmap_id
    13 = beatmapset_id
    14 = ar
    15 = od
    16 = difficulty (rounded)
    gotta get song name on ur own :3c
    get userid and username from stats()
    """
    stats = requests.get(f'https://akatsuki.pw/api/v1/users/scores/recent?rx=0&name={user}&mode=0')
    if not stats:
        return 'error'
    score = stats.json()['scores'][0]['score']
    max_combo = stats.json()['scores'][0]['max_combo']
    full_combo = stats.json()['scores'][0]['beatmap']['max_combo']
    modsNum = stats.json()['scores'][0]['mods']

    if modsNum == 0:
        mods = 'NM'
    else:
        mods = readableMods(modsNum)
        if 'NC' in mods:
            mods = mods.replace('DT','')

    count_300 = stats.json()['scores'][0]['count_300']
    count_100 = stats.json()['scores'][0]['count_100']
    count_50 = stats.json()['scores'][0]['count_50']
    count_miss = stats.json()['scores'][0]['count_miss']
    acc = stats.json()['scores'][0]['accuracy']
    accuracy = round(acc, 2)
    ppp = stats.json()['scores'][0]['pp']
    pp = round(ppp, 2)
    rank = stats.json()['scores'][0]['rank']
    com = stats.json()['scores'][0]['completed']

    if com == 3 or com == 2:
        completed = 'Yes'
    else:
        completed = 'No'

    beatmap_id = stats.json()['scores'][0]['beatmap']['beatmap_id']
    beatmapset_id = stats.json()['scores'][0]['beatmap']['beatmapset_id']
    ar = stats.json()['scores'][0]['beatmap']['ar']
    od = stats.json()['scores'][0]['beatmap']['od']
    diff = stats.json()['scores'][0]['beatmap']['difficulty2']['std']
    difficulty = round(diff, 2)
    return f'{score} {max_combo} {full_combo} {mods} {count_300} {count_100} {count_50} {count_miss} {accuracy} {pp} {rank} {completed} {beatmap_id} {beatmapset_id} {ar} {od} {difficulty}'.split()

def relaxrecent(user: str):
    """
    gets recent relax score stats from akatsuki!
    example: recent('Cover')
    0 = score
    1 = max_combo
    2 = full_combo
    3 = mods (letters)
    4 = count_300
    5 = count_100
    6 = count_50
    7 = count_miss
    8 = accuracy (rounded)
    9 = pp
    10 = rank
    11 = completed (Yes or No)
    12 = beatmap_id
    13 = beatmapset_id
    14 = ar
    15 = od
    16 = difficulty (rounded)
    gotta get song name on ur own :3c
    get userid and username from stats()
    """
    stats = requests.get(f'https://akatsuki.pw/api/v1/users/scores/recent?rx=1&name={user}&mode=0')
    if not stats:
        return 'error'
    score = stats.json()['scores'][0]['score']
    max_combo = stats.json()['scores'][0]['max_combo']
    full_combo = stats.json()['scores'][0]['beatmap']['max_combo']
    modsNum = stats.json()['scores'][0]['mods']

    if modsNum == 0:
        mods = 'NM'
    else:
        mods = readableMods(modsNum)
        if 'NC' in mods:
            mods = mods.replace('DT','')
    
    count_300 = stats.json()['scores'][0]['count_300']
    count_100 = stats.json()['scores'][0]['count_100']
    count_50 = stats.json()['scores'][0]['count_50']
    count_miss = stats.json()['scores'][0]['count_miss']
    acc = stats.json()['scores'][0]['accuracy']
    accuracy = round(acc, 2)
    ppp = stats.json()['scores'][0]['pp']
    pp = round(ppp, 2)
    rank = stats.json()['scores'][0]['rank']
    com = stats.json()['scores'][0]['completed']

    if com == 3 or com == 2:
        completed = 'Yes'
    else:
        completed = 'No'

    beatmap_id = stats.json()['scores'][0]['beatmap']['beatmap_id']
    beatmapset_id = stats.json()['scores'][0]['beatmap']['beatmapset_id']
    ar = stats.json()['scores'][0]['beatmap']['ar']
    od = stats.json()['scores'][0]['beatmap']['od']
    diff = stats.json()['scores'][0]['beatmap']['difficulty2']['std']
    difficulty = round(diff, 2)
    return f'{score} {max_combo} {full_combo} {mods} {count_300} {count_100} {count_50} {count_miss} {accuracy} {pp} {rank} {completed} {beatmap_id} {beatmapset_id} {ar} {od} {difficulty}'.split()

def taikorecent(user: str):
    """
    gets recent taiko score stats from akatsuki!
    example: taikorecent('Cover')
    0 = score
    1 = max_combo
    2 = full_combo
    3 = mods (letters)
    4 = count_300
    5 = count_100
    6 = count_50
    7 = count_miss
    8 = accuracy (rounded)
    9 = pp
    10 = rank
    11 = completed (Yes or No)
    12 = beatmap_id
    13 = beatmapset_id
    14 = ar
    15 = od
    16 = difficulty (rounded)
    gotta get song name on ur own :3c
    get userid and username from stats()
    """
    stats = requests.get(f'https://akatsuki.pw/api/v1/users/scores/recent?rx=0&name={user}&mode=1')
    if not stats:
        return 'error'
    score = stats.json()['scores'][0]['score']
    max_combo = stats.json()['scores'][0]['max_combo']
    full_combo = stats.json()['scores'][0]['beatmap']['max_combo']
    modsNum = stats.json()['scores'][0]['mods']

    if modsNum == 0:
        mods = 'NM'
    else:
        mods = readableMods(modsNum)
        if 'NC' in mods:
            mods = mods.replace('DT','')
    
    count_300 = stats.json()['scores'][0]['count_300']
    count_100 = stats.json()['scores'][0]['count_100']
    count_50 = stats.json()['scores'][0]['count_50']
    count_miss = stats.json()['scores'][0]['count_miss']
    acc = stats.json()['scores'][0]['accuracy']
    accuracy = round(acc, 2)
    ppp = stats.json()['scores'][0]['pp']
    pp = round(ppp, 2)
    rank = stats.json()['scores'][0]['rank']
    com = stats.json()['scores'][0]['completed']

    if com == 3 or com == 2:
        completed = 'Yes'
    else:
        completed = 'No'

    beatmap_id = stats.json()['scores'][0]['beatmap']['beatmap_id']
    beatmapset_id = stats.json()['scores'][0]['beatmap']['beatmapset_id']
    ar = stats.json()['scores'][0]['beatmap']['ar']
    od = stats.json()['scores'][0]['beatmap']['od']
    diff = stats.json()['scores'][0]['beatmap']['difficulty2']['taiko']
    difficulty = round(diff, 2)
    return f'{score} {max_combo} {full_combo} {mods} {count_300} {count_100} {count_50} {count_miss} {accuracy} {pp} {rank} {completed} {beatmap_id} {beatmapset_id} {ar} {od} {difficulty}'.split()

def relaxtaikorecent(user: str):
    """
    gets recent relax taiko score from akatsuki!
    example: taikorecent('Cover')
    0 = score
    1 = max_combo
    2 = full_combo
    3 = mods (letters)
    4 = count_300
    5 = count_100
    6 = count_50
    7 = count_miss
    8 = accuracy (rounded)
    9 = pp
    10 = rank
    11 = completed (Yes or No)
    12 = beatmap_id
    13 = beatmapset_id
    14 = ar
    15 = od
    16 = difficulty (rounded)
    gotta get song name on ur own :3c
    get userid and username from stats()
    """
    stats = requests.get(f'https://akatsuki.pw/api/v1/users/scores/recent?rx=1&name={user}&mode=1')
    if not stats:
        return 'error'
    score = stats.json()['scores'][0]['score']
    max_combo = stats.json()['scores'][0]['max_combo']
    full_combo = stats.json()['scores'][0]['beatmap']['max_combo']
    modsNum = stats.json()['scores'][0]['mods']

    if modsNum == 0:
        mods = 'NM'
    else:
        mods = readableMods(modsNum)
        if 'NC' in mods:
            mods = mods.replace('DT','')
    
    count_300 = stats.json()['scores'][0]['count_300']
    count_100 = stats.json()['scores'][0]['count_100']
    count_50 = stats.json()['scores'][0]['count_50']
    count_miss = stats.json()['scores'][0]['count_miss']
    acc = stats.json()['scores'][0]['accuracy']
    accuracy = round(acc, 2)
    ppp = stats.json()['scores'][0]['pp']
    pp = round(ppp, 2)
    rank = stats.json()['scores'][0]['rank']
    com = stats.json()['scores'][0]['completed']

    if com == 3 or com == 2:
        completed = 'Yes'
    else:
        completed = 'No'

    beatmap_id = stats.json()['scores'][0]['beatmap']['beatmap_id']
    beatmapset_id = stats.json()['scores'][0]['beatmap']['beatmapset_id']
    ar = stats.json()['scores'][0]['beatmap']['ar']
    od = stats.json()['scores'][0]['beatmap']['od']
    diff = stats.json()['scores'][0]['beatmap']['difficulty2']['taiko']
    difficulty = round(diff, 2)
    return f'{score} {max_combo} {full_combo} {mods} {count_300} {count_100} {count_50} {count_miss} {accuracy} {pp} {rank} {completed} {beatmap_id} {beatmapset_id} {ar} {od} {difficulty}'.split()

def top(user: str):
    """
    gets top reg score from akatsuki!
    example: top('Cover')
    0 = score
    1 = max_combo
    2 = full_combo
    3 = mods (letters)
    4 = count_300
    5 = count_100
    6 = count_50
    7 = count_miss
    8 = accuracy (rounded)
    9 = pp
    10 = rank
    11 = completed (Yes or No)
    12 = beatmap_id
    13 = beatmapset_id
    14 = ar
    15 = od
    16 = difficulty (rounded)
    gotta get song name on ur own :3c
    get userid and username from stats()
    """
    stats = requests.get(f'https://akatsuki.pw/api/v1/users/scores/best?rx=0&name={user}&mode=0')
    if not stats:
        return 'error'
    score = stats.json()['scores'][0]['score']
    max_combo = stats.json()['scores'][0]['max_combo']
    full_combo = stats.json()['scores'][0]['beatmap']['max_combo']
    modsNum = stats.json()['scores'][0]['mods']

    if modsNum == 0:
        mods = 'NM'
    else:
        mods = readableMods(modsNum)
        if 'NC' in mods:
            mods = mods.replace('DT','')
    
    count_300 = stats.json()['scores'][0]['count_300']
    count_100 = stats.json()['scores'][0]['count_100']
    count_50 = stats.json()['scores'][0]['count_50']
    count_miss = stats.json()['scores'][0]['count_miss']
    acc = stats.json()['scores'][0]['accuracy']
    accuracy = round(acc, 2)
    ppp = stats.json()['scores'][0]['pp']
    pp = round(ppp, 2)
    rank = stats.json()['scores'][0]['rank']
    com = stats.json()['scores'][0]['completed']

    if com == 3 or com == 2:
        completed = 'Yes'
    else:
        completed = 'No'

    beatmap_id = stats.json()['scores'][0]['beatmap']['beatmap_id']
    beatmapset_id = stats.json()['scores'][0]['beatmap']['beatmapset_id']
    ar = stats.json()['scores'][0]['beatmap']['ar']
    od = stats.json()['scores'][0]['beatmap']['od']
    diff = stats.json()['scores'][0]['beatmap']['difficulty2']['std']
    difficulty = round(diff, 2)
    return f'{score} {max_combo} {full_combo} {mods} {count_300} {count_100} {count_50} {count_miss} {accuracy} {pp} {rank} {completed} {beatmap_id} {beatmapset_id} {ar} {od} {difficulty}'.split()

def relaxtop(user: str):
    """
    gets top relax score from akatsuki!
    example: top('Cover')
    0 = score
    1 = max_combo
    2 = full_combo
    3 = mods (letters)
    4 = count_300
    5 = count_100
    6 = count_50
    7 = count_miss
    8 = accuracy (rounded)
    9 = pp
    10 = rank
    11 = completed (Yes or No)
    12 = beatmap_id
    13 = beatmapset_id
    14 = ar
    15 = od
    16 = difficulty (rounded)
    gotta get song name on ur own :3c
    get userid and username from stats()
    """
    stats = requests.get(f'https://akatsuki.pw/api/v1/users/scores/best?rx=1&name={user}&mode=0')
    if not stats:
        return 'error'
    score = stats.json()['scores'][0]['score']
    max_combo = stats.json()['scores'][0]['max_combo']
    full_combo = stats.json()['scores'][0]['beatmap']['max_combo']
    modsNum = stats.json()['scores'][0]['mods']

    if modsNum == 0:
        mods = 'NM'
    else:
        mods = readableMods(modsNum)
        if 'NC' in mods:
            mods = mods.replace('DT','')
    
    count_300 = stats.json()['scores'][0]['count_300']
    count_100 = stats.json()['scores'][0]['count_100']
    count_50 = stats.json()['scores'][0]['count_50']
    count_miss = stats.json()['scores'][0]['count_miss']
    acc = stats.json()['scores'][0]['accuracy']
    accuracy = round(acc, 2)
    ppp = stats.json()['scores'][0]['pp']
    pp = round(ppp, 2)
    rank = stats.json()['scores'][0]['rank']
    com = stats.json()['scores'][0]['completed']

    if com == 3 or com == 2:
        completed = 'Yes'
    else:
        completed = 'No'

    beatmap_id = stats.json()['scores'][0]['beatmap']['beatmap_id']
    beatmapset_id = stats.json()['scores'][0]['beatmap']['beatmapset_id']
    ar = stats.json()['scores'][0]['beatmap']['ar']
    od = stats.json()['scores'][0]['beatmap']['od']
    diff = stats.json()['scores'][0]['beatmap']['difficulty2']['std']
    difficulty = round(diff, 2)
    return f'{score} {max_combo} {full_combo} {mods} {count_300} {count_100} {count_50} {count_miss} {accuracy} {pp} {rank} {completed} {beatmap_id} {beatmapset_id} {ar} {od} {difficulty}'.split()

def relaxtaikotop(user: str):
    """
    gets top relax score from akatsuki!
    example: top('Cover')
    0 = score
    1 = max_combo
    2 = full_combo
    3 = mods (letters)
    4 = count_300
    5 = count_100
    6 = count_50
    7 = count_miss
    8 = accuracy (rounded)
    9 = pp
    10 = rank
    11 = completed (Yes or No)
    12 = beatmap_id
    13 = beatmapset_id
    14 = ar
    15 = od
    16 = difficulty (rounded)
    gotta get song name on ur own :3c
    get userid and username from stats()
    """
    stats = requests.get(f'https://akatsuki.pw/api/v1/users/scores/best?rx=1&name={user}&mode=1')
    if not stats:
        return 'error'
    score = stats.json()['scores'][0]['score']
    max_combo = stats.json()['scores'][0]['max_combo']
    full_combo = stats.json()['scores'][0]['beatmap']['max_combo']
    modsNum = stats.json()['scores'][0]['mods']

    if modsNum == 0:
        mods = 'NM'
    else:
        mods = readableMods(modsNum)
        if 'NC' in mods:
            mods = mods.replace('DT','')
    
    count_300 = stats.json()['scores'][0]['count_300']
    count_100 = stats.json()['scores'][0]['count_100']
    count_50 = stats.json()['scores'][0]['count_50']
    count_miss = stats.json()['scores'][0]['count_miss']
    acc = stats.json()['scores'][0]['accuracy']
    accuracy = round(acc, 2)
    ppp = stats.json()['scores'][0]['pp']
    pp = round(ppp, 2)
    rank = stats.json()['scores'][0]['rank']
    com = stats.json()['scores'][0]['completed']

    if com == 3 or com == 2:
        completed = 'Yes'
    else:
        completed = 'No'

    beatmap_id = stats.json()['scores'][0]['beatmap']['beatmap_id']
    beatmapset_id = stats.json()['scores'][0]['beatmap']['beatmapset_id']
    ar = stats.json()['scores'][0]['beatmap']['ar']
    od = stats.json()['scores'][0]['beatmap']['od']
    diff = stats.json()['scores'][0]['beatmap']['difficulty2']['taiko']
    difficulty = round(diff, 2)
    return f'{score} {max_combo} {full_combo} {mods} {count_300} {count_100} {count_50} {count_miss} {accuracy} {pp} {rank} {completed} {beatmap_id} {beatmapset_id} {ar} {od} {difficulty}'.split()

def taikotop(user: str):
    """
    gets top relax score from akatsuki!
    example: top('Cover')
    0 = score
    1 = max_combo
    2 = full_combo
    3 = mods (letters)
    4 = count_300
    5 = count_100
    6 = count_50
    7 = count_miss
    8 = accuracy (rounded)
    9 = pp
    10 = rank
    11 = completed (Yes or No)
    12 = beatmap_id
    13 = beatmapset_id
    14 = ar
    15 = od
    16 = difficulty (rounded)
    gotta get song name on ur own :3c
    get userid and username from stats()
    """
    stats = requests.get(f'https://akatsuki.pw/api/v1/users/scores/best?rx=0&name={user}&mode=1')
    if not stats:
        return 'error'
    score = stats.json()['scores'][0]['score']
    max_combo = stats.json()['scores'][0]['max_combo']
    full_combo = stats.json()['scores'][0]['beatmap']['max_combo']
    modsNum = stats.json()['scores'][0]['mods']

    if modsNum == 0:
        mods = 'NM'
    else:
        mods = readableMods(modsNum)
        if 'NC' in mods:
            mods = mods.replace('DT','')
    
    count_300 = stats.json()['scores'][0]['count_300']
    count_100 = stats.json()['scores'][0]['count_100']
    count_50 = stats.json()['scores'][0]['count_50']
    count_miss = stats.json()['scores'][0]['count_miss']
    acc = stats.json()['scores'][0]['accuracy']
    accuracy = round(acc, 2)
    pp = stats.json()['scores'][0]['pp']
    rank = stats.json()['scores'][0]['rank']
    com = stats.json()['scores'][0]['completed']

    if com == 3 or com == 2:
        completed = 'Yes'
    else:
        completed = 'No'

    beatmap_id = stats.json()['scores'][0]['beatmap']['beatmap_id']
    beatmapset_id = stats.json()['scores'][0]['beatmap']['beatmapset_id']
    ar = stats.json()['scores'][0]['beatmap']['ar']
    od = stats.json()['scores'][0]['beatmap']['od']
    diff = stats.json()['scores'][0]['beatmap']['difficulty2']['taiko']
    difficulty = round(diff, 2)
    return f'{score} {max_combo} {full_combo} {mods} {count_300} {count_100} {count_50} {count_miss} {accuracy} {pp} {rank} {completed} {beatmap_id} {beatmapset_id} {ar} {od} {difficulty}'.split()

def compare(username: str, bmid: int, mode: int, rx: int):

    user = requests.get(f'https://akatsuki.pw/api/v1/users/whatid?name={username}')
    if not user:
        return 'no user found'
    userid = user.json()['id']
    info = requests.get(f'https://akatsuki.pw/api/get_scores?b={bmid}&m={mode}&u={userid}&limit=1&')
    if not info:
        return 'no score found'

    return info.json()[0]

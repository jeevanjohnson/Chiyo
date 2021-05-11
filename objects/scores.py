import config
from ext import glob
from typing import Union
from discord import Embed
from objects.const import Mods
from objects.const import Server
from objects.players import Player
from objects.beatmaps import Beatmap
from objects.const import GRADE_URLS

class Score:
    def __init__(self) -> None:
        self.score: int
        self.nkatsu: int
        self.ngeki: int
        self.n300: int
        self.n100: int
        self.n50: int
        self.misses: int
        self.mods: Mods
        self.date: str
        self.rank: str
        self.max_combo: int
        self.bmap: Beatmap
        self.completed: bool
        self.pp: float
        self.id: int
        self.server: Server
        self.player: Player
        self.mode: int
        self.acc: float

    def calc_acc(self) -> float:
        if self.mode == 0: # osu!
            total = sum((self.n300, self.n100, self.n50, self.misses))

            if total == 0:
                self.acc = 0.0
                return

            self.acc = 100.0 * sum((
                self.n50 * 50.0,
                self.n100 * 100.0,
                self.n300 * 300.0
            )) / (total * 300.0)

        elif self.mode == 1: # osu!taiko
            total = sum((self.n300, self.n100, self.misses))

            if total == 0:
                self.acc = 0.0
                return

            self.acc = 100.0 * sum((
                self.n100 * 0.5,
                self.n300
            )) / total

        elif self.mode == 2:
            # osu!catch
            total = sum((self.n300, self.n100, self.n50,
                         self.nkatu, self.misses))

            if total == 0:
                self.acc = 0.0
                return

            self.acc = 100.0 * sum((
                self.n300,
                self.n100,
                self.n50
            )) / total

        elif self.mode == 3:
            # osu!mania
            total = sum((self.n300, self.n100, self.n50,
                         self.ngeki, self.nkatu, self.misses))

            if total == 0:
                self.acc = 0.0
                return

            self.acc = 100.0 * sum((
                self.n50 * 50.0,
                self.n100 * 100.0,
                self.nkatu * 200.0,
                (self.n300 + self.ngeki) * 300.0
            )) / (total * 300.0)

    @property
    def embed(self) -> Embed:
        if not self.completed:
            m = f'▸ Map Completion: {self.map_completion:.2f}%'
        else:
            m = ''

        description = (
            f'▸ {self.pp:.0f}PP [AR: {self.bmap.ar} OD: {self.bmap.od}] ▸ {self.acc:.2f}%\n'
            f'▸ {self.score:,} ▸ {self.max_combo}x/{self.bmap.max_combo}x '
            f'▸ [{self.n300}/{self.n100}/{self.n50}/{self.misses}]\n'
            + m
        )
        e = Embed(
            description = description
        )

        e.set_author(
            name = f"{self.bmap.song_name} +{repr(self.mods)} [{self.bmap.difficulty:.2f}★]",
            url = self.bmap.url,
            icon_url = GRADE_URLS[self.rank]
        )

        e.set_thumbnail(
            url = self.player.avatar
        )

        e.set_image(
            url = self.bmap.cover
        )

        return e

    @property    
    def map_completion(self) -> float:
        #TODO: Make this better lol
        if self.completed:
            return 100.0
        
        total_objects = (
            self.n300 + self.n100 + 
            self.n50 + self.misses
        )

        self.bmap.mapfile.get_hit_objects()
        
        return (total_objects / len(self.bmap.mapfile.hit_objects)) * 100

    @classmethod
    async def from_akatsuki_top(
        cls, user: Union[int, str],
        mode = 0, index = 0, relax = 0
    ):
        s = cls()
        base = 'https://akatsuki.pw/api/v1'
        path = 'users/scores/best'
        params = {
            'name' if isinstance(user, str) else 'id': user,
            'm': mode,
            'rx': relax
        }

        s.player = await Player.from_akatsuki(
            user, mode, relax
        )

        async with glob.http.get(
            url = f'{base}/{path}',
            params = params
        ) as resp:
            if not resp or resp.status != 200:
                return
            
            if not (json := await resp.json()):
                return
        
        if len(json) < index:
            return

        json = json['scores'][index]
        s.score = json['score']
        s.nkatsu = json['count_katu']
        s.ngeki = json['count_geki']
        s.n300 = json['count_300']
        s.n100 = json['count_100']
        s.n50 = json['count_50']
        s.misses = json['count_miss']
        s.mods = Mods(json['mods'])
        s.date = json['time'].replace('T', ' ').replace('Z', ' ')
        s.rank = json['rank']
        s.max_combo = json['max_combo']
        s.bmap = await Beatmap.from_id(
            bmap_id = json['beatmap']['beatmap_id'],
            mode = mode
        )
        s.completed = True
        s.server = Server.Akatsuki
        s.pp = json['pp']
        s.id = json['id']
        s.mode = mode

        s.calc_acc()

        return s

    @classmethod
    async def from_akatsuki_recent(
        cls, user: Union[str, int],
        mode = 0, index = 0, relax = 0
    ):
        s = cls()
        base = 'https://akatsuki.pw/api/v1'
        path = 'users/scores/recent?'
        params = {
            'name' if isinstance(user, str) else 'id': user,
            'm': mode,
            'rx': relax
        }

        s.player = await Player.from_akatsuki(
            user, mode, relax
        )

        async with glob.http.get(
            url = f'{base}/{path}',
            params = params
        ) as resp:
            if not resp or resp.status != 200:
                return
            
            if not (json := await resp.json()):
                return
        
        if len(json) < index:
            return

        json = json['scores'][index]
        s.score = json['score']
        s.nkatsu = json['count_katu']
        s.ngeki = json['count_geki']
        s.n300 = json['count_300']
        s.n100 = json['count_100']
        s.n50 = json['count_50']
        s.misses = json['count_miss']
        s.mods = Mods(json['mods'])
        s.date = json['time'].replace('T', ' ').replace('Z', ' ')
        s.rank = json['rank']
        s.max_combo = json['max_combo']
        s.bmap = await Beatmap.from_id(
            bmap_id = json['beatmap']['beatmap_id'],
            mode = mode
        )
        s.completed = json['completed'] > 1
        s.server = Server.Akatsuki
        s.pp = json['pp']
        s.id = json['id']
        s.mode = mode

        s.calc_acc()

        return s

    @classmethod
    async def from_bancho_recent(
        cls, user: Union[str, int], 
        mode = 0, index = 0
    ):
        s = cls()
        base = 'https://osu.ppy.sh/api'
        path = 'get_user_recent'
        params = {
            'k': config.api_key,
            'u': user,
            'm': mode,
            'type': 'string' if isinstance(user, str) else 'id'
        }

        s.player = await Player.from_bancho(
            user, mode
        )

        async with glob.http.get(
            url = f'{base}/{path}',
            params = params
        ) as resp:
            if not resp or resp.status != 200:
                return
            
            if not (json := await resp.json()):
                return
        
        if len(json) < index:
            return
        
        _json = json = json[index]
        s.score = int(json['score'])
        s.max_combo = int(json['maxcombo'])
        s.nkatsu = int(json['countkatu'])
        s.ngeki = int(json['countgeki'])
        s.n300 = int(json['count300'])
        s.n100 = int(json['count100'])
        s.n50 = int(json['count50'])
        s.misses = int(json['countmiss'])
        s.mods = Mods(int(json['enabled_mods']))
        s.date = json['date']
        s.rank = json['rank']
        s.bmap = await Beatmap.from_id(
            bmap_id = int(json['beatmap_id']),
            mode = mode
        )
        s.completed = s.rank != 'F'
        s.server = Server.Bancho
        s.pp = 0.0
        s.mode = mode

        if s.completed and s.bmap.status:
            path = 'get_scores'
            params = {
                'k': config.api_key,
                'b': s.bmap.id,
                'u': user,
                'm': mode,
                'type': 'string' if isinstance(user, str) else 'id'
            }
            async with glob.http.get(
                url = f'{base}/{path}',
                params = params
            ) as resp:
                if not resp or resp.status != 200:
                    return
                
                if not (json := await resp.json()):
                    return

            for score in json:
                if (
                    _json['score'] == score['score'] and
                    _json['maxcombo'] == score['maxcombo'] and
                    _json['count50'] == score['count50'] and
                    _json['count100'] == score['count100'] and
                    _json['count300'] == score['count300'] and
                    _json['countmiss'] == score['countmiss'] and
                    _json['countkatu'] == score['countkatu'] and
                    _json['countgeki'] == score['countgeki'] and
                    _json['perfect'] == score['perfect'] and
                    _json['enabled_mods'] == score['enabled_mods'] and
                    _json['date'] == score['date'] and
                    _json['rank'] == score['rank']
                ):
                    s.id = int(score['score_id'])
                    s.pp = float(score['pp'])
                    break
        
        s.calc_acc()

        return s

    @classmethod
    async def from_bancho_top(
        cls, user: Union[str, int], 
        mode = 0, index = 0
    ):
        s = cls()
        base = 'https://osu.ppy.sh/api'
        path = 'get_user_best'
        params = {
            'k': config.api_key,
            'u': user,
            'm': mode,
            'type': 'string' if isinstance(user, str) else 'id'
        }

        s.player = await Player.from_bancho(
            user, mode
        )

        async with glob.http.get(
            url = f'{base}/{path}',
            params = params
        ) as resp:
            if not resp or resp.status != 200:
                return
            
            if not (json := await resp.json()):
                return
        
        if len(json) < index:
            return
        
        json = json[index]
        s.score = int(json['score'])
        s.max_combo = int(json['maxcombo'])
        s.nkatsu = int(json['countkatu'])
        s.ngeki = int(json['countgeki'])
        s.n300 = int(json['count300'])
        s.n100 = int(json['count100'])
        s.n50 = int(json['count50'])
        s.misses = int(json['countmiss'])
        s.mods = Mods(int(json['enabled_mods']))
        s.date = json['date']
        s.rank = json['rank']
        s.bmap = await Beatmap.from_id(
            bmap_id = int(json['beatmap_id']),
            mode = mode
        )
        s.completed = True
        s.server = Server.Bancho
        s.pp = float(json['pp'])
        s.mode = mode
        
        s.calc_acc()

        return s

    @classmethod
    async def from_akatsuki(
        cls, user: Player,
        bmap: Beatmap, mode = 0, 
        index = 0, relax = 0
    ):
        s = cls()
        base = 'https://akatsuki.pw/api'
        path = 'get_scores'
        params = {
            'b': bmap.id,
            'm': mode,
            'u': user.id,
            'rx': relax
        }

        s.player = user

        async with glob.http.get(
            url = f'{base}/{path}',
            params = params
        ) as resp:
            if not resp or resp.status != 200:
                return
            
            if not (json := await resp.json()):
                return
        
        if len(json) < index:
            return

        json = json[index]
        s.score = int(json['score'])
        s.nkatsu = int(json['countkatu'])
        s.ngeki = int(json['countgeki'])
        s.n300 = int(json['count300'])
        s.n100 = int(json['count100'])
        s.n50 = int(json['count50'])
        s.misses = int(json['countmiss'])
        s.mods = Mods(int(json['enabled_mods']))
        s.date = json['date']
        s.rank = json['rank']
        s.max_combo = int(json['maxcombo'])
        s.bmap = bmap
        s.completed = True
        s.server = Server.Akatsuki
        s.pp = float(json['pp'])
        s.id = int(json['score_id'])
        s.mode = mode

        s.calc_acc()

        return s        

    @classmethod
    async def from_bancho(
        cls, user: Player, 
        bmap: Beatmap,
        mode = 0, index = 0,
    ):
        s = cls()
        base = 'https://osu.ppy.sh/api'
        path = 'get_scores'
        params = {
            'k': config.api_key,
            'u': user.id,
            'm': mode,
            'b': bmap.id,
            'type': 'string' if isinstance(user, str) else 'id'
        }

        s.player = user

        async with glob.http.get(
            url = f'{base}/{path}',
            params = params
        ) as resp:
            if not resp or resp.status != 200:
                return
            
            if not (json := await resp.json()):
                return
        
        if len(json) < index:
            return
        
        json = json[index]
        s.score = int(json['score'])
        s.max_combo = int(json['maxcombo'])
        s.nkatsu = int(json['countkatu'])
        s.ngeki = int(json['countgeki'])
        s.n300 = int(json['count300'])
        s.n100 = int(json['count100'])
        s.n50 = int(json['count50'])
        s.misses = int(json['countmiss'])
        s.mods = Mods(int(json['enabled_mods']))
        s.date = json['date']
        s.rank = json['rank']
        s.bmap = bmap
        s.completed = True
        s.server = Server.Bancho
        s.pp = float(json['pp'])
        s.mode = mode
        
        s.calc_acc()

        return s       
import config
import pyttanko
from ext import glob
from helpers import note
from discord import Embed
from objects.const import Mods
from objects.const import Server
from objects.players import Player
from objects.beatmaps import Beatmap
from objects.const import GRADE_URLS
from functools import cached_property
from objects.const import BeatmapStatus
from objects.const import magnitude_fmt

ignore = (BeatmapStatus.Pending, BeatmapStatus.WIP, BeatmapStatus.Graveyard)

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
        self.index: int

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
                         self.nkatsu, self.misses))

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
                         self.ngeki, self.nkatsu, self.misses))

            if total == 0:
                self.acc = 0.0
                return

            self.acc = 100.0 * sum((
                self.n50 * 50.0,
                self.n100 * 100.0,
                self.nkatsu * 200.0,
                (self.n300 + self.ngeki) * 300.0
            )) / (total * 300.0)

    @cached_property
    def pp_if_fc(self) -> tuple[float, float]:
        if self.mode != 0:
            return
        
        n100 = round(self.n100 / 1.5)
        n50 = round(self.n50 / 1.5)
        stars = pyttanko.diff_calc().calc(self.bmap.mapfile, self.mods._value_)
        data = pyttanko.ppv2(
            stars.aim, stars.speed, 
            bmap = self.bmap.mapfile, 
            mods = self.mods._value_,
            n100 = n100, n50 = n50
        )

        return data[0], data[4]
    
    @property
    def embed(self) -> Embed:
        if not self.completed:
            m = f'\n▸ Map Completion: {self.map_completion:.2f}%'
        else:
            m = ''

        if (
            self.acc < 100 and 
            self.mode == 0 and
            not self.mods & Mods.RELAX
        ):
            pp, acc = self.pp_if_fc
            if_fc = f'{pp:.2f}PP for {acc:.2f}% FC'
        else:
            self.bmap.mods = self.mods
            self.bmap.convert_difficulty_attrs()
            if_fc = f'AR: {self.bmap.ar:.2f} OD: {self.bmap.od:.2f}'

        score = magnitude_fmt(self.score)
        description = (
            f'▸ {self.pp:.0f}PP [{if_fc}] ▸ {self.acc:.2f}%\n'
            f'▸ {score} ▸ {self.max_combo}x/{self.bmap.max_combo}x '
            f'▸ [{self.n300}/{self.n100}/{self.n50}/{self.misses}]'
            + m
        )
        e = Embed(
            description = description
        )
        
        if self.mode == 0:
            sr = f'{self.bmap.convert_star_rating():.2f}★'
        else:
            sr = f'{self.bmap.difficulty:.2f}★'
        
        e.set_author(
            name = f"{self.bmap.song_name} +{repr(self.mods)} [{sr}]",
            url = self.bmap.url,
            icon_url = GRADE_URLS[self.rank]
        )

        e.set_thumbnail(
            url = self.player.avatar
        )

        e.set_image(
            url = self.bmap.cover
        )

        e.set_footer(
            text = f'Score set on {self.server.name.lower()}!'
        )

        return e

    @cached_property    
    def map_completion(self) -> float:
        if self.completed:
            return 100.0
        
        total_objects = (
            self.n300 + self.n100 + 
            self.n50 + self.misses
        )

        if self.mode == 0:
            hitobjects = len(self.bmap.mapfile.hitobjects)
        else:
            self.bmap._mapfile.get_hit_objects()
            hitobjects = len(self.bmap._mapfile.hit_objects)

        return (total_objects / hitobjects) * 100

    @classmethod
    async def from_akatsuki_top(
        cls, user: Player,
        mode = 0, index = 0, 
        relax = 0
    ):
        s = cls()
        s.index = index
        base = 'https://akatsuki.pw/api/v1'
        path = 'users/scores/best'
        params = {
            'id': user.id,
            'mode': mode,
            'rx': relax
        }

        s.player = user

        async with glob.http.get(
            url = f'{base}/{path}',
            params = params
        ) as resp:
            if not resp or resp.status != 200:
                await note(
                    statement = "if not resp or resp.status != 200",
                    name_or_id = user.name,
                    mode = mode,
                    relax = relax,
                    function = 'Score.from_akatsuki_top'
                )
                return
            
            if not (json := await resp.json()):
                await note(
                    statement = "if not (json := await resp.json())",
                    name_or_id = user.name,
                    mode = mode,
                    relax = relax,
                    function = 'Score.from_akatsuki_top'
                )
                return
        
        if len(json['scores']) - 1 < index:
            await note(
                statement = "if len(json['scores']) - 1 < index",
                json = json['scores'],
                name_or_id = user.name,
                mode = mode,
                relax = relax,
                function = 'Score.from_akatsuki_top'
            )
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
        if not s.bmap:
            await note(
                statement = "if not s.bmap",
                name_or_id = user.name,
                mode = mode,
                relax = relax,
                bmap_id = json['beatmap']['beatmap_id'],
                function = 'Score.from_akatsuki_top'
            )
            return
        
        s.completed = True
        s.server = Server.Akatsuki
        s.bmap.mods = s.mods
        s.pp = json['pp']
        s.id = json['id']
        s.mode = mode

        s.calc_acc()

        return s

    @classmethod
    async def from_akatsuki_recent(
        cls, user: Player,
        mode = 0, index = 0, 
        relax = 0
    ):
        s = cls()
        s.index = index
        base = 'https://akatsuki.pw/api/v1'
        path = 'users/scores/recent?'
        params = {
            'id': user.id,
            'mode': mode,
            'rx': relax
        }

        s.player = user

        async with glob.http.get(
            url = f'{base}/{path}',
            params = params
        ) as resp:
            if not resp or resp.status != 200:
                await note(
                    statement = "if not resp or resp.status != 200",
                    name_or_id = user.name,
                    mode = mode,
                    relax = relax,
                    function = 'Score.from_akatsuki_recent'
                )
                return
            
            if not (json := await resp.json()):
                await note(
                    statement = "if not (json := await resp.json())",
                    name_or_id = user.name,
                    mode = mode,
                    relax = relax,
                    function = 'Score.from_akatsuki_recent'
                )
                return
        
        if len(json['scores']) - 1 < index:
            await note(
                statement = "if len(json['scores']) - 1 < index",
                json = json['scores'],
                name_or_id = user.name,
                mode = mode,
                relax = relax,
                function = 'Score.from_akatsuki_recent'
            )
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
        if not s.bmap:
            await note(
                statement = "if not s.bmap",
                json = json['scores'],
                name_or_id = user.name,
                mode = mode,
                relax = relax,
                bmap_id = json['beatmap']['beatmap_id'],
                function = 'Score.from_akatsuki_recent'
            )
            return
        
        s.completed = json['completed'] > 1
        s.server = Server.Akatsuki
        s.bmap.mods = s.mods
        s.pp = json['pp']
        s.id = json['id']
        s.mode = mode

        s.calc_acc()

        return s

    @classmethod
    async def from_bancho_recent(
        cls, user: Player, 
        mode = 0, index = 0
    ):
        s = cls()
        s.index = index
        base = 'https://osu.ppy.sh/api'
        path = 'get_user_recent'
        params = {
            'k': config.api_key,
            'u': user.id,
            'm': mode,
            'type': 'id'
        }

        s.player = user

        async with glob.http.get(
            url = f'{base}/{path}',
            params = params
        ) as resp:
            if not resp or resp.status != 200:
                await note(
                    statement = "if not resp or resp.status != 200",
                    name_or_id = user.name,
                    mode = mode,
                    function = 'Score.from_bancho_recent'
                )
                return
            
            if not (json := await resp.json()):
                await note(
                    statement = "if not (json := await resp.json())",
                    name_or_id = user.name,
                    mode = mode,
                    function = 'Score.from_bancho_recent'
                )
                return
        
        if len(json) - 1 < index:
            await note(
                statement = "if len(json) - 1 < index",
                json = json,
                name_or_id = user.name,
                mode = mode,
                function = 'Score.from_bancho_recent'
            )
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
        if not s.bmap:
            await note(
                statement = "if not s.bmap",
                name_or_id = user.name,
                mode = mode,
                bmap_id = int(json['beatmap_id']),
                function = 'Score.from_bancho_recent'
            )
            return
        
        s.completed = s.rank != 'F'
        s.server = Server.Bancho
        s.bmap.mods = s.mods
        s.pp = 0.0
        s.mode = mode

        if (
            s.completed and 
            s.bmap.status not in ignore
        ):
            path = 'get_scores'
            params = {
                'k': config.api_key,
                'b': s.bmap.id,
                'u': user.id,
                'm': mode,
                'type': 'id'
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
                    s.pp = float(score['pp'] or 0)
                    break
        
        s.calc_acc()

        return s

    @classmethod
    async def from_bancho_top(
        cls, user: Player, 
        mode = 0, index = 0
    ):
        s = cls()
        s.index = index
        base = 'https://osu.ppy.sh/api'
        path = 'get_user_best'
        params = {
            'k': config.api_key,
            'u': user.id,
            'm': mode,
            'limit': 100,
            'type': 'id'
        }

        s.player = user

        async with glob.http.get(
            url = f'{base}/{path}',
            params = params
        ) as resp:
            if not resp or resp.status != 200:
                await note(
                    statement = "if not resp or resp.status != 200",
                    name_or_id = user.name,
                    mode = mode,
                    function = 'Score.from_bancho_top'
                )
                return
            
            if not (json := await resp.json()):
                await note(
                    statement = "if not (json := await resp.json())",
                    name_or_id = user.name,
                    mode = mode,
                    function = 'Score.from_bancho_top'
                )
                return
        
        if len(json) - 1 < index:
            await note(
                statement = "if len(json) - 1 < index",
                name_or_id = user.name,
                mode = mode,
                json = json,
                function = 'Score.from_bancho_top'
            )
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
        if not s.bmap:
            await note(
                statement = "if not s.bmap",
                name_or_id = user.name,
                mode = mode,
                bmap_id = int(json['beatmap_id']),
                function = 'Score.from_bancho_top'
            )
            return
        
        s.completed = True
        s.bmap.mods = s.mods
        s.server = Server.Bancho
        s.pp = float(json['pp'] or 0)
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
        s.index = index
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
                await note(
                    statement = "if not resp or resp.status != 200",
                    name_or_id = user.name,
                    mode = mode,
                    relax = relax,
                    index = index,
                    function = 'Score.from_akatsuki'
                )
                return
            
            if not (json := await resp.json()):
                await note(
                    statement = "if not (json := await resp.json())",
                    name_or_id = user.name,
                    mode = mode,
                    relax = relax,
                    index = index,
                    function = 'Score.from_akatsuki'
                )
                return
        
        if len(json) - 1 < index:
            await note(
                statement = "if len(json) - 1 < index",
                name_or_id = user.name,
                mode = mode,
                relax = relax,
                index = index,
                json = json,
                function = 'Score.from_akatsuki'
            )
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
        s.bmap.mods = s.mods
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
        s.index = index
        base = 'https://osu.ppy.sh/api'
        path = 'get_scores'
        params = {
            'k': config.api_key,
            'u': user.id,
            'm': mode,
            'b': bmap.id,
            'type': 'id'
        }

        s.player = user

        async with glob.http.get(
            url = f'{base}/{path}',
            params = params
        ) as resp:
            if not resp or resp.status != 200:
                await note(
                    statement = "if not resp or resp.status != 200",
                    name_or_id = user.name,
                    mode = mode,
                    index = index,
                    function = 'Score.from_bancho'
                )
                return
            
            if not (json := await resp.json()):
                await note(
                    statement = "if not (json := await resp.json())",
                    name_or_id = user.name,
                    mode = mode,
                    index = index,
                    function = 'Score.from_bancho'
                )
                return
        
        if len(json) - 1 < index:
            await note(
                statement = "if len(json) - 1 < index",
                name_or_id = user.name,
                mode = mode,
                index = index,
                json = json,
                function = 'Score.from_bancho'
            )
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
        s.pp = float(json['pp'] or 0)
        s.bmap.mods = s.mods
        s.mode = mode
        
        s.calc_acc()

        return s       
import config
import pyttanko
from ext import glob
from typing import Union
from discord import Embed
from typing import Optional
from objects.const import Mods
from objects.players import Player
from objects.const import BeatmapStatus
from coover import Beatmap as BeatmapParser

class Beatmap:
    def __init__(self) -> None:
        self.setid: int
        self.id: int
        self.total_length: int
        self.hit_length: int
        self.version: str
        self.md5: str
        self.cs: float
        self.od: float
        self.ar: float
        self.hp: float
        self.mode: int
        self.artist: str
        self.title: str
        self.creator: Player
        self.max_combo: int
        self.difficulty: float
        self.bpm: float
        self.status: BeatmapStatus
        self.favs: int
        self.last_updated: str
        self.mods: Mods = Mods.NOMOD
        self._mapfile: Optional[BeatmapParser] = None
        self.mapfile: Optional[pyttanko.beatmap] = None
        self.parser: pyttanko.parser = pyttanko.parser()
        self.embed_pp_values: list[str] = []
    
    def convert_difficulty_attrs(self) -> None:
        v = pyttanko.mods_apply(
            mods = self.mods._value_,
            ar = self.ar,
            od = self.od,
            cs = self.cs,
            hp = self.hp,
        )[1:]

        self.ar, self.od, self.cs, self.hp = v
    
    def convert_star_rating(self) -> float:
        m = (Mods.NOMOD, Mods.NOFAIL, Mods.AUTOPILOT, Mods.RELAX, Mods.SPUNOUT)
        if not self.mods in m and self.mode == 0:
            sr = pyttanko.diff_calc().calc(
                self.mapfile, self.mods
            )
            if not sr:
                star_rating = self.difficulty
            else:
                star_rating = sr.total
        else:
            star_rating = self.difficulty
        
        return star_rating

    def set_embed_pp(
        self, 
        mods: Mods = None,
        acc: tuple[Union[float, int]] = (95, 97.5, 100), 
    ) -> None:

        if self.mode != 0:
            return
        
        if not mods:
            mods = self.mods

        self.embed_pp_values = []
        
        stars = pyttanko.diff_calc().calc(self.mapfile, mods._value_)
        for a in acc:
            n300, n100, n50 = pyttanko.acc_round(
                a, len(self.mapfile.hitobjects), 0
            )
            pp = pyttanko.ppv2(
                stars.aim, stars.speed,
                n100 = n100, n50 = n50,
                mods = mods._value_, 
                bmap = self.mapfile,
                n300 = n300, 
            )[0]
            self.embed_pp_values.append(f'{a}%-{pp:.2f}PP')

    @property
    def embed(self) -> Embed:
        e = Embed()

        if not self.creator:
            icon_url = 'https://a.ppy.sh/'
            name = f'{self.song_name} (★{self.difficulty:.2f})'
        else:
            icon_url = self.creator.avatar
            name = f'{self.song_name} (★{self.difficulty:.2f}) by {self.creator.name}'
        
        e.set_author(
            name = name,
            url = self.url,
            icon_url = icon_url,
        )

        e.set_image(
            url = self.cover
        )

        v = (
            f'▸ [osu!](https://osu.ppy.sh/d/{self.setid})\n'
            f'▸ [beatconnect](https://beatconnect.io/b/{self.setid})\n'
            f'▸ [chimu](https://api.chimu.moe/v1/download/{self.setid}?n=1)\n'
            f'▸ [nerina](https://nerina.pw/d/{self.setid})\n'
            f'▸ [sayobot](https://osu.sayobot.cn/osu.php?s={self.setid})'
        )   
        
        diff = (
            f'CS: {self.cs} | AR: {self.ar}\n'
            f'OD: {self.od} | HP: {self.hp}\n'
            f'Max Combo: x{self.max_combo}'
        )

        if self.mode == 0 and self.mapfile:
            if not self.embed_pp_values:
                self.set_embed_pp()
            
            v += f'\n\n**Estimated PP if FC** (with {repr(self.mods)})\n'
            for pp in self.embed_pp_values:
                v += f'{pp}\n'

        e.add_field(
            name = 'Download Links:',
            value = v
        )

        e.add_field(
            name = 'Difficulty:',
            value = diff
        )

        e.set_footer(
            text = f'❤︎ {self.favs} | Last updated: {self.last_updated}'
        )

        return e

    @property
    def url(self) -> str:
        return f'https://osu.ppy.sh/b/{self.id}'
    
    @property
    def cover(self) -> str:
        return f"https://assets.ppy.sh/beatmaps/{self.setid}/covers/cover.jpg"

    @property
    def song_name(self) -> str:
        return f'{self.artist} - {self.title} [{self.version}]'
    
    @classmethod
    async def get_id_from_set(cls, setid: Union[str, int]):
        """Returns the highest difficulty of a set's id"""
        if isinstance(setid, str):
            setid = int(setid)
        
        if setid in glob.cache.beatmap_sets:
            bmap_list = tuple(glob.cache.beatmap_sets[setid].values())
            key = lambda bmap: bmap.difficulty
            bmap = sorted(bmap_list, key = key, reverse = True)[0]
            return bmap
        else:
            base = 'https://osu.ppy.sh/api'
            path = 'get_beatmaps'
            params = {
                'k': config.api_key,
                's': setid,
                'a': 1
            }

            async with glob.http.get(
                url = f'{base}/{path}',
                params = params
            ) as resp:
                if not resp or resp.status != 200:
                    return
                
                if not (json := await resp.json()):
                    return
            
            key = lambda x: float(x['difficultyrating'])
            json: list[dict] = sorted(json, key = key, reverse = True)[0]
        
            return await cls.from_api_dict(json)

    @classmethod
    async def from_api_dict(cls, dictionary: dict):
        bmap_id = int(dictionary['beatmap_id'])
        mode = int(dictionary['mode'])
        key = (bmap_id, mode)
        if key in glob.cache.beatmaps:
            return glob.cache.beatmaps[key]

        bmap = cls()
        bmap.setid = int(dictionary['beatmapset_id'])
        bmap.id = bmap_id
        bmap.total_length = int(dictionary['total_length'])
        bmap.hit_length = int(dictionary['hit_length'])
        bmap.version = dictionary['version']
        bmap.md5 = dictionary['file_md5']
        bmap.cs = float(dictionary['diff_size'])
        bmap.od = float(dictionary['diff_overall'])
        bmap.ar = float(dictionary['diff_approach'])
        bmap.hp = float(dictionary['diff_drain'])
        bmap.mode = mode
        bmap.artist = dictionary['artist']
        bmap.title = dictionary['title']
        bmap.creator = await Player.from_bancho(
            user = dictionary['creator']
        )
        bmap.max_combo = int(dictionary['max_combo'])
        bmap.difficulty = float(dictionary['difficultyrating'])
        bmap.bpm = float(dictionary['bpm'])
        bmap.status = BeatmapStatus(int(dictionary['approved']))
        bmap.favs = int(dictionary['favourite_count'])
        bmap.last_updated = dictionary['last_update']

        data: Optional[str] = None
        url = f'https://osu.ppy.sh/osu/{bmap.id}'
        
        async with glob.http.get(url) as resp:
            if not resp or resp.status != 200:
                pass
            else:
                data = await resp.text()

        if data:
            bmap._mapfile = BeatmapParser(data)
            if bmap.mode == 0:
                bmap.mapfile = bmap.parser.map(
                    osu_file = data.splitlines()
                )
        
        glob.loop.create_task(bmap.add_set_to_cache())
        return bmap

    @classmethod
    async def from_id(cls, bmap_id: int, mode = 0):
        key = (bmap_id, mode)
        if key in glob.cache.beatmaps:
            return glob.cache.beatmaps[key]
        
        bmap = cls()
        base = 'https://osu.ppy.sh/api'
        path = 'get_beatmaps'
        params = {
            'k': config.api_key,
            'b': bmap_id,
            'm': mode,
            'a': 1
        }

        async with glob.http.get(
            url = f'{base}/{path}',
            params = params
        ) as resp:
            if not resp or resp.status != 200:
                return
            
            if not (json := await resp.json()):
                return
        
        json = json[0]
        bmap.setid = int(json['beatmapset_id'])
        bmap.id = bmap_id
        bmap.total_length = int(json['total_length'])
        bmap.hit_length = int(json['hit_length'])
        bmap.version = json['version']
        bmap.md5 = json['file_md5']
        bmap.cs = float(json['diff_size'])
        bmap.od = float(json['diff_overall'])
        bmap.ar = float(json['diff_approach'])
        bmap.hp = float(json['diff_drain'])
        bmap.mode = mode
        bmap.artist = json['artist']
        bmap.title = json['title']
        bmap.creator = await Player.from_bancho(
            user = json['creator']
        )
        bmap.max_combo = int(json['max_combo'])
        bmap.difficulty = float(json['difficultyrating'])
        bmap.bpm = float(json['bpm'])
        bmap.status = BeatmapStatus(int(json['approved']))
        bmap.favs = int(json['favourite_count'])
        bmap.last_updated = json['last_update']

        url = f'https://osu.ppy.sh/osu/{bmap.id}'
        async with glob.http.get(url) as resp:
            if not resp or resp.status != 200:
                return
            
            if not (data := await resp.text()):
                return

            bmap._mapfile = BeatmapParser(data)
            if bmap.mode == 0:
                bmap.mapfile = bmap.parser.map(
                    osu_file = data.splitlines()
                )
        
        glob.loop.create_task(bmap.add_set_to_cache())

        return bmap
    
    def add_map_to_cache(self) -> None:
        glob.cache.beatmaps[(self.id, self.mode)] = self

    async def add_set_to_cache(self) -> None:
        if (self.id, self.mode) in glob.cache.beatmaps:
            return # This means we already have the whole set in cache

        self.add_map_to_cache()

        base = 'https://osu.ppy.sh/api'
        path = 'get_beatmaps'
        params = {
            'k': config.api_key,
            's': self.setid,
            'm': self.mode,
            'a': 1
        }

        async with glob.http.get(
            f'{base}/{path}', 
            params = params
        ) as resp:
            
            if not resp or resp.status != 200:
                return
            
            if not (json := await resp.json()):
                return
        
        set_dict = {}
        for bmap_dict in json:
            key = (int(bmap_dict['beatmap_id']), self.mode)
            if key in glob.cache.beatmaps:
                continue
            
            bmap: Beatmap = await Beatmap.from_api_dict(bmap_dict)
            if not bmap:
                continue
        
            bmap.add_map_to_cache()
            set_dict[bmap.id] = bmap
        
        glob.cache.beatmap_sets[(self.setid, self.mode)] = set_dict
        glob.cache.beatmap_sets[self.setid] = set_dict
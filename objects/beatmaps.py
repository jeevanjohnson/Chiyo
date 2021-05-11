import config
from ext import glob
from discord import Embed
from objects.players import Player
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
        self.creator: str
        self.max_combo: int
        self.difficulty: float
        self.bpm: float
        self.status: int
        self.mapfile: BeatmapParser
    
    @property
    def embed(self) -> Embed:
        e = Embed()

        e.set_author(
            name = f'{self.song_name} ★{self.difficulty:.2f}'
        )

        e.set_image(
            url = self.cover
        )

        v = (
            f'▸ [osu!](https://osu.ppy.sh/b/{self.id})\n'
            f'▸ [osu! (old)](https://old.ppy.sh/s/{self.id})\n'
            f'▸ [osu!gatari](https://osu.gatari.pw/b/{self.id})\n'
        )
        e.add_field(
            name = 'Download Links:',
            value = v
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
    async def from_id(cls, bmap_id: int, mode = 0):
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
        bmap.id = int(json['beatmap_id'])
        bmap.total_length = int(json['total_length'])
        bmap.hit_length = int(json['hit_length'])
        bmap.version = json['version']
        bmap.md5 = json['file_md5']
        bmap.cs = float(json['diff_size'])
        bmap.od = float(json['diff_overall'])
        bmap.ar = float(json['diff_approach'])
        bmap.hp = float(json['diff_drain'])
        bmap.mode = int(json['mode'])
        bmap.artist = json['artist']
        bmap.title = json['title']
        bmap.creator = await Player.from_bancho(
            user = json['creator']
        )
        bmap.max_combo = int(json['max_combo'])
        bmap.difficulty = float(json['difficultyrating'])
        bmap.bpm = float(json['bpm'])
        bmap.status = int(json['approved'])

        url = f'https://osu.ppy.sh/osu/{bmap.id}'
        async with glob.http.get(url) as resp:
            bmap.mapfile = BeatmapParser(await resp.text())

        return bmap
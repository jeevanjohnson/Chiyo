import config
import pyttanko
from ext import glob
from discord import Embed
from objects.const import Mods
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
        self.creator: Player
        self.max_combo: int
        self.difficulty: float
        self.bpm: float
        self.status: int
        self.favs: int
        self.last_updated: str
        self.mapfile: pyttanko.beatmap
        self._mapfile: BeatmapParser
        self.parser: pyttanko.parser = pyttanko.parser()
        self.mods: Mods = Mods.NOMOD
    
    def convert_diff(self) -> None:
        v = pyttanko.mods_apply(
            mods = self.mods.value,
            ar = self.ar,
            od = self.od,
            cs = self.cs,
            hp = self.hp,
        )[1:]

        self.ar, self.od, self.cs, self.hp = v
    
    @property
    def embed(self) -> Embed:
        e = Embed()

        e.set_author(
            url = self.url,
            icon_url = self.creator.avatar,
            name = f'{self.song_name} (★{self.difficulty:.2f}) by {self.creator.name}'
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
        bmap.id = bmap_id
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

        return bmap
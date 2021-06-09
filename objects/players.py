import config
from ext import glob
from typing import Union
from helpers import note
from discord import Embed
from objects.const import Server
from objects.const import magnitude_fmt

class Player:
    def __init__(self) -> None:
        self.id: int
        self.name: str
        self.join_date: str
        self.pcount: int
        self.ranked_score: int
        self.total_score: int
        self.pp: float
        self.level: float
        self.rank: int
        self.acc: float
        self.country: str
        self.country_rank: int
        self.server: Server
    
    @property
    def country_url(self) -> str:
        return f'https://www.countryflags.io/{self.country}/flat/64.png'
    
    @property
    def avatar(self) -> str:
        return (
            f'https://a.ppy.sh/{self.id}',
            f'https://a.akatsuki.pw/{self.id}'
        )[self.server.value]
    
    @property
    def url(self) -> str:
        return (
            f'https://osu.ppy.sh/u/{self.id}',
            f'https://akatsuki.pw/u/{self.id}'
        )[self.server.value]

    @property
    def embed(self) -> Embed:
        pdict = self.__dict__

        if self.country:
            country_rank = ' ({country}#{country_rank})'
        else:
            country_rank = ''
        
        ranked_score = magnitude_fmt(self.ranked_score)
        data = (
            '▸ Official Rank: #{rank}' f'{country_rank}\n'
            '▸ Level: {level:.2f}\n'
            '▸ Total PP: {pp:.0f} \n'
            '▸ Accuracy: {acc:.2f}% \n'
            '▸ Playcount: {pcount}\n'
            f'▸ Ranked Score: {ranked_score}'
        )
        e = Embed(
            description = data.format(**pdict)
        )

        e.set_author(
            name = f'osu! {self.server.name} Profile for {self.name}',
            icon_url = self.country_url,
            url = self.url
        )

        e.set_thumbnail(
            url = self.avatar
        )

        join_date = self.join_date.replace('Z', ' ').replace('T', ' ')
        e.set_footer(
            text = f'Registered on {join_date}'
        )

        return e

    @classmethod
    async def from_bancho(
        cls, 
        user: Union[str, int], 
        mode: int = 0
    ):
        p = cls()
        base = 'https://osu.ppy.sh/api'
        path = 'get_user'
        params = {
            'k': config.api_key,
            'u': user,
            'm': mode,
            'type': 'string' if isinstance(user, str) else 'id'
        }

        async with glob.http.get(
            url = f'{base}/{path}', 
            params = params
        ) as resp:
            if not resp or resp.status != 200:
                await note(
                    statement = "if not resp or resp.status != 200",
                    user = user, 
                    mode = mode, 
                    function = 'Player.from_bancho'
                )
                return
            
            if not (json := await resp.json()):
                await note(
                    statement = "if not (json := await resp.json())",
                    user = user, 
                    mode = mode, 
                    function = 'Player.from_bancho'
                )
                return
        
        json = json[0]
        p.id = int(json['user_id'] or 0)
        p.name = json['username']
        p.join_date = json['join_date']
        p.pcount = int(json['playcount'] or 0)
        p.ranked_score = int(json['ranked_score'] or 0)
        p.total_score = int(json['total_score'] or 0)
        p.pp = float(json['pp_raw'] or 0)
        p.level = float(json['level'] or 0)
        p.rank = int(json['pp_rank'] or 0)
        p.acc = float(json['accuracy'] or 0)
        p.country = json['country']
        p.country_rank = int(json['pp_country_rank'] or 0)
        p.server = Server.Bancho

        return p

    @classmethod
    async def from_akatsuki(
        cls, 
        user: Union[str, int], 
        mode: int = 0, 
        relax: int = 0
    ):
        p = cls()
        base = 'https://akatsuki.pw/api/v1'
        path = '/users/full'
        params = {
            'name' if isinstance(user, str) else 'id': user, 
        }

        async with glob.http.get(
            url = f'{base}/{path}', 
            params = params
        ) as resp:
            if not resp or resp.status != 200:
                await note(
                    statement = "if not resp or resp.status != 200",
                    user = user, mode = mode, 
                    relax = bool(relax), function = 'Player.from_akatsuki'
                )
                return
            
            if not (json := await resp.json()):
                await note(
                    statement = "if not (json := await resp.json())",
                    user = user, mode = mode, 
                    relax = bool(relax), function = 'Player.from_akatsuki'
                )
                return
        
        m = ('std', 'taiko', 'ctb', 'mania')[mode]
        stats = json['stats'][relax][m]
        p.id = json['id']
        p.name = json['username']
        p.join_date = json['registered_on']
        p.pcount = stats['playcount']
        p.ranked_score = stats['ranked_score']
        p.total_score = stats['total_score']
        p.pp = stats['pp']
        p.level = stats['level']
        p.rank = stats['global_leaderboard_rank']
        p.acc = stats['accuracy']
        p.country = json['country']
        p.country_rank = stats['country_leaderboard_rank']
        p.server = Server.Akatsuki

        return p
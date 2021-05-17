import math
import config
import pyttanko
from ext import glob
from typing import Union
from discord import Embed
from objects.const import Mods
from objects.players import Player
from objects.beatmaps import Beatmap

class OsuCard:
    def __init__(self) -> None:
        self.player: Player
        self.aim: float = 0.0
        self.speed: float = 0.0
        self.acc: float = 0.0
    
    @property
    def embed(self) -> Embed:
        e = Embed()

        e.set_author(
            url = self.player.url,
            icon_url = self.player.country_url,
            name = f'osu! card for {self.player.name}'
        )

        e.set_thumbnail(
            url = self.player.avatar
        )

        e.add_field(
            name = 'Aim:',
            value = f'{self.aim:.0f}'
        )

        e.add_field(
            name = 'Speed:',
            value = f'{self.speed:.0f}'
        )

        e.add_field(
            name = 'Accuracy:',
            value = f'{self.acc:.0f}'
        )

        return e
    
    @staticmethod
    def calc_acc(
        mode: int, n300: int, 
        n100: int, n50: int, 
        misses: int, nkatsu: int, 
        ngeki: int
    ):
        if mode == 0: # osu!
            total = sum((n300, n100, n50, misses))

            if total == 0:
                acc = 0.0
                return acc

            acc = 100.0 * sum((
                n50 * 50.0,
                n100 * 100.0,
                n300 * 300.0
            )) / (total * 300.0)

            return acc

        elif mode == 1: # osu!taiko
            total = sum((n300, n100, misses))

            if total == 0:
                acc = 0.0
                return acc

            acc = 100.0 * sum((
                n100 * 0.5,
                n300
            )) / total

            return acc

        elif mode == 2:
            # osu!catch
            total = sum((n300, n100, n50,
                         nkatsu, misses))

            if total == 0:
                acc = 0.0
                return acc

            acc = 100.0 * sum((
                n300,
                n100,
                n50
            )) / total
            
            return acc

        elif mode == 3:
            # osu!mania
            total = sum((n300, n100, n50,
                         ngeki, nkatsu, misses))

            if total == 0:
                acc = 0.0
                return acc

            acc = 100.0 * sum((
                n50 * 50.0,
                n100 * 100.0,
                nkatsu * 200.0,
                (n300 + ngeki) * 300.0
            )) / (total * 300.0)

            return acc

    @staticmethod
    def calc_std_value(stars, **kwargs) -> tuple[float, float, float]:
        """Calculate speed/acc/aim values for a score."""
        cs: float = kwargs['cs']
        bpm: float = kwargs['bpm']
        ar: float = kwargs['ar']
        od: float = kwargs['od']
        hp: float = kwargs['hp']
        acc: float = kwargs['acc']
        bmap: Beatmap = kwargs['bmap']
        combo: int = kwargs['combo']
        mods: Mods = kwargs['mods']

        aim = (
            stars.aim * (math.pow(cs, 0.1) / math.pow(4, 0.1))
        ) * 2

        speed = (
            stars.speed * 
            (math.pow(bpm, 0.09) / math.pow(180, 0.09)) * 
            (math.pow(ar, 0.1) / math.pow(6, 0.1))
        ) * 2

        final_aim = aim
        final_speed = speed

        unbalance_limit = (
            abs(aim - speed)) > (math.pow(5, math.log(aim + speed) / math.log(1.7)) / 2940
        )

        if mods & (Mods.DOUBLETIME | Mods.NIGHTCORE) and unbalance_limit:
            aim /= 1.06
            speed /= 1.06

        acc = (
            math.pow(aim / 2, (math.pow(acc, 2.5) / math.pow(100, 2.5)) * (0.083 *
            math.log10(stars.nsingles * 900000000) * (math.pow(1.42, combo / bmap.max_combo) - 0.3))) + 
            math.pow(speed / 2, (math.pow(acc, 2.5) / math.pow(100, 2.5)) * (0.0945 *
            math.log10(stars.nsingles * 900000000) * (math.pow(1.35, combo / bmap.max_combo) - 0.3))) * 
            (math.pow(od, 0.02) / math.pow(6, 0.02)) * (math.pow(hp, 0.02) / (math.pow(6, 0.02)))
        )

        if mods & Mods.FLASHLIGHT:
            acc *= (0.095 * math.log10(stars.nsingles * 900000000))

        return final_aim, final_speed, acc

    @classmethod
    async def from_bancho(
        cls, user: Union[str, int], 
        mode = 0,
    ):
        card = cls()
        base = 'https://osu.ppy.sh/api'
        path = 'get_user_best'
        params = {
            'k': config.api_key,
            'u': user,
            'm': mode,
            'limit': 100,
            'type': 'string' if isinstance(user, str) else 'id'
        }

        card.player = await Player.from_bancho(
            user, mode
        )

        if not card.player:
            return

        async with glob.http.get(
            url = f'{base}/{path}',
            params = params
        ) as resp:
            if not resp or resp.status != 200:
                return
            
            if not (json := await resp.json()):
                return
        
        for play in json:
            bid = int(play['beatmap_id'])
            if bid in glob.cache.beatmaps:
                bmap = glob.cache.beatmaps[bid]
            else:
                bmap = await Beatmap.from_id(
                    bmap_id = bid,
                    mode = mode
                )

                if not bmap:
                    continue

                glob.cache.beatmaps[bid] = bmap

            mods = Mods(int(play['enabled_mods']))
            stars = pyttanko.diff_calc().calc(
                bmap = bmap.mapfile,
                mods = mods.value
            )
            
            # convert bpm, ar, od, cs, hp to 
            # values depending on the mods
            if mods & Mods.DOUBLETIME:
                bpm = bmap.bpm * 1.5
            elif mods & Mods.HALFTIME:
                bpm = bmap.bpm * 0.75
            else:
                bpm = bmap.bpm

            ar, od, cs, hp = pyttanko.mods_apply(
                mods = mods.value,
                ar = bmap.ar,
                od = bmap.od,
                cs = bmap.cs,
                hp = bmap.hp,
            )[1:]

            n300 = int(play['count300'])
            n100 = int(play['count100'])
            n50 = int(play['count50'])
            misses = int(play['countmiss'])
            nkatsu = int(play['countkatu'])
            ngeki = int(play['countgeki'])
            acc = OsuCard.calc_acc(
                mode, n300, n100, 
                n50, misses, nkatsu, 
                ngeki
            )

            if mode == 0:
                values = OsuCard.calc_std_value(
                    stars, ar = ar,
                    od = od, cs = cs,
                    hp = hp, acc = acc,
                    bmap = bmap, bpm = bpm,
                    combo = int(play['maxcombo']),
                    mods = mods
                )
            elif mode == 1:
                ...
            elif mode == 2:
                ...
            elif mode == 3:
                ...
            
            aim, speed, acc = values
            card.aim += aim
            card.speed += speed
            card.acc += acc

        return card
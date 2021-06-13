from enum import unique
from enum import IntEnum
from enum import IntFlag
from typing import Union
from textwrap import wrap

BOT_OWNER_ID = 828821094559514684

GRADE_URLS = {
    'SSH': 'https://cdn.discordapp.com/emojis/724849277406281728.png?v=1',
    'SHD': 'https://cdn.discordapp.com/emojis/724847645142810624.png?v=1',
    'XH': 'https://cdn.discordapp.com/emojis/724849277406281728.png?v=1',
    'SH': 'https://cdn.discordapp.com/emojis/724847645142810624.png?v=1',
    'SS': 'https://cdn.discordapp.com/emojis/724849299300548680.png?v=1',
    'X': 'https://cdn.discordapp.com/emojis/724849299300548680.png?v=1',
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

        if not self:
            return 'NM'

        # dt/nc is a special case, as osu! will send
        # the mods as 'DTNC' while only NC is applied.
        if self & Mods.NIGHTCORE:
            self &= ~Mods.DOUBLETIME

        return ''.join(v for k, v in mod_to_str.items() if self & k)

    @classmethod
    def from_str(cls, s: str):
        final_mods = 0
        for m in wrap(s, 2):
            if m not in str_to_mod:
                continue
            
            final_mods += str_to_mod[m]
        
        return cls(final_mods)

str_to_mod = {
    'nm': Mods.NOMOD,
    'ez': Mods.EASY,
    'td': Mods.TOUCHSCREEN,
    'hd': Mods.HIDDEN,
    'hr': Mods.HARDROCK,
    'sd': Mods.SUDDENDEATH,
    'dt': Mods.DOUBLETIME,
    'rx': Mods.RELAX,
    'ht': Mods.HALFTIME,
    'nc': Mods.NIGHTCORE,
    'fl': Mods.FLASHLIGHT,
    'au': Mods.AUTOPLAY,
    'so': Mods.SPUNOUT,
    'ap': Mods.AUTOPILOT,
    'pf': Mods.PERFECT,
    'k1': Mods.KEY1, 
    'k2': Mods.KEY2, 
    'k3': Mods.KEY3, 
    'k4': Mods.KEY4, 
    'k5': Mods.KEY5, 
    'k6': Mods.KEY6, 
    'k7': Mods.KEY7, 
    'k8': Mods.KEY8, 
    'k9': Mods.KEY9,
    'fi': Mods.FADEIN,
    'rn': Mods.RANDOM,
    'cn': Mods.CINEMA,
    'tp': Mods.TARGET,
    'v2': Mods.SCOREV2,
    'co': Mods.KEYCOOP,
    'mi': Mods.MIRROR
}

mod_to_str = {
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

@unique
class Server(IntEnum):
    Bancho = 0
    Akatsuki = 1

    @property
    def name(self) -> str:
        return (
            'Bancho',
            'Akatsuki'
        )[self._value_]

    def __repr__(self) -> str:
        return (
            '<Bancho (osu.ppy.sh)>',
            '<Akatsuki (akatsuki.pw)>'
        )[self._value_]
    
    @classmethod
    def from_name(cls, name: str):
        return {
            'bancho': cls.Bancho,
            'akatsuki': cls.Akatsuki
        }[name.lower()]

def magnitude_fmt(num: Union[int, float]) -> str:
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num = num / 1000
    
    m = ['', 'K', 'M', 'B', 'T', 'Q'][magnitude]
    return f'{num:,.2f}{m}'
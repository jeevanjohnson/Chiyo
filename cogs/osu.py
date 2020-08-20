import discord
from discord.ext import commands
import requests
import os
import akatsukiapi
import Chiyo

collation = Chiyo.collation
global cache
# 0 = guild id | 1 = channel id | 2 = beatmap id | 3 = mode
# 4 = beatmap set id | 5 = songname | 6 = userid | 7 = difficulty
# 8 = ar | 9 = od | 10 = full combo | 11 = rx will be 1 no rx will be 0
cache = ['','','','','','','','','','','','']

class Akatsuki(commands.Cog):

    def __int__(self, client):
        self.client = client

    @commands.command()
    async def reg(self, ctx, *args):
        """reg profile
        """
        completemessage = len(args)
        if ctx.message.mentions:
            b = collation.find_one({"_id": ctx.message.mentions[0].id})
            if b == None: 
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
        elif completemessage == 0:
            b = collation.find_one({"_id": ctx.message.author.id})
            if b == None: 
                return await ctx.send("User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
        else: 
            c = '{}'.format(' '.join(args))
        
        info = akatsukiapi.stats(c)
        if info == 'error':
            return await ctx.send(f"User couldn't be found for {c}!")
        userid = info[12]
        username = info[0]
        official_rank = info[9]
        country = info[11]
        country_rank = info[10]
        level = info[6]
        pp = info[8]
        accuracy = info[7]
        playcount = info[3]
        embed=discord.Embed(description=f'▸ Official Rank: {official_rank} ({country}#{country_rank}) \n▸ Level: {level}\n▸ Total PP: {pp} \n▸ Accuracy: {accuracy}% \n▸ Playcount: {playcount}', color=0xb6ebf1)
        embed.set_author(name=f"osu! Standard Profile for {username.replace('ygfviasfa',' ')} ", url=f"https://akatsuki.pw/u/{userid}", icon_url=f"https://avatars0.githubusercontent.com/u/45724130?s=200&v=4.png")
        embed.set_thumbnail(url=f"https://a.akatsuki.pw/{userid}.png")
        embed.set_footer(text=f"Player on Akatsuki!")
        return await ctx.send(embed=embed)

    @commands.command()
    async def rx(self, ctx, *args):
        """relax profile
        """
        completemessage = len(args)
        if ctx.message.mentions:
            b = collation.find_one({"_id": ctx.message.mentions[0].id})
            if b == None: 
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
        elif completemessage == 0:
            b = collation.find_one({"_id": ctx.message.author.id})
            if b == None: 
                return await ctx.send("User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
        else: 
            c = '{}'.format(' '.join(args))

        info = akatsukiapi.relaxstats(c)
        if info == 'error':
            return await ctx.send(f"User couldn't be found for {c}!")
        userid = info[12]
        username = info[0]
        official_rank = info[9]
        country = info[11]
        country_rank = info[10]
        level = info[6]
        pp = info[8]
        accuracy = info[7]
        playcount = info[3]
        embed=discord.Embed(description=f'▸ Official Rank: {official_rank} ({country}#{country_rank}) \n▸ Level: {level}\n▸ Total PP: {pp} \n▸ Accuracy: {accuracy}% \n▸ Playcount: {playcount}', color=0xb6ebf1)
        embed.set_author(name=f"osu! Relax Standard Profile for {username.replace('ygfviasfa',' ')} ", url=f"https://akatsuki.pw/u/{userid}", icon_url=f"https://avatars0.githubusercontent.com/u/45724130?s=200&v=4.png")
        embed.set_thumbnail(url=f"https://a.akatsuki.pw/{userid}.png")
        embed.set_footer(text=f"Player on Akatsuki!")
        return await ctx.send(embed=embed)

    @commands.command()
    async def trx(self, ctx, *args):
        """relax taiko profile
        """
        completemessage = len(args)
        if ctx.message.mentions:
            b = collation.find_one({"_id": ctx.message.mentions[0].id})
            if b == None: 
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
        elif completemessage == 0:
            b = collation.find_one({"_id": ctx.message.author.id})
            if b == None: 
                return await ctx.send("User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
        else: 
            c = '{}'.format(' '.join(args))
        
        info = akatsukiapi.relaxtaikostats(c)
        if info == 'error':
            return await ctx.send(f"User couldn't be found for {c}!")
        userid = info[12]
        username = info[0]
        official_rank = info[9]
        country = info[11]
        country_rank = info[10]
        level = info[6]
        pp = info[8]
        accuracy = info[7]
        playcount = info[3]
        embed=discord.Embed(description=f'▸ Official Rank: {official_rank} ({country}#{country_rank}) \n▸ Level: {level}\n▸ Total PP: {pp} \n▸ Accuracy: {accuracy}% \n▸ Playcount: {playcount}', color=0xb6ebf1)
        embed.set_author(name=f"osu! Relax Taiko Profile for {username.replace('ygfviasfa',' ')}", url=f"https://akatsuki.pw/u/{userid}", icon_url=f"https://avatars0.githubusercontent.com/u/45724130?s=200&v=4.png")
        embed.set_thumbnail(url=f"https://a.akatsuki.pw/{userid}.png")
        embed.set_footer(text=f"Player on Akatsuki!")
        return await ctx.send(embed=embed)

    @commands.command()
    async def rt(self, ctx, *args):
        """reg taiko profile
        """
        completemessage = len(args)
        if ctx.message.mentions:
            b = collation.find_one({"_id": ctx.message.mentions[0].id})
            if b == None: 
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
        elif completemessage == 0:
            b = collation.find_one({"_id": ctx.message.author.id})
            if b == None: 
                return await ctx.send("User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
        else: 
            c = '{}'.format(' '.join(args))
        
        info = akatsukiapi.taikostats(c)
        if info == 'error':
            return await ctx.send(f"User couldn't be found for {c}!")
        userid = info[12]
        username = info[0]
        official_rank = info[9]
        country = info[11]
        country_rank = info[10]
        level = info[6]
        pp = info[8]
        accuracy = info[7]
        playcount = info[3]
        embed=discord.Embed(description=f'▸ Official Rank: {official_rank} ({country}#{country_rank}) \n▸ Level: {level}\n▸ Total PP: {pp} \n▸ Accuracy: {accuracy}% \n▸ Playcount: {playcount}', color=0xb6ebf1)
        embed.set_author(name=f"osu! Taiko Profile for {username.replace('ygfviasfa',' ')} ", url=f"https://akatsuki.pw/u/{userid}", icon_url=f"https://avatars0.githubusercontent.com/u/45724130?s=200&v=4.png")
        embed.set_thumbnail(url=f"https://a.akatsuki.pw/{userid}.png")
        embed.set_footer(text=f"Player on Akatsuki!")
        return await ctx.send(embed=embed)

    @commands.command()
    async def r(self, ctx, *args):
        """recent score
        """
        completemessage = len(args)
        if ctx.message.mentions:
            b = collation.find_one({"_id": ctx.message.mentions[0].id})
            if b == None: 
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
        elif completemessage == 0:
            b = collation.find_one({"_id": ctx.message.author.id})
            if b == None: 
                return await ctx.send(f"User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
        else: 
            c = '{}'.format(' '.join(args))
        
        ababa = akatsukiapi.stats(c)
        if ababa == 'error':
            return await ctx.send(f"User couldn't be found for {c}!")
        info = akatsukiapi.recent(c)
        if info == 'error':
            return await ctx.send(f"User couldn't be found for {c}!")
        userid = ababa[12]
        username = ababa[0]
        score = info[0]
        max_combo = info[1]
        full_combo = info[2]
        mods = info[3]
        count_300 = info[4]
        count_100 = info[5]
        count_50 = info[6]
        count_miss = info[7]
        accuracy = info[8]
        pp = info[9]
        rank = info[10]
        completed = info[11]
        beatmap_id = info[12]
        beatmapset_id = info[13]
        ar = info[14]
        od = info[15]
        difficulty = info[16]

        cache[0] = ctx.guild.id
        cache[1] = ctx.message.channel.id
        cache[2] = beatmap_id
        cache[3] = 0
        cache[4] = beatmapset_id
        cache[6] = userid
        cache[7] = difficulty
        cache[8] = ar
        cache[9] = od
        cache[10] = full_combo
        cache[11] = 0

        lol = requests.get(f'https://akatsuki.pw/api/v1/users/scores/recent?rx=0&name={c}&mode=0')
        if not lol:
            return await ctx.send(f"User couldn't be found for {c}!")
        songname = lol.json()['scores'][0]['beatmap']['song_name']

        cache[5] = songname
        #nope

        embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR: {ar} OD: {od}] ▸ {accuracy}%\n▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{count_300}/{count_100}/{count_50}/{count_miss}]\n▸ Map Completed: {completed}', color=0xb6ebf1)
        embed.set_author(name=f"{songname} +{mods} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmap_id}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
        embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapset_id}l.jpg")
        embed.set_footer(text=f"Most Recent osu! Standard Play for {username.replace('ygfviasfa',' ')} ")
        await ctx.send(embed=embed)

    @commands.command()
    async def rxr(self, ctx, *args):
        """recent relax score
        """
        completemessage = len(args)
        if ctx.message.mentions:
            b = collation.find_one({"_id": ctx.message.mentions[0].id})
            if b == None: 
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
        elif completemessage == 0:
            b = collation.find_one({"_id": ctx.message.author.id})
            if b == None: 
                return await ctx.send(f"User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
        else: 
            c = '{}'.format(' '.join(args))
        
        ababa = akatsukiapi.stats(c)
        if ababa == 'error':
            return await ctx.send(f"User couldn't be found for {c}!")
        info = akatsukiapi.relaxrecent(c)
        if info == 'error':
            return await ctx.send(f"User couldn't be found for {c}!")
        userid = ababa[12]
        username = ababa[0]
        score = info[0]
        max_combo = info[1]
        full_combo = info[2]
        mods = info[3]
        count_300 = info[4]
        count_100 = info[5]
        count_50 = info[6]
        count_miss = info[7]
        accuracy = info[8]
        pp = info[9]
        rank = info[10]
        completed = info[11]
        beatmap_id = info[12]
        beatmapset_id = info[13]
        ar = info[14]
        od = info[15]
        difficulty = info[16]

        lol = requests.get(f'https://akatsuki.pw/api/v1/users/scores/recent?rx=1&name={c}&mode=0')
        if not lol:
            return await ctx.send(f"User couldn't be found for {c}!")
        songname = lol.json()['scores'][0]['beatmap']['song_name']

        embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR: {ar} OD: {od}] ▸ {accuracy}%\n▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{count_300}/{count_100}/{count_50}/{count_miss}]\n▸ Map Completed: {completed}', color=0xb6ebf1)
        embed.set_author(name=f"{songname} +{mods} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmap_id}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
        embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapset_id}l.jpg")
        embed.set_footer(text=f"Most Recent osu! Relax Standard Play for {username.replace('ygfviasfa',' ')} ")
        await ctx.send(embed=embed)

    @commands.command()
    async def tr(self, ctx, *args):
        """recent taiko score
        """
        completemessage = len(args)
        if ctx.message.mentions:
            b = collation.find_one({"_id": ctx.message.mentions[0].id})
            if b == None: 
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
        elif completemessage == 0:
            b = collation.find_one({"_id": ctx.message.author.id})
            if b == None: 
                return await ctx.send(f"User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
        else: 
            c = '{}'.format(' '.join(args))
        
        ababa = akatsukiapi.stats(c)
        if ababa == 'error':
            return await ctx.send(f"User couldn't be found for {c}!")
        info = akatsukiapi.taikorecent(c)
        if info == 'error':
            return await ctx.send(f"User couldn't be found for {c}!")
        userid = ababa[12]
        username = ababa[0]
        score = info[0]
        max_combo = info[1]
        full_combo = info[2]
        mods = info[3]
        count_300 = info[4]
        count_100 = info[5]
        count_50 = info[6]
        count_miss = info[7]
        accuracy = info[8]
        pp = info[9]
        rank = info[10]
        completed = info[11]
        beatmap_id = info[12]
        beatmapset_id = info[13]
        ar = info[14]
        od = info[15]
        difficulty = info[16]

        cache[0] = ctx.guild.id
        cache[1] = ctx.message.channel.id
        cache[2] = beatmap_id
        cache[3] = 1
        cache[4] = beatmapset_id
        cache[6] = userid
        cache[7] = difficulty
        cache[8] = ar
        cache[9] = od
        cache[10] = full_combo
        cache[11] = 0

        lol = requests.get(f'https://akatsuki.pw/api/v1/users/scores/recent?rx=0&name={c}&mode=1')
        if not lol:
            return await ctx.send(f"User couldn't be found for {c}!")
        songname = lol.json()['scores'][0]['beatmap']['song_name']

        cache[5] = songname

        embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR: {ar} OD: {od}] ▸ {accuracy}%\n▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{count_300}/{count_100}/{count_50}/{count_miss}]\n▸ Map Completed: {completed}', color=0xb6ebf1)
        embed.set_author(name=f"{songname} +{mods} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmap_id}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
        embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapset_id}l.jpg")
        embed.set_footer(text=f"Most Recent osu! Taiko Play for {username.replace('ygfviasfa',' ')} ")
        await ctx.send(embed=embed)

    @commands.command()
    async def rxtr(self, ctx, *args):
        """relax taiko recent score
        """
        completemessage = len(args)
        if ctx.message.mentions:
            b = collation.find_one({"_id": ctx.message.mentions[0].id})
            if b == None: 
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
        elif completemessage == 0:
            b = collation.find_one({"_id": ctx.message.author.id})
            if b == None: 
                return await ctx.send(f"User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
        else: 
            c = '{}'.format(' '.join(args))
        
        ababa = akatsukiapi.stats(c)
        if ababa == 'error':
            return await ctx.send(f"User couldn't be found for {c}!")
        info = akatsukiapi.relaxtaikorecent(c)
        if info == 'error':
            return await ctx.send(f"User couldn't be found for {c}!")
        userid = ababa[12]
        username = ababa[0]
        score = info[0]
        max_combo = info[1]
        full_combo = info[2]
        mods = info[3]
        count_300 = info[4]
        count_100 = info[5]
        count_50 = info[6]
        count_miss = info[7]
        accuracy = info[8]
        pp = info[9]
        rank = info[10]
        completed = info[11]
        beatmap_id = info[12]
        beatmapset_id = info[13]
        ar = info[14]
        od = info[15]
        difficulty = info[16]

        cache[0] = ctx.guild.id
        cache[1] = ctx.message.channel.id
        cache[2] = beatmap_id
        cache[3] = 1
        cache[4] = beatmapset_id
        cache[6] = userid
        cache[7] = difficulty
        cache[8] = ar
        cache[9] = od
        cache[10] = full_combo
        cache[11] = 1

        lol = requests.get(f'https://akatsuki.pw/api/v1/users/scores/recent?rx=1&name={c}&mode=1')
        if not lol:
            return await ctx.send(f"User couldn't be found for {c}!")
        songname = lol.json()['scores'][0]['beatmap']['song_name']

        cache[5] = songname

        embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR: {ar} OD: {od}] ▸ {accuracy}%\n▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{count_300}/{count_100}/{count_50}/{count_miss}]\n▸ Map Completed: {completed}', color=0xb6ebf1)
        embed.set_author(name=f"{songname} +{mods} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmap_id}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
        embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapset_id}l.jpg")
        embed.set_footer(text=f"Most Recent osu! Relax Taiko Play for {username.replace('ygfviasfa',' ')} ")
        await ctx.send(embed=embed)

    @commands.command()
    async def t(self, ctx, *args):
        """top play
        """
        completemessage = len(args)
        if ctx.message.mentions:
            b = collation.find_one({"_id": ctx.message.mentions[0].id})
            if b == None: 
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
        elif completemessage == 0:
            b = collation.find_one({"_id": ctx.message.author.id})
            if b == None: 
                return await ctx.send(f"User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
        else: 
            c = '{}'.format(' '.join(args))
        
        ababa = akatsukiapi.stats(c)
        if ababa == 'error':
            return await ctx.send(f"User couldn't be found for {c}!")
        info = akatsukiapi.top(c)
        if info == 'error':
            return await ctx.send(f"User couldn't be found for {c}!")
        userid = ababa[12]
        username = ababa[0]
        score = info[0]
        max_combo = info[1]
        full_combo = info[2]
        mods = info[3]
        count_300 = info[4]
        count_100 = info[5]
        count_50 = info[6]
        count_miss = info[7]
        accuracy = info[8]
        pp = info[9]
        rank = info[10]
        completed = info[11]
        beatmap_id = info[12]
        beatmapset_id = info[13]
        ar = info[14]
        od = info[15]
        difficulty = info[16]

        cache[0] = ctx.guild.id
        cache[1] = ctx.message.channel.id
        cache[2] = beatmap_id
        cache[3] = 0
        cache[4] = beatmapset_id
        cache[6] = userid
        cache[7] = difficulty
        cache[8] = ar
        cache[9] = od
        cache[10] = full_combo
        cache[11] = 0

        lol = requests.get(f'https://akatsuki.pw/api/v1/users/scores/best?rx=0&name={c}&mode=0')
        if not lol:
            return await ctx.send(f"User couldn't be found for {c}!")
        songname = lol.json()['scores'][0]['beatmap']['song_name']

        cache[5] = songname
        #nope

        embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR: {ar} OD: {od}] ▸ {accuracy}%\n▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{count_300}/{count_100}/{count_50}/{count_miss}]\n▸ Map Completed: {completed}', color=0xb6ebf1)
        embed.set_author(name=f"{songname} +{mods} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmap_id}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
        embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapset_id}l.jpg")
        embed.set_footer(text=f"Top osu! Standard Play for {username.replace('ygfviasfa',' ')} ")
        await ctx.send(embed=embed)

    @commands.command()
    async def rxt(self, ctx, *args):
        """relax top play
        """
        completemessage = len(args)
        if ctx.message.mentions:
            b = collation.find_one({"_id": ctx.message.mentions[0].id})
            if b == None: 
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
        elif completemessage == 0:
            b = collation.find_one({"_id": ctx.message.author.id})
            if b == None: 
                return await ctx.send(f"User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
        else: 
            c = '{}'.format(' '.join(args))
        
        ababa = akatsukiapi.stats(c)
        if ababa == 'error':
            return await ctx.send(f"User couldn't be found for {c}!")
        info = akatsukiapi.relaxtop(c)
        if info == 'error':
            return await ctx.send(f"User couldn't be found for {c}!")
        userid = ababa[12]
        username = ababa[0]
        score = info[0]
        max_combo = info[1]
        full_combo = info[2]
        mods = info[3]
        count_300 = info[4]
        count_100 = info[5]
        count_50 = info[6]
        count_miss = info[7]
        accuracy = info[8]
        pp = info[9]
        rank = info[10]
        completed = info[11]
        beatmap_id = info[12]
        beatmapset_id = info[13]
        ar = info[14]
        od = info[15]
        difficulty = info[16]

        cache[0] = ctx.guild.id
        cache[1] = ctx.message.channel.id
        cache[2] = beatmap_id
        cache[3] = 0
        cache[4] = beatmapset_id
        cache[6] = userid
        cache[7] = difficulty
        cache[8] = ar
        cache[9] = od
        cache[10] = full_combo
        cache[11] = 1

        lol = requests.get(f'https://akatsuki.pw/api/v1/users/scores/best?rx=1&name={c}&mode=0')
        if not lol:
            return await ctx.send(f"User couldn't be found for {c}!")
        songname = lol.json()['scores'][0]['beatmap']['song_name']

        cache[5] = songname

        embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR: {ar} OD: {od}] ▸ {accuracy}%\n▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{count_300}/{count_100}/{count_50}/{count_miss}]\n▸ Map Completed: {completed}', color=0xb6ebf1)
        embed.set_author(name=f"{songname} +{mods} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmap_id}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
        embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapset_id}l.jpg")
        embed.set_footer(text=f"Top osu! Relax Standard Play for {username.replace('ygfviasfa',' ')} ")
        await ctx.send(embed=embed)

    @commands.command()
    async def rxtt(self, ctx, *args):
        """relax taiko top
        """
        completemessage = len(args)
        if ctx.message.mentions:
            b = collation.find_one({"_id": ctx.message.mentions[0].id})
            if b == None: 
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
        elif completemessage == 0:
            b = collation.find_one({"_id": ctx.message.author.id})
            if b == None: 
                return await ctx.send(f"User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
        else: 
            c = '{}'.format(' '.join(args))
        
        ababa = akatsukiapi.stats(c)
        if ababa == 'error':
            return await ctx.send(f"User couldn't be found for {c}!")
        info = akatsukiapi.relaxtaikotop(c)
        if info == 'error':
            return await ctx.send(f"User couldn't be found for {c}!")
        userid = ababa[12]
        username = ababa[0]
        score = info[0]
        max_combo = info[1]
        full_combo = info[2]
        mods = info[3]
        count_300 = info[4]
        count_100 = info[5]
        count_50 = info[6]
        count_miss = info[7]
        accuracy = info[8]
        pp = info[9]
        rank = info[10]
        completed = info[11]
        beatmap_id = info[12]
        beatmapset_id = info[13]
        ar = info[14]
        od = info[15]
        difficulty = info[16]

        cache[0] = ctx.guild.id
        cache[1] = ctx.message.channel.id
        cache[2] = beatmap_id
        cache[3] = 1
        cache[4] = beatmapset_id
        cache[6] = userid
        cache[7] = difficulty
        cache[8] = ar
        cache[9] = od
        cache[10] = full_combo
        cache[11] = 1

        lol = requests.get(f'https://akatsuki.pw/api/v1/users/scores/best?rx=1&name={c}&mode=1')
        if not lol:
            return await ctx.send(f"User couldn't be found for {c}!")
        songname = lol.json()['scores'][0]['beatmap']['song_name']

        cache[5] = songname

        embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR: {ar} OD: {od}] ▸ {accuracy}%\n▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{count_300}/{count_100}/{count_50}/{count_miss}]\n▸ Map Completed: {completed}', color=0xb6ebf1)
        embed.set_author(name=f"{songname} +{mods} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmap_id}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
        embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapset_id}l.jpg")
        embed.set_footer(text=f"Top osu! Relax Taiko Play for {username.replace('ygfviasfa',' ')} ")
        await ctx.send(embed=embed)

    @commands.command()
    async def tt(self, ctx, *args):
        """taiko top
        """
        completemessage = len(args)
        if ctx.message.mentions:
            b = collation.find_one({"_id": ctx.message.mentions[0].id})
            if b == None: 
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
        elif completemessage == 0:
            b = collation.find_one({"_id": ctx.message.author.id})
            if b == None: 
                return await ctx.send(f"User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
        else: 
            c = '{}'.format(' '.join(args))
        
        ababa = akatsukiapi.stats(c)
        if ababa == 'error':
            return await ctx.send(f"User couldn't be found for {c}!")
        info = akatsukiapi.taikotop(c)
        if info == 'error':
            return await ctx.send(f"User couldn't be found for {c}!")
        userid = ababa[12]
        username = ababa[0]
        score = info[0]
        max_combo = info[1]
        full_combo = info[2]
        mods = info[3]
        count_300 = info[4]
        count_100 = info[5]
        count_50 = info[6]
        count_miss = info[7]
        accuracy = info[8]
        pp = info[9]
        rank = info[10]
        completed = info[11]
        beatmap_id = info[12]
        beatmapset_id = info[13]
        ar = info[14]
        od = info[15]
        difficulty = info[16]

        cache[0] = ctx.guild.id
        cache[1] = ctx.message.channel.id
        cache[2] = beatmap_id
        cache[3] = 1
        cache[4] = beatmapset_id
        cache[6] = userid
        cache[7] = difficulty
        cache[8] = ar
        cache[9] = od
        cache[10] = full_combo
        cache[11] = 0

        lol = requests.get(f'https://akatsuki.pw/api/v1/users/scores/best?rx=0&name={c}&mode=1')
        if not lol:
            return await ctx.send(f"User couldn't be found for {c}!")
        songname = lol.json()['scores'][0]['beatmap']['song_name']

        cache[5] = songname

        embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR: {ar} OD: {od}] ▸ {accuracy}%\n▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{count_300}/{count_100}/{count_50}/{count_miss}]\n▸ Map Completed: {completed}', color=0xb6ebf1)
        embed.set_author(name=f"{songname} +{mods} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmap_id}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
        embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapset_id}l.jpg")
        embed.set_footer(text=f"Top osu! Taiko Play for {username.replace('ygfviasfa',' ')} ")
        await ctx.send(embed=embed)

    @commands.command()
    async def c(self, ctx, *args):
        """compare map
        """
        completemessage = len(args)
        if ctx.message.mentions:
            b = collation.find_one({"_id": ctx.message.mentions[0].id})
            if b == None: 
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
        elif completemessage == 0:
            b = collation.find_one({"_id": ctx.message.author.id})
            if b == None: 
                return await ctx.send(f"User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
        else:
            c = '{}'.format(' '.join(args))

        if ctx.message.channel.id not in cache or ctx.guild.id not in cache:
        	return await ctx.send('Couldnt find map in this place!')

        beatmapid = cache[2]
        mode = cache[3]
        beatmapset_id = cache[4]
        songname = cache[5]
        difficulty = cache[7]
        rx = cache[11]
        ar = cache[8]
        od = cache[9]
        full_combo = cache[10]

        info = akatsukiapi.compare(c, beatmapid, mode, rx)
        
        if info == 'no user found':
            return await ctx.send('No user found!')

        if info == 'no score found':
            return await ctx.send('No score found for this user on this map!')

        if int(info['enabled_mods']) == 0:
            mods = 'NM'
        else:
            just_some_mods_lol = akatsukiapi.readableMods(int(info['enabled_mods']))
            if 'NC' in just_some_mods_lol:
                mods = just_some_mods_lol.replace('DT','')
            else:
                mods = just_some_mods_lol
        
        userid = info['user_id']
        rank = info['rank']
        pppp = info['pp']
        ppp = float(pppp)
        pp = round(ppp, 2)
        score = info['score']
        max_combo = info['maxcombo']
        count_300 = info['count300']
        count_100 = info['count100']
        count_50 = info['count50']
        count_miss = info['countmiss']
        username = info['username']
        if mode == 0:
        	total = sum((int(count_300), int(count_100), int(count_50), int(count_miss)))
	        accc = 100.0 * sum((
	                int(count_50) * 50.0,
	                int(count_100) * 100.0,
	                int(count_300) * 300.0
	            )) / (total * 300.0)
        elif mode == 1:
            total = sum((int(count_300), int(count_100), int(count_miss)))
            accc = 100.0 * sum((
            int(count_100) * 150.0,
            int(count_300) * 300.0
           )) / (total * 300.0)

        acc = round(accc, 2)
        embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR: {ar} OD: {od}] ▸ {acc}%\n▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{count_300}/{count_100}/{count_50}/{count_miss}]', color=0xb6ebf1)
        embed.set_author(name=f"{songname} +{mods} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmapid}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
        embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapset_id}l.jpg")
        embed.set_footer(text=f"Top Play for {username} on this map!")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Akatsuki(client))

import discord
from discord.ext import commands
import requests
import os
import akatsukiapi
import Chiyo

collation = Chiyo.collation

class Akatsuki(commands.Cog):

    def __int__(self, client):
        self.client = client

    @commands.command()
    async def reg(self, ctx, *args):
        completemessage = len(args)
        if ctx.message.mentions:
            b = collation.find_one({"_id": ctx.message.mentions[0].id})
            if b == None: 
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
            info = akatsukiapi.stats(c)
            if info == 'error':
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
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
        elif completemessage == 0:
            b = collation.find_one({"_id": ctx.message.author.id})
            if b == None: 
                return await ctx.send("User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
            info = akatsukiapi.stats(c)
            if info == 'error':
                return await ctx.send("User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
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
        else: 
            msg = '{}'.format(' '.join(args))
            info = akatsukiapi.stats(msg)
            if info == 'error':
                return await ctx.send(f"User couldn't be found for {msg}!")
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
    async def relax(self, ctx, *args):
        completemessage = len(args)
        if ctx.message.mentions:
            b = collation.find_one({"_id": ctx.message.mentions[0].id})
            if b == None: 
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
            info = akatsukiapi.relaxstats(c)
            if info == 'error':
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
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
        elif completemessage == 0:
            b = collation.find_one({"_id": ctx.message.author.id})
            if b == None: 
                return await ctx.send("User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
            info = akatsukiapi.relaxstats(c)
            if info == 'error':
                return await ctx.send("User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
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
        else: 
            msg = '{}'.format(' '.join(args))
            info = akatsukiapi.relaxstats(msg)
            if info == 'error':
                return await ctx.send(f"User couldn't be found for {msg}!")
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
    async def relaxtaiko(self, ctx, *args):
        completemessage = len(args)
        if ctx.message.mentions:
            b = collation.find_one({"_id": ctx.message.mentions[0].id})
            if b == None: 
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
            info = akatsukiapi.relaxtaikostats(c)
            if info == 'error':
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
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
            embed.set_author(name=f"osu! Relax Taiko Profile for {username.replace('ygfviasfa',' ')} ", url=f"https://akatsuki.pw/u/{userid}", icon_url=f"https://avatars0.githubusercontent.com/u/45724130?s=200&v=4.png")
            embed.set_thumbnail(url=f"https://a.akatsuki.pw/{userid}.png")
            embed.set_footer(text=f"Player on Akatsuki!")
            return await ctx.send(embed=embed)
        elif completemessage == 0:
            b = collation.find_one({"_id": ctx.message.author.id})
            if b == None: 
                return await ctx.send("User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
            info = akatsukiapi.relaxtaikostats(c)
            if info == 'error':
                return await ctx.send("User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
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
            embed.set_author(name=f"osu! Relax Taiko Profile for {username.replace('ygfviasfa',' ')} ", url=f"https://akatsuki.pw/u/{userid}", icon_url=f"https://avatars0.githubusercontent.com/u/45724130?s=200&v=4.png")
            embed.set_thumbnail(url=f"https://a.akatsuki.pw/{userid}.png")
            embed.set_footer(text=f"Player on Akatsuki!")
            return await ctx.send(embed=embed)
        else: 
            msg = '{}'.format(' '.join(args))
            info = akatsukiapi.relaxtaikostats(msg)
            if info == 'error':
                return await ctx.send(f"User couldn't be found for {msg}!")
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
    async def taiko(self, ctx, *args):
        completemessage = len(args)
        if ctx.message.mentions:
            b = collation.find_one({"_id": ctx.message.mentions[0].id})
            if b == None: 
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
            info = akatsukiapi.taikostats(c)
            if info == 'error':
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
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
        elif completemessage == 0:
            b = collation.find_one({"_id": ctx.message.author.id})
            if b == None: 
                return await ctx.send("User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
            info = akatsukiapi.taikostats(c)
            if info == 'error':
                return await ctx.send("User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
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
        else: 
            msg = '{}'.format(' '.join(args))
            info = akatsukiapi.taikostats(msg)
            if info == 'error':
                return await ctx.send(f"User couldn't be found for {msg}!")
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
    async def recent(self, ctx, *args):
        completemessage = len(args)
        if ctx.message.mentions:
            b = collation.find_one({"_id": ctx.message.mentions[0].id})
            if b == None: 
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
            ababa = akatsukiapi.stats(c)
            if ababa == 'error':
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
            info = akatsukiapi.recent(c)
            if info == 'error':
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
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

            lol = requests.get(f'https://akatsuki.pw/api/v1/users/scores/recent?rx=0&name={c}&mode=0')
            if not lol:
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
            songname = lol.json()['scores'][0]['beatmap']['song_name']

            embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR: {ar} OD: {od}] ▸ {accuracy}%\n▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{count_300}/{count_100}/{count_50}/{count_miss}]\n▸ Map Completed: {completed}', color=0xb6ebf1)
            embed.set_author(name=f"{songname} +{mods} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmap_id}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
            embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapset_id}l.jpg")
            embed.set_footer(text=f"Most Recent osu! Standard Play for {username.replace('ygfviasfa',' ')} ")
            await ctx.send(embed=embed)
        elif completemessage == 0:
            b = collation.find_one({"_id": ctx.message.author.id})
            if b == None: 
                return await ctx.send(f"User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
            ababa = akatsukiapi.stats(c)
            if ababa == 'error':
                return await ctx.send(f"User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
            info = akatsukiapi.recent(c)
            if info == 'error':
                return await ctx.send(f"User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
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

            lol = requests.get(f'https://akatsuki.pw/api/v1/users/scores/recent?rx=0&name={c}&mode=0')
            if not lol:
                return await ctx.send(f"User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
            songname = lol.json()['scores'][0]['beatmap']['song_name']

            embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR: {ar} OD: {od}] ▸ {accuracy}%\n▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{count_300}/{count_100}/{count_50}/{count_miss}]\n▸ Map Completed: {completed}', color=0xb6ebf1)
            embed.set_author(name=f"{songname} +{mods} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmap_id}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
            embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapset_id}l.jpg")
            embed.set_footer(text=f"Most Recent osu! Standard Play for {username.replace('ygfviasfa',' ')} ")
            await ctx.send(embed=embed)
        else: 
            msg = '{}'.format(' '.join(args))
            ababa = akatsukiapi.stats(msg)
            if ababa == 'error':
                return await ctx.send(f"User couldn't be found for {msg}!")
            info = akatsukiapi.recent(msg)
            if info == 'error':
                return await ctx.send(f"User couldn't be found for {msg}!")
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

            lol = requests.get(f'https://akatsuki.pw/api/v1/users/scores/recent?rx=0&name={msg}&mode=0')
            if not lol:
                return await ctx.send(f"User couldn't be found for {msg}!")
            songname = lol.json()['scores'][0]['beatmap']['song_name']

            embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR: {ar} OD: {od}] ▸ {accuracy}%\n▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{count_300}/{count_100}/{count_50}/{count_miss}]\n▸ Map Completed: {completed}', color=0xb6ebf1)
            embed.set_author(name=f"{songname} +{mods} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmap_id}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
            embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapset_id}l.jpg")
            embed.set_footer(text=f"Most Recent osu! Standard Play for {username.replace('ygfviasfa',' ')} ")
            await ctx.send(embed=embed)

    @commands.command()
    async def relaxrecent(self, ctx, *args):
        completemessage = len(args)
        if ctx.message.mentions:
            b = collation.find_one({"_id": ctx.message.mentions[0].id})
            if b == None: 
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
            ababa = akatsukiapi.stats(c)
            if ababa == 'error':
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
            info = akatsukiapi.relaxrecent(c)
            if info == 'error':
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
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
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
            songname = lol.json()['scores'][0]['beatmap']['song_name']

            embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR: {ar} OD: {od}] ▸ {accuracy}%\n▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{count_300}/{count_100}/{count_50}/{count_miss}]\n▸ Map Completed: {completed}', color=0xb6ebf1)
            embed.set_author(name=f"{songname} +{mods} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmap_id}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
            embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapset_id}l.jpg")
            embed.set_footer(text=f"Most Recent osu! Relax Standard Play for {username.replace('ygfviasfa',' ')} ")
            await ctx.send(embed=embed)
        elif completemessage == 0:
            b = collation.find_one({"_id": ctx.message.author.id})
            if b == None: 
                return await ctx.send(f"User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
            ababa = akatsukiapi.stats(c)
            if ababa == 'error':
                return await ctx.send(f"User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
            info = akatsukiapi.relaxrecent(c)
            if info == 'error':
                return await ctx.send(f"User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
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
                return await ctx.send(f"User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
            songname = lol.json()['scores'][0]['beatmap']['song_name']

            embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR: {ar} OD: {od}] ▸ {accuracy}%\n▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{count_300}/{count_100}/{count_50}/{count_miss}]\n▸ Map Completed: {completed}', color=0xb6ebf1)
            embed.set_author(name=f"{songname} +{mods} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmap_id}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
            embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapset_id}l.jpg")
            embed.set_footer(text=f"Most Recent osu! Relax Standard Play for {username.replace('ygfviasfa',' ')} ")
            await ctx.send(embed=embed)
        else: 
            msg = '{}'.format(' '.join(args))
            ababa = akatsukiapi.stats(msg)
            if ababa == 'error':
                return await ctx.send(f"User couldn't be found for {msg}!")
            info = akatsukiapi.relaxrecent(msg)
            if info == 'error':
                return await ctx.send(f"User couldn't be found for {msg}!")
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

            lol = requests.get(f'https://akatsuki.pw/api/v1/users/scores/recent?rx=1&name={msg}&mode=0')
            if not lol:
                return await ctx.send(f"User couldn't be found for {msg}!")
            songname = lol.json()['scores'][0]['beatmap']['song_name']

            embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR: {ar} OD: {od}] ▸ {accuracy}%\n▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{count_300}/{count_100}/{count_50}/{count_miss}]\n▸ Map Completed: {completed}', color=0xb6ebf1)
            embed.set_author(name=f"{songname} +{mods} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmap_id}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
            embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapset_id}l.jpg")
            embed.set_footer(text=f"Most Recent osu! Relax Standard Play for {username.replace('ygfviasfa',' ')} ")
            await ctx.send(embed=embed)

    @commands.command()
    async def taikorecent(self, ctx, *args):
        completemessage = len(args)
        if ctx.message.mentions:
            b = collation.find_one({"_id": ctx.message.mentions[0].id})
            if b == None: 
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
            ababa = akatsukiapi.stats(c)
            if ababa == 'error':
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
            info = akatsukiapi.taikorecent(c)
            if info == 'error':
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
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

            lol = requests.get(f'https://akatsuki.pw/api/v1/users/scores/recent?rx=0&name={c}&mode=1')
            if not lol:
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
            songname = lol.json()['scores'][0]['beatmap']['song_name']

            embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR: {ar} OD: {od}] ▸ {accuracy}%\n▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{count_300}/{count_100}/{count_50}/{count_miss}]\n▸ Map Completed: {completed}', color=0xb6ebf1)
            embed.set_author(name=f"{songname} +{mods} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmap_id}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
            embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapset_id}l.jpg")
            embed.set_footer(text=f"Most Recent osu! Taiko Play for {username.replace('ygfviasfa',' ')} ")
            await ctx.send(embed=embed)
        elif completemessage == 0:
            b = collation.find_one({"_id": ctx.message.author.id})
            if b == None: 
                return await ctx.send(f"User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
            ababa = akatsukiapi.stats(c)
            if ababa == 'error':
                return await ctx.send(f"User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
            info = akatsukiapi.taikorecent(c)
            if info == 'error':
                return await ctx.send(f"User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
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

            lol = requests.get(f'https://akatsuki.pw/api/v1/users/scores/recent?rx=0&name={c}&mode=1')
            if not lol:
                return await ctx.send(f"User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
            songname = lol.json()['scores'][0]['beatmap']['song_name']

            embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR: {ar} OD: {od}] ▸ {accuracy}%\n▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{count_300}/{count_100}/{count_50}/{count_miss}]\n▸ Map Completed: {completed}', color=0xb6ebf1)
            embed.set_author(name=f"{songname} +{mods} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmap_id}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
            embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapset_id}l.jpg")
            embed.set_footer(text=f"Most Recent osu! Taiko Play for {username.replace('ygfviasfa',' ')} ")
            await ctx.send(embed=embed)
        else: 
            msg = '{}'.format(' '.join(args))
            ababa = akatsukiapi.stats(msg)
            if ababa == 'error':
                return await ctx.send(f"User couldn't be found for {msg}!")
            info = akatsukiapi.taikorecent(msg)
            if info == 'error':
                return await ctx.send(f"User couldn't be found for {msg}!")
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

            lol = requests.get(f'https://akatsuki.pw/api/v1/users/scores/recent?rx=0&name={msg}&mode=1')
            if not lol:
                return await ctx.send(f"User couldn't be found for {msg}!")
            songname = lol.json()['scores'][0]['beatmap']['song_name']

            embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR: {ar} OD: {od}] ▸ {accuracy}%\n▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{count_300}/{count_100}/{count_50}/{count_miss}]\n▸ Map Completed: {completed}', color=0xb6ebf1)
            embed.set_author(name=f"{songname} +{mods} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmap_id}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
            embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapset_id}l.jpg")
            embed.set_footer(text=f"Most Recent osu! Taiko Play for {username.replace('ygfviasfa',' ')} ")
            await ctx.send(embed=embed)

    @commands.command()
    async def relaxtaikorecent(self, ctx, *args):
        completemessage = len(args)
        if ctx.message.mentions:
            b = collation.find_one({"_id": ctx.message.mentions[0].id})
            if b == None: 
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
            ababa = akatsukiapi.stats(c)
            if ababa == 'error':
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
            info = akatsukiapi.relaxtaikorecent(c)
            if info == 'error':
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
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

            lol = requests.get(f'https://akatsuki.pw/api/v1/users/scores/recent?rx=1&name={c}&mode=1')
            if not lol:
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
            songname = lol.json()['scores'][0]['beatmap']['song_name']

            embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR: {ar} OD: {od}] ▸ {accuracy}%\n▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{count_300}/{count_100}/{count_50}/{count_miss}]\n▸ Map Completed: {completed}', color=0xb6ebf1)
            embed.set_author(name=f"{songname} +{mods} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmap_id}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
            embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapset_id}l.jpg")
            embed.set_footer(text=f"Most Recent osu! Relax Taiko Play for {username.replace('ygfviasfa',' ')} ")
            await ctx.send(embed=embed)
        elif completemessage == 0:
            b = collation.find_one({"_id": ctx.message.author.id})
            if b == None: 
                return await ctx.send(f"User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
            ababa = akatsukiapi.stats(c)
            if ababa == 'error':
                return await ctx.send(f"User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
            info = akatsukiapi.relaxtaikorecent(c)
            if info == 'error':
                return await ctx.send(f"User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
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

            lol = requests.get(f'https://akatsuki.pw/api/v1/users/scores/recent?rx=1&name={c}&mode=1')
            if not lol:
                return await ctx.send(f"User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
            songname = lol.json()['scores'][0]['beatmap']['song_name']

            embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR: {ar} OD: {od}] ▸ {accuracy}%\n▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{count_300}/{count_100}/{count_50}/{count_miss}]\n▸ Map Completed: {completed}', color=0xb6ebf1)
            embed.set_author(name=f"{songname} +{mods} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmap_id}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
            embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapset_id}l.jpg")
            embed.set_footer(text=f"Most Recent osu! Relax Taiko Play for {username.replace('ygfviasfa',' ')} ")
            return await ctx.send(embed=embed)
        else: 
            msg = '{}'.format(' '.join(args))
            ababa = akatsukiapi.stats(msg)
            if ababa == 'error':
                return await ctx.send(f"User couldn't be found for {msg}!")
            info = akatsukiapi.relaxtaikorecent(msg)
            if info == 'error':
                return await ctx.send(f"User couldn't be found for {msg}!")
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

            lol = requests.get(f'https://akatsuki.pw/api/v1/users/scores/recent?rx=1&name={msg}&mode=1')
            if not lol:
                return await ctx.send(f"User couldn't be found for {msg}!")
            songname = lol.json()['scores'][0]['beatmap']['song_name']

            embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR: {ar} OD: {od}] ▸ {accuracy}%\n▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{count_300}/{count_100}/{count_50}/{count_miss}]\n▸ Map Completed: {completed}', color=0xb6ebf1)
            embed.set_author(name=f"{songname} +{mods} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmap_id}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
            embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapset_id}l.jpg")
            embed.set_footer(text=f"Most Recent osu! Relax Taiko Play for {username.replace('ygfviasfa',' ')} ")
            await ctx.send(embed=embed)

    @commands.command()
    async def top(self, ctx, *args):
        completemessage = len(args)
        if ctx.message.mentions:
            b = collation.find_one({"_id": ctx.message.mentions[0].id})
            if b == None: 
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
            ababa = akatsukiapi.stats(c)
            if ababa == 'error':
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
            info = akatsukiapi.top(c)
            if info == 'error':
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
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

            lol = requests.get(f'https://akatsuki.pw/api/v1/users/scores/best?rx=0&name={c}&mode=0')
            if not lol:
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
            songname = lol.json()['scores'][0]['beatmap']['song_name']

            embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR: {ar} OD: {od}] ▸ {accuracy}%\n▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{count_300}/{count_100}/{count_50}/{count_miss}]\n▸ Map Completed: {completed}', color=0xb6ebf1)
            embed.set_author(name=f"{songname} +{mods} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmap_id}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
            embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapset_id}l.jpg")
            embed.set_footer(text=f"Top osu! Standard Play for {username.replace('ygfviasfa',' ')} ")
            await ctx.send(embed=embed)
        elif completemessage == 0:
            b = collation.find_one({"_id": ctx.message.author.id})
            if b == None: 
                return await ctx.send(f"User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
            ababa = akatsukiapi.stats(c)
            if ababa == 'error':
                return await ctx.send(f"User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
            info = akatsukiapi.top(c)
            if info == 'error':
                return await ctx.send(f"User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
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

            lol = requests.get(f'https://akatsuki.pw/api/v1/users/scores/best?rx=0&name={c}&mode=0')
            if not lol:
                return await ctx.send(f"User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
            songname = lol.json()['scores'][0]['beatmap']['song_name']

            embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR: {ar} OD: {od}] ▸ {accuracy}%\n▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{count_300}/{count_100}/{count_50}/{count_miss}]\n▸ Map Completed: {completed}', color=0xb6ebf1)
            embed.set_author(name=f"{songname} +{mods} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmap_id}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
            embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapset_id}l.jpg")
            embed.set_footer(text=f"Top osu! Standard Play for {username.replace('ygfviasfa',' ')} ")
            return await ctx.send(embed=embed)
        else: 
            msg = '{}'.format(' '.join(args))
            ababa = akatsukiapi.stats(msg)
            if ababa == 'error':
                return await ctx.send(f"User couldn't be found for {msg}!")
            info = akatsukiapi.top(msg)
            if info == 'error':
                return await ctx.send(f"User couldn't be found for {msg}!")
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

            lol = requests.get(f'https://akatsuki.pw/api/v1/users/scores/best?rx=0&name={msg}&mode=0')
            if not lol:
                return await ctx.send(f"User couldn't be found for {msg}!")
            songname = lol.json()['scores'][0]['beatmap']['song_name']

            embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR: {ar} OD: {od}] ▸ {accuracy}%\n▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{count_300}/{count_100}/{count_50}/{count_miss}]\n▸ Map Completed: {completed}', color=0xb6ebf1)
            embed.set_author(name=f"{songname} +{mods} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmap_id}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
            embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapset_id}l.jpg")
            embed.set_footer(text=f"Top osu! Standard Play for {username.replace('ygfviasfa',' ')} ")
            await ctx.send(embed=embed)

    @commands.command()
    async def relaxtop(self, ctx, *args):
        completemessage = len(args)
        if ctx.message.mentions:
            b = collation.find_one({"_id": ctx.message.mentions[0].id})
            if b == None: 
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
            ababa = akatsukiapi.stats(c)
            if ababa == 'error':
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
            info = akatsukiapi.relaxtop(c)
            if info == 'error':
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
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

            lol = requests.get(f'https://akatsuki.pw/api/v1/users/scores/best?rx=1&name={c}&mode=0')
            if not lol:
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
            songname = lol.json()['scores'][0]['beatmap']['song_name']

            embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR: {ar} OD: {od}] ▸ {accuracy}%\n▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{count_300}/{count_100}/{count_50}/{count_miss}]\n▸ Map Completed: {completed}', color=0xb6ebf1)
            embed.set_author(name=f"{songname} +{mods} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmap_id}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
            embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapset_id}l.jpg")
            embed.set_footer(text=f"Top osu! Relax Standard Play for {username.replace('ygfviasfa',' ')} ")
            await ctx.send(embed=embed)
        elif completemessage == 0:
            b = collation.find_one({"_id": ctx.message.author.id})
            if b == None: 
                return await ctx.send(f"User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
            ababa = akatsukiapi.stats(c)
            if ababa == 'error':
                return await ctx.send(f"User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
            info = akatsukiapi.relaxtop(c)
            if info == 'error':
                return await ctx.send(f"User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
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

            lol = requests.get(f'https://akatsuki.pw/api/v1/users/scores/best?rx=1&name={c}&mode=0')
            if not lol:
                return await ctx.send(f"User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
            songname = lol.json()['scores'][0]['beatmap']['song_name']

            embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR: {ar} OD: {od}] ▸ {accuracy}%\n▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{count_300}/{count_100}/{count_50}/{count_miss}]\n▸ Map Completed: {completed}', color=0xb6ebf1)
            embed.set_author(name=f"{songname} +{mods} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmap_id}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
            embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapset_id}l.jpg")
            embed.set_footer(text=f"Top osu! Relax Standard Play for {username.replace('ygfviasfa',' ')} ")
            return await ctx.send(embed=embed)
        else: 
            msg = '{}'.format(' '.join(args))
            ababa = akatsukiapi.stats(msg)
            if ababa == 'error':
                return await ctx.send(f"User couldn't be found for {msg}!")
            info = akatsukiapi.relaxtop(msg)
            if info == 'error':
                return await ctx.send(f"User couldn't be found for {msg}!")
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

            lol = requests.get(f'https://akatsuki.pw/api/v1/users/scores/best?rx=1&name={msg}&mode=0')
            if not lol:
                return await ctx.send(f"User couldn't be found for {msg}!")
            songname = lol.json()['scores'][0]['beatmap']['song_name']

            embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR: {ar} OD: {od}] ▸ {accuracy}%\n▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{count_300}/{count_100}/{count_50}/{count_miss}]\n▸ Map Completed: {completed}', color=0xb6ebf1)
            embed.set_author(name=f"{songname} +{mods} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmap_id}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
            embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapset_id}l.jpg")
            embed.set_footer(text=f"Top osu! Relax Standard Play for {username.replace('ygfviasfa',' ')} ")
            await ctx.send(embed=embed)

    @commands.command()
    async def relaxtaikotop(self, ctx, *args):
        completemessage = len(args)
        if ctx.message.mentions:
            b = collation.find_one({"_id": ctx.message.mentions[0].id})
            if b == None: 
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
            ababa = akatsukiapi.stats(c)
            if ababa == 'error':
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
            info = akatsukiapi.relaxtaikotop(c)
            if info == 'error':
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
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

            lol = requests.get(f'https://akatsuki.pw/api/v1/users/scores/best?rx=1&name={c}&mode=1')
            if not lol:
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
            songname = lol.json()['scores'][0]['beatmap']['song_name']

            embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR: {ar} OD: {od}] ▸ {accuracy}%\n▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{count_300}/{count_100}/{count_50}/{count_miss}]\n▸ Map Completed: {completed}', color=0xb6ebf1)
            embed.set_author(name=f"{songname} +{mods} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmap_id}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
            embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapset_id}l.jpg")
            embed.set_footer(text=f"Top osu! Relax Taiko Play for {username.replace('ygfviasfa',' ')} ")
            await ctx.send(embed=embed)
        elif completemessage == 0:
            b = collation.find_one({"_id": ctx.message.author.id})
            if b == None: 
                return await ctx.send(f"User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
            ababa = akatsukiapi.stats(c)
            if ababa == 'error':
                return await ctx.send(f"User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
            info = akatsukiapi.relaxtaikotop(c)
            if info == 'error':
                return await ctx.send(f"User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
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

            lol = requests.get(f'https://akatsuki.pw/api/v1/users/scores/best?rx=1&name={c}&mode=1')
            if not lol:
                return await ctx.send(f"User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
            songname = lol.json()['scores'][0]['beatmap']['song_name']

            embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR: {ar} OD: {od}] ▸ {accuracy}%\n▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{count_300}/{count_100}/{count_50}/{count_miss}]\n▸ Map Completed: {completed}', color=0xb6ebf1)
            embed.set_author(name=f"{songname} +{mods} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmap_id}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
            embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapset_id}l.jpg")
            embed.set_footer(text=f"Top osu! Relax Taiko Play for {username.replace('ygfviasfa',' ')} ")
            return await ctx.send(embed=embed)
        else: 
            msg = '{}'.format(' '.join(args))
            ababa = akatsukiapi.stats(msg)
            if ababa == 'error':
                return await ctx.send(f"User couldn't be found for {msg}!")
            info = akatsukiapi.relaxtaikotop(msg)
            if info == 'error':
                return await ctx.send(f"User couldn't be found for {msg}!")
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

            lol = requests.get(f'https://akatsuki.pw/api/v1/users/scores/best?rx=1&name={msg}&mode=1')
            if not lol:
                return await ctx.send(f"User couldn't be found for {msg}!")
            songname = lol.json()['scores'][0]['beatmap']['song_name']

            embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR: {ar} OD: {od}] ▸ {accuracy}%\n▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{count_300}/{count_100}/{count_50}/{count_miss}]\n▸ Map Completed: {completed}', color=0xb6ebf1)
            embed.set_author(name=f"{songname} +{mods} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmap_id}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
            embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapset_id}l.jpg")
            embed.set_footer(text=f"Top osu! Relax Taiko Play for {username.replace('ygfviasfa',' ')} ")
            await ctx.send(embed=embed)

    @commands.command()
    async def taikotop(self, ctx, *args):
        completemessage = len(args)
        if ctx.message.mentions:
            b = collation.find_one({"_id": ctx.message.mentions[0].id})
            if b == None: 
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
            ababa = akatsukiapi.stats(c)
            if ababa == 'error':
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
            info = akatsukiapi.taikotop(c)
            if info == 'error':
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
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

            lol = requests.get(f'https://akatsuki.pw/api/v1/users/scores/best?rx=0&name={c}&mode=1')
            if not lol:
                return await ctx.send(f"User couldn't be found for {ctx.message.mentions[0]}!\n{ctx.message.mentions[0]} try connecting your account to a valid user like `;connect <Akatsuki Username>`")
            songname = lol.json()['scores'][0]['beatmap']['song_name']

            embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR: {ar} OD: {od}] ▸ {accuracy}%\n▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{count_300}/{count_100}/{count_50}/{count_miss}]\n▸ Map Completed: {completed}', color=0xb6ebf1)
            embed.set_author(name=f"{songname} +{mods} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmap_id}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
            embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapset_id}l.jpg")
            embed.set_footer(text=f"Top osu! Taiko Play for {username.replace('ygfviasfa',' ')} ")
            await ctx.send(embed=embed)
        elif completemessage == 0:
            b = collation.find_one({"_id": ctx.message.author.id})
            if b == None: 
                return await ctx.send(f"User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
            a = b['name']
            c = str(a)
            ababa = akatsukiapi.stats(c)
            if ababa == 'error':
                return await ctx.send(f"User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
            info = akatsukiapi.taikotop(c)
            if info == 'error':
                return await ctx.send(f"User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
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

            lol = requests.get(f'https://akatsuki.pw/api/v1/users/scores/best?rx=0&name={c}&mode=1')
            if not lol:
                return await ctx.send(f"User couldn't be found!\nTry connecting your account to a valid user like `;connect <Akatsuki Username>`")
            songname = lol.json()['scores'][0]['beatmap']['song_name']

            embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR: {ar} OD: {od}] ▸ {accuracy}%\n▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{count_300}/{count_100}/{count_50}/{count_miss}]\n▸ Map Completed: {completed}', color=0xb6ebf1)
            embed.set_author(name=f"{songname} +{mods} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmap_id}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
            embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapset_id}l.jpg")
            embed.set_footer(text=f"Top osu! Taiko Play for {username.replace('ygfviasfa',' ')} ")
            return await ctx.send(embed=embed)
        else: 
            msg = '{}'.format(' '.join(args))
            ababa = akatsukiapi.stats(msg)
            if ababa == 'error':
                return await ctx.send(f"User couldn't be found for {msg}!")
            info = akatsukiapi.taikotop(msg)
            if info == 'error':
                return await ctx.send(f"User couldn't be found for {msg}!")
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

            lol = requests.get(f'https://akatsuki.pw/api/v1/users/scores/best?rx=0&name={msg}&mode=1')
            if not lol:
                return await ctx.send(f"User couldn't be found for {msg}!")
            songname = lol.json()['scores'][0]['beatmap']['song_name']

            embed=discord.Embed(description=f'▸ {rank} ▸ {pp}PP [AR: {ar} OD: {od}] ▸ {accuracy}%\n▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{count_300}/{count_100}/{count_50}/{count_miss}]\n▸ Map Completed: {completed}', color=0xb6ebf1)
            embed.set_author(name=f"{songname} +{mods} [{difficulty}★]", url=f"https://akatsuki.pw/b/{beatmap_id}", icon_url=f"https://a.akatsuki.pw/{userid}.png")
            embed.set_thumbnail(url=f"https://b.ppy.sh/thumb/{beatmapset_id}l.jpg")
            embed.set_footer(text=f"Top osu! Taiko Play for {username.replace('ygfviasfa',' ')} ")
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Akatsuki(client))

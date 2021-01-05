import discord
from discord.ext import commands
import cover
import config
from cover import log

class osu(commands.Cog):

    def __init__(self, client) -> None:
        self.client = client
        self.QUERY = client.db
        self.cache = client.cache

    @commands.command()
    async def connect(self, ctx):
        msg = ctx.message.content.split(' ')[1:]
        if not len(msg):
            return await ctx.send("Please provide a user.")

        _username = self.QUERY.find_one({"_id": ctx.message.author.id})
        username = ' '.join(msg)
        user = cover.get_profile(username)

        if not user:
            return ctx.send('no user found.')

        if _username is None:
            post = {"_id": ctx.message.author.id, 'akatsuki': user['userid']}
            self.QUERY.insert_one(post)
        else:
            newvalues = { "$set": { 'akatsuki': user['userid'] } }
            self.QUERY.update_one(_username, newvalues)

        embed = discord.Embed(
            colour = ctx.message.author.roles[len(ctx.message.author.roles) - 1].color
        )
        
        embed.set_author(
            name = f"{user['username']} was connected to your discord account!", 
            url = config.logo if config.logo else 'https://akatsuki.pw/static/logos/logo.png'
        )

        embed.set_image(
            url = f"https://a.akatsuki.pw/{user['userid']}"
        )

        return await ctx.send(embed=embed)

    @commands.command(aliases=['r','rs','rc'])
    async def recent(self, ctx):
        relax = scoreid = mode = 0
        msg = ctx.message.content.lower().split(' ')[1:]
        if '-p' in msg:
            scoreid = int(msg[msg.index('-p') + 1])
            msg.remove(str(scoreid))
            msg.remove('-p')
        for _mode in (lawl := ['-std', '-taiko', '-ctb', '-mania']):
            if _mode in msg:
                msg.remove(_mode)
                mode = lawl.index(_mode)
            if 'mania' in _mode:
                relax = 0
        if '-rx' in msg:
            msg.remove('-rx')
            relax = 1
        msg = ' '.join(msg)

        if ctx.message.mentions:
            _userid = self.QUERY.find_one({"_id": ctx.message.mentions[0].id})
            if not _userid:
                return await ctx.send(f"User couldn't be found in our database! Try connecting a user to our database by doing `;connect (your username)`")
            userinfo = cover.get_recent(
                user = _userid['akatsuki'],
                mode = mode,
                relax = relax,
                limit = scoreid
            )
            if not userinfo:
                return await ctx.send("Couldn't find a score or user.")
        elif len(msg) == 0:
            _userid = self.QUERY.find_one({"_id": ctx.message.author.id})
            if not _userid:
                return await ctx.send(f"User couldn't be found in our database! Try connecting a user to our database by doing `;connect (your username)`")
            userinfo = cover.get_recent(
                user = _userid['akatsuki'],
                mode = mode,
                relax = relax,
                limit = scoreid
            )
            if not userinfo:
                return await ctx.send("Couldn't find a score or user.")
        else:
            userinfo = cover.get_recent(
                user = msg,
                mode = mode,
                relax = relax,
                limit = scoreid
            )
            if not userinfo:
                return await ctx.send("Couldn't find a score or user.")
        
        self.cache[ctx.message.channel.id] = userinfo['beatmap_id']
        embed=discord.Embed(
            description = 
            (
                '▸ {pp}PP [AR: {ar} OD: {od}] ▸ {acc}%\n'
                '▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{300s}/{100s}/{50s}/{misses}]\n'
                '▸ Map Completion: {completion}%'
            ).format(**userinfo),
            color = ctx.message.author.roles[len(ctx.message.author.roles) - 1].color
        )
        embed.set_author(
            name =
            (
                "{song_name} +{mods} [{difficulty}★]"
            ).format(**userinfo),
            url = "https://akatsuki.pw/b/{beatmap_id}".format(**userinfo), 
            icon_url = userinfo['rank']
        )
        embed.set_thumbnail(
            url = f'https://a.akatsuki.pw/{userinfo["userid"]}'
        )
        embed.set_image(
            url=f"https://assets.ppy.sh/beatmaps/{userinfo['beatmapset_id']}/covers/cover.jpg"
        )
        embed.set_footer(text=f"Recent Akatsuki Play for {userinfo['username']} set on {userinfo['time']}")
        return await ctx.send(embed=embed)

    @commands.command(aliases=['c'])
    async def compare(self, ctx):
        relax = scoreid = mode = 0
        msg = ctx.message.content.lower().split(' ')[1:]
        if '-p' in msg:
            scoreid = int(msg[msg.index('-p') + 1])
            msg.remove(str(scoreid))
            msg.remove('-p')
        for _mode in (lawl := ['-std', '-taiko', '-ctb', '-mania']):
            if _mode in msg:
                msg.remove(_mode)
                mode = lawl.index(_mode)
            if 'mania' in _mode:
                relax = 0
        if '-rx' in msg:
            msg.remove('-rx')
            relax = 1
        msg = ' '.join(msg)

        if ctx.message.channel.id not in self.cache:
            return await ctx.send('no map found.')

        if ctx.message.mentions:
            _userid = self.QUERY.find_one({"_id": ctx.message.mentions[0].id})
            if not _userid:
                return await ctx.send(f"User couldn't be found in our database! Try connecting a user to our database by doing `;connect (your username)`")
            userinfo = cover.get_scores(
                user = _userid['akatsuki'],
                mode = mode,
                relax = relax,
                limit = scoreid,
                beatmapid = self.cache[ctx.message.channel.id]
            )
            if not userinfo:
                return await ctx.send("Couldn't find a score.")
        elif len(msg) == 0:
            _userid = self.QUERY.find_one({"_id": ctx.message.author.id})
            if _userid is None:
                return await ctx.send(f"User couldn't be found in our database! Try connecting a user to our database by doing `;connect (your username)`")
            userinfo = cover.get_scores(
                user = _userid['akatsuki'],
                mode = mode,
                relax = relax,
                limit = scoreid,
                beatmapid = self.cache[ctx.message.channel.id]
            )
            if not userinfo:
                return await ctx.send("Couldn't find a score.")
        else:
            userinfo = cover.get_scores(
                user = msg,
                mode = mode,
                relax = relax,
                limit = scoreid,
                beatmapid = self.cache[ctx.message.channel.id]
            )
            if not userinfo:
                return await ctx.send("Couldn't find a score.")

        embed=discord.Embed(
            description = 
            (
                '▸ {pp}PP [AR: {ar} OD: {od}] ▸ {acc}%\n'
                '▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{300s}/{100s}/{50s}/{misses}]\n'
            ).format(**userinfo),
            color = ctx.message.author.roles[len(ctx.message.author.roles) - 1].color
        )
        embed.set_author(
            name =
            (
                "{song_name} +{mods} [{difficulty}★]"
            ).format(**userinfo),
            url = "https://osu.ppy.sh/b/{beatmap_id}".format(**userinfo), icon_url=userinfo['rank']
        )
        embed.set_thumbnail(
            url = f'https://a.akatsuki.pw/{userinfo["userid"]}'
        )
        embed.set_image(
            url=f"https://assets.ppy.sh/beatmaps/{userinfo['beatmapset_id']}/covers/cover.jpg"
        )
        embed.set_footer(text=f"Akatsuki Play for {userinfo['username']} set on {userinfo['time']}")
        return await ctx.send(embed=embed)

    @commands.command(aliases=['t'])
    async def top(self, ctx):
        relax = scoreid = mode = 0
        msg = ctx.message.content.lower().split(' ')[1:]
        if '-p' in msg:
            scoreid = int(msg[msg.index('-p') + 1])
            msg.remove(str(scoreid))
            msg.remove('-p')
        for _mode in (lawl := ['-std', '-taiko', '-ctb', '-mania']):
            if _mode in msg:
                msg.remove(_mode)
                mode = lawl.index(_mode)
            if 'mania' in _mode:
                relax = 0
        if '-rx' in msg:
            msg.remove('-rx')
            relax = 1
        msg = ' '.join(msg)

        if ctx.message.mentions:
            _userid = self.QUERY.find_one({"_id": ctx.message.mentions[0].id})
            if _userid is None:
                return await ctx.send(f"User couldn't be found in our database! Try connecting a user to our database by doing `;connect (your username)`")
            userinfo = cover.get_best(
                user = _userid['akatsuki'],
                mode = mode,
                relax = relax,
                limit = scoreid
            )
            if not userinfo:
                return await ctx.send("Couldn't find a score.")
        
        elif len(msg) == 0:
            _userid = self.QUERY.find_one({"_id": ctx.message.author.id})
            if _userid is None:
                return await ctx.send(f"User couldn't be found in our database! Try connecting a user to our database by doing `;connect (your username)`")
            userinfo = cover.get_best(
                user = _userid['akatsuki'],
                mode = mode,
                relax = relax,
                limit = scoreid
            )
            if not userinfo:
                return await ctx.send("Couldn't find a score.")
        else:
            userinfo = cover.get_best(
                user = msg,
                mode = mode,
                relax = relax,
                limit = scoreid
            )
            if not userinfo:
                return await ctx.send("Couldn't find a score.")

        self.cache[ctx.message.channel.id] = userinfo['beatmap_id']

        embed=discord.Embed(
            description = 
            (
                '▸ {pp}PP [AR: {ar} OD: {od}] ▸ {acc}%\n'
                '▸ {score} ▸ {max_combo}x/{full_combo}x ▸ [{300s}/{100s}/{50s}/{misses}]\n'
            ).format(**userinfo),
            color = ctx.message.author.roles[len(ctx.message.author.roles) - 1].color
        )
        embed.set_author(
            name =
            (
                "{song_name} +{mods} [{difficulty}★]"
            ).format(**userinfo),
            url = "https://osu.ppy.sh/b/{beatmap_id}".format(**userinfo), icon_url = userinfo['rank']
        )
        embed.set_thumbnail(
            url = f"https://a.akatsuki.pw/{userinfo['userid']}"
        )
        embed.set_image(
            url = f"https://assets.ppy.sh/beatmaps/{userinfo['beatmapset_id']}/covers/cover.jpg"
        )
        embed.set_footer(text=f"Top Akatsuki Play for {userinfo['username']} set on {userinfo['time']}")
        await ctx.send(embed=embed)


    @commands.command(aliases=['p','osu'])
    async def profile(self, ctx):
        relax, mode = 0, 0
        msg = ctx.message.content.lower().split(' ')[1:]
        for _mode in (lawl := ['-std', '-taiko', '-ctb', '-mania']):
            if _mode in msg:
                msg.remove(_mode)
                mode = lawl.index(_mode)
            if 'mania' in _mode:
                relax = 0
        if '-rx' in msg:
            msg.remove('-rx')
            relax = 1
        msg = ' '.join(msg)

        if ctx.message.mentions:
            _userid = self.QUERY.find_one({"_id": ctx.message.mentions[0].id})
            if _userid is None:
                return await ctx.send(f"User couldn't be found in our database! Try connecting a user to our database by doing `;connect (your username)`")

            userinfo = cover.get_profile(
                user = _userid['akatsuki'],
                mode = mode,
                relax = relax
            )
            if not userinfo:
                return await ctx.send(f"User couldn't be found.")
        elif len(msg) == 0:
            _userid = self.QUERY.find_one({"_id": ctx.message.author.id})
            if _userid == None:
                return await ctx.send(f"User couldn't be found in our database! Try connecting a user to our database by doing `;connect (your username)`")
            userinfo = cover.get_profile(
                user = _userid['akatsuki'],
                mode = mode,
                relax = relax
            )
            if not userinfo:
                return await ctx.send(f"User couldn't be found.")
        else:
            userinfo = cover.get_profile(
                user = msg,
                mode = mode,
                relax = relax
            )
            if not userinfo:
                return await ctx.send(f"User couldn't be found.")

        embed=discord.Embed(
        description = 
        ('▸ Official Rank: {rank} ({country}#{country_rank}) \n▸ Level: {level}\n▸ Total PP: {pp} \n▸ Accuracy: {acc}% \n▸ Playcount: {playcount}').format(**userinfo),
        color = ctx.message.author.roles[len(ctx.message.author.roles) - 1].color
        )
        embed.set_author(
            name = f"osu! Akatsuki Profile for {userinfo['username']} ", 
            url = f"https://akatsuki.pw/u/{userinfo['userid']}", 
            icon_url = config.logo if config.logo else 'https://akatsuki.pw/static/logos/logo.png'
        )
        embed.set_thumbnail(url = f"https://a.akatsuki.pw/{userinfo['userid']}")
        embed.set_footer(text=f"Registered on {userinfo['registered_on']}")
        return await ctx.send(embed=embed)


def setup(client):
    client.add_cog(osu(client))
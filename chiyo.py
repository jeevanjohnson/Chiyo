import discord
from discord.ext import commands
import config
import cover
import pymongo
import os
import re

BEATMAP = re.compile(r'https://akatsuki\.pw/b/(?P<id>[0-9]*)')

class Chiyo:

    def connect_database(self):
        try:
            client = pymongo.MongoClient((
            f"mongodb+srv://{config.username}:{config.password}"
            f"@{config.cluster}.bergf.mongodb.net/{config.database_name}"
            "?retryWrites=true&w=majority"))
        except Exception as e:
            cover.log(f"ERROR! when connecting to collection: {e}", cover.bcolors.FAIL)
            return

        db = client[config.database_name][config.collection]
        cover.log(f"Connecting to collection [{db.name}] was succesfull!", cover.bcolors.OKGREEN)
        return db

    def get_prefix(Chiyo, message):
        ...

    def run(self):
        Chiyo = commands.Bot(
            command_prefix = config.prefix,#get_prefix,
            case_insensitive = True,
            help_command = None
        )
        Chiyo.db = self.connect_database()
        Chiyo.cache = {}

        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                Chiyo.load_extension(f'cogs.{filename[:-3]}')

        @Chiyo.event
        async def on_ready():
            amount_of_servers = str(len(Chiyo.guilds))
            cover.log(f"{Chiyo.user} is online! | Currently in {amount_of_servers} servers!", cover.bcolors.OKGREEN)
        
        @Chiyo.event
        async def on_message(message):
            await Chiyo.wait_until_ready()
            await Chiyo.process_commands(message)

            cover.log(f"[{message.guild}] [{message.channel}] {message.author}: {message.content}", cover.bcolors.OKBLUE)

            for r in BEATMAP.findall(message.content):
                
                for m in (0, 1, 2, 3):
                    req = cover.get_beatmap(int(r), m)

                    if not req:
                        continue
                    else:
                        break
                
                if not req: 
                    return
                
                e = discord.Embed(
                    color = message.author.color.value
                )

                e.set_author(
                    name = "{artist} - {title} [{version}] ★{starRating}".format(
                        **req, starRating = round(float(req['difficultyrating']), 2)
                    ), 
                    url = "https://akatsuki.pw/b/{beatmap_id}".format(**req), 
                    icon_url = config.logo if config.logo else 'https://akatsuki.pw/static/logos/logo.png'
                )

                e.set_image(
                    url = "https://assets.ppy.sh/beatmaps/{beatmapset_id}/covers/cover.jpg".format(**req)
                )

                e.add_field(
                    name = 'Download Links:',
                    value = (
                            '▸ [beatconnect](https://beatconnect.io/b/{beatmapset_id})\n'
                            '▸ [osu!gatari](https://osu.gatari.pw/b/{beatmap_id})\n'
                            '▸ [osu!](https://osu.ppy.sh/b/{beatmap_id})\n'
                            '▸ [osu! (old)](https://old.ppy.sh/s/{beatmapset_id})').format(**req)        
                    )
                
                Chiyo.cache[message.channel.id] = req['beatmap_id']
                return await message.channel.send(embed = e)
                
                


        Chiyo.run(config.token)
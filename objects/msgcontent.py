import time
from ext import glob
from helpers import note
from typing import Optional
from objects.const import Server
from objects.players import Player
from discord.ext.commands import Context

class MsgContent:
    def __init__(self) -> None:
        self.mode: int = 0
        self.page: int = 0
        self.relax: int = 0
        self.player: Optional[Player] = None
        self.server: Optional[Server] = None
        self.server_name: Optional[str] = None
        self.start_time: Optional[float] = None
    
    @classmethod
    async def from_discord_msg(
        cls, ctx: Context, 
        type: Optional[str] = None
    ):
        content = cls()
        content.start_time = time.time()
        server = Server.Bancho
        relax = mode = index = 0
        msg: list[str] = ctx.message.content.lower().split()[1:]

        if '-p' in msg:
            index = msg[msg.index('-p') + 1]
            msg.remove('-p')
            msg.remove(index)
            if not index.isdecimal():
                await ctx.send(
                    'Please provide a number for `-p`'
                )
                return

            index = int(index)
            index = index - 1 if index > 0 else index
            
            content.page = index

        if '-std' in msg:
            msg.remove('-std')
            mode = 0
        elif '-taiko' in msg:
            msg.remove('-taiko')
            mode = 1
        elif '-ctb' in msg:
            msg.remove('-ctb')
            mode = 2
        elif '-mania' in msg:
            msg.remove('-mania')
            mode = 3
        
        content.mode = mode

        if '-rx' in msg:
            msg.remove('-rx')
            server = Server.Akatsuki
            relax = 1
        
        if '-bancho' in msg:
            msg.remove('-bancho')
            server = Server.Bancho
        elif '-akatsuki' in msg:
            msg.remove('-akatsuki')
            server = Server.Akatsuki
        
        content.server = server
        content.relax = relax

        name = ' '.join(msg)
        if type == 'connect' and not name:
            await ctx.send("Please provide a name.")
            return

        server_name = content.server_name = server.name.lower()

        if not type:
            if ctx.message.mentions:
                mentioned = ctx.message.mentions[0]
                user = glob.db.find_one({"_id": mentioned.id})
                if not user or server_name not in user:
                    await ctx.send(
                        "User couldn't be found in our database! "
                        f"{mentioned.name}, Try connecting a user "
                        "to our database by doing `;connect (your username)`"
                    )
                    return
                
                name = user[server_name]

            elif not name:
                user = glob.db.find_one({"_id": ctx.author.id})
                if not user or server_name not in user:
                    await ctx.send(
                        "User couldn't be found in our database! "
                        "Try connecting a user to our database"
                        "by doing `;connect (your username)`"
                    )
                    return
                
                name = user[server_name]
            
            else:
                pass
        
        if server == Server.Bancho:
            p = content.player = await Player.from_bancho(
                name, mode
            )
        else:
            p = content.player = await Player.from_akatsuki(
                name, mode, relax
            )
        
        if not p:
            await note(
                statement = "if not p:",
                name_or_id = name,
                mode = mode,
                server = server_name,
                function = 'MsgContent.from_discord_msg'
            )
            await ctx.send(
                f"No user from `{server_name}` was found!"
            )
            return

        return content
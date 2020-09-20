import discord
from discord.ext import commands
from config import token, prefix
from events import Chiyo

client = commands.Bot(command_prefix = prefix, case_insensitive=True)

chiyo = Chiyo(token, client)
chiyo.run()

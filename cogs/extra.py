import discord
from discord.ext import commands

class extra(commands.Cog):

    def __init__(self, client) -> None:
        self.client = client
        self.QUERY = client.db
        self.cache = client.cache

    @commands.command(aliases=['help'])
    async def faq(self, ctx):
        embed = discord.Embed(
            title = "Commands", 
            description = "what it do?",
            color = ctx.message.author.roles[len(ctx.message.author.roles) - 1].color
        )
        embed.add_field(
            name = ';[recent, r, rc, rs] (username or @someone) (-rx) (-p (numnber)) (-std) (-taiko) (-ctb) (-mania)',
            value = "This command gets a user's recent akatsuki play!",
            inline = False
        )
        embed.add_field(
            name = ';[top, t] (username or @someone) (-rx) (-p (numnber)) (-std) (-taiko) (-ctb) (-mania)',
            value = "This command gets a user's top akatsuki play!",
            inline = False
        )
        embed.add_field(
            name = ';[compare, c] (username or @someone) (-rx) (-p (numnber)) (-std) (-taiko) (-ctb) (-mania)',
            value = "This command compares a play\nfrom the most recent used command such as [;r or ;t] on akatsuki!",
            inline = False
        )
        embed.add_field(
            name = ';[profile, p, osu] (username or @someone) (-rx) (-std) (-taiko) (-ctb) (-mania)',
            value = "This command gets a user's stats on akatsuki!",
            inline = False
        )
        return await ctx.send(embed = embed)


def setup(client):
    client.add_cog(extra(client))
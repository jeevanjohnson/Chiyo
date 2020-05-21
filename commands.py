import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content.startswith(';faq'):
            await message.channel.send('coming soon.')

client = MyClient()
client.run('NzA1MTc2NjYyMzY2NDg2NTI5.Xqn5AQ.FUYBk7XlBP-6RglVFrNLAC8lDVA')
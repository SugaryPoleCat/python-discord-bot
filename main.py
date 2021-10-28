import discord
from decouple import config

DEV_TOKEN = config('DEV_TOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        # if the message author is the bot
        print(message.author.bot)
        if message.author == client.user:
            return
        if message.content.startswith('!hello'):
            await message.channel.send("kukaren")

client = MyClient()
client.run(DEV_TOKEN)
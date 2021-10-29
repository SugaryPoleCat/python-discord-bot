import discord
from decouple import config
import requests
import random
from .hello import Hello

DEV_TOKEN = config('DEV_TOKEN')

# doesnt wrok probbaly because the api is bad now ?
# idk.
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    if(response.status_code == 200):
        json_data = response.json(response.text)
        quote = json_data[0]['q'] + " -" + json_data[0]['a']
        return(quote)
    else:
        text = "The response failed."
        return(text)

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

starter_encouragemnets = ["Cheer up!", "Hang in there!", "You are a great person!", "You are doing great!", "You are fantastic!"]

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        # if the message author is the bot
        # print(message.author.bot)
        msg = message.content
        if message.author.bot == True:
            print("user was a bot")
            return
        if message.content.startswith('!hello'):
            await Hello.get_hello(message)

        if message.content.startswith('!quote'):
            # quote = get_quote()
            quote = "this should be a random quote but the API is broken."
            await message.channel.send(quote)

# if you want it to work without checking if its a command, comment the line below.
        # if message.content.startswith('!insp'):
            # IF any word in your message.content matcehs a sad_word, this will happen.
        if any(word in msg for word in sad_words):
            await message.channel.send(random.choice(starter_encouragemnets))

client = MyClient()
client.run(DEV_TOKEN)
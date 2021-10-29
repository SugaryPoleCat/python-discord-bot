import discord

class Hello(message):
	async def get_hello(message):
		await message.channel.send("Hello!")
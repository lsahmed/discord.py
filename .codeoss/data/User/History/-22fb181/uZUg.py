import main
import discord
import requests

intents = discord.Intents.default()
discord.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    print(main.on_message())
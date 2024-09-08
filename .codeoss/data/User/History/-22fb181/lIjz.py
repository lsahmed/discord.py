import main
import discord
import requests

intents = discord.Intents.default()

@client.event
async def on_message(message):
    print(main.on_message())
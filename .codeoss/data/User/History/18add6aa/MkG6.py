import discord
from dotenv import load_dotenv
import requests
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    hello = message.content.lower()
    if hello == "hello":
        await message.channel.send("Hello")
    if message.content.startswith("$weather"):
        lisplace = message.content.split(" ")
        if len(lisplace)>1:
            place = lisplace[1]
            await message.channel.send(place)


load_dotenv()
token = os.getenv('TOKEN')
client.run(token)
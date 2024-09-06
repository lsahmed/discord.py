import discord
from getapi import weather
from dotenv import load_dotenv
import os

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if(message.content.startswith("$weather")):
        parts = message.content.split(" ")
        if len(parts)>1:
            place = parts[1]
            await message.channel.send(weather(place))
        else:
            await message.channel.send("$weather commands accept atleast one arguement ")

load_dotenv()
token = os.getenv('TOKEN')
client.run(token)
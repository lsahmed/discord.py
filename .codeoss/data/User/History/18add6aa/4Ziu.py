import discord
from dotenv import load_dotenv
from getapi import api_weather
import requests
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
    
    hello = message.content.lower()
    if hello == "hello":
        await message.channel.send("Hello")

    if message.content.startswith("$weather"):
        parts = message.content.split(" ")
        if len(parts) > 1:
            place = parts[1]
            # Fetch weather data
            weatherdata = api_weather(place)
            await message.channel.send(weatherdata)
        else:
            await message.channel.send("Please provide a location after the $weather command.")

load_dotenv()
token = os.getenv('TOKEN')
client.run(token)

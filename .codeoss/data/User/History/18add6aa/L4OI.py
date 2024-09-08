import discord
from dotenv import load_dotenv
import requests
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def api_weather(place):
    load_dotenv()
    apitoken = os.getenv('APITOKEN')
    response = requests.get(f"https://api.weatherapi.com/v1/current.json?key={APITOKEN}&q={place}")
    data = response.json()
    status = response.status_code

    if status == 200:
        # Extract data from API
        city = data["location"].get("name")
        region = data["location"].get("region")
        country = data["location"].get("country")
        temp = data["current"].get("temp_c")
        condition = data["current"]["condition"].get("text")
        humidity = data["current"].get("humidity")
        last_updated = data["current"].get("last_updated")

        def day_or_night():
            if data["current"].get("is_day") == 0:
                return "Night"
            elif data["current"].get("is_day") == 1:
                return "Day"
            return "Unknown"

        diurnal = day_or_night()
        weatherdata = (f"Showing current weather for {place}\n"
                       f"Temperature: {temp}°C\n"
                       f"Condition: {condition}\n"
                       f"Humidity: {humidity}%\n"
                       f"Day/Night Cycle: {diurnal}\n"
                       f"Last updated on: {last_updated}")
    else:
        weatherdata = "Could not retrieve weather data."

    return weatherdata

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

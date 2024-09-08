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
            
            def apiwather():
                load_dotenv()
                apitoken = os.getenv('APITOKEN')
                response = requests.get(f"https://api.weatherapi.com/v1/current.json?key={apitoken}&q={place}")
                data = response.json()
                status = response.status_code
                if status == 200:
                    # All inputs from API
                    city = data["location"].get("name")
                    region = data["location"].get("region")
                    country = data["location"].get("country")
                    # Weather inputs
                    temp = data["current"].get("temp_c")
                    condition = data["current"]["condition"].get("text")
                    humidity = data["current"].get("humidity")
                    last_updated = data["current"].get("last_updated")

                    def dayornight():
                        diurnal = ""
                        if(data["current"].get("is_day")==0):
                            diurnal = "Night"
                        elif(data["current"].get("is_day")==1):
                            diurnal = "Day"

                        return diurnal
                    weatherdata = (f"Showing current weather for {place}\ntemprature: {temp}\ncondition: {condition}\nhumidity: {humidity}\nDiural_cycle: {diu}\nlast updated on {last_updated}")
                return weatherdata
            
                


load_dotenv()
token = os.getenv('TOKEN')
client.run(token)
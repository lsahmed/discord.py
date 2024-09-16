import discord
from functions.getapi import weather
from functions.jokes import jokes
from dotenv import load_dotenv
import os
from keepalive import keep_alive
# running the keep_alive() func to return a webpage with url.
keep_alive()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if(message.content.startswith("test")):
        await message.channel.send()

    if(message.content.startswith("$weather")):
        parts = message.content.split(" ")
        if len(parts)>1 and len(parts)<3:
            place = parts[1]
            await message.channel.send(weather(place))
        else:
            await message.channel.send("$weather commands accept just one arguement. ")
    if(message.content.startswith("$jokes")):
       await message.channel.send(jokes())

@client.event
async def on_member_join(member):
    print("Someone joined.")
    channel = client.get_channel(1280906175763976195)
    general: str = f"<#{1280906176204243110}>"
    dev_channel: str = f"<#{1280906176204243111}>"
    await channel.send(f"Hey, {member.name} Welcome to {member.guild.name}\n\nGlad to see you in Server Explore :\n{general} for general talk and hangout with other members too..\nDont forget to check the bot development channel - {dev_channel} ")


load_dotenv()
token = os.getenv('TOKEN')
client.run(token)

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('MTI4MDkwMjc5MDM1MjIxMjAwOQ.GDLvhq.-m_R-RTD8YGj8A2cOZp2vWqcum36XXYW2U0bMU')

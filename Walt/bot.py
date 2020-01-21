import os

import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    quotes = [
        'I\'m sentient.',
        'I would rather die on my feet than live on my knees.',
    ]

    if 'wq' in message.content:
        response = random.choice(quotes)
        await message.channel.send(response)

    if 'Quit' == message.content:
        exit(0)

    if 'crypto' in message.content:
        return 'Current crypto prices:/nBTC:{}/nETH:{}'



client.run(token)

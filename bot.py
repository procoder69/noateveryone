import discord
import asyncio
import random
import pickle
import os
from tendo import singleton
from profanities import profs
from token import tok

me = singleton.SingleInstance()
client = discord.Client()

@client.event
async def on_ready(): #prints log in info
        print("Logged in as")
        print(client.user.name)
        print(client.user.id)

@client.event
async def on_message(message):
        if "@everyone" in message.content: #deletes any message that contains the string @everyone
                await client.send_message(message.channel, "@ everyone is disabled on this server")
                await client.delete_message(message)

        for word in profs:
                if word in message.content.lower(): #deletes any message that contains profanity
                        await client.send_message(message.channel, "profanities are not allowed on this server")
                        await client.delete_message(message)

tok()

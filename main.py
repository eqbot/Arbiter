'''
Arbiter : A discord bot made for simple server administration
v1.0
@author: Trent Kenny
'''

import discord
import asyncio

client = discord.Client()



@client.event
async def on_message(message):
'''
Arbiter : A discord bot made for simple server administration
v1.0
@author: Trent Kenny
'''

import discord
import asyncio
import commands
import shlex
import configparser
import sys

client = discord.Client()

#setup config
config = configparser.ConfigParser()
if config.read('config.ini') == []:
    config['VALUES'] = {'token': ''}
    print('Config file needs to be set up before use.')
    config.write('config.ini')
    sys.exit()
else:
    token = config['VALUES']['token']
    
users = configparser.ConfigParser()
if users.read('users.ini') == []:
    config['ROOT'] = {'username': 'root',
                      'discriminator': 1337,
                      'powerlevel': 0
                      }
@client.event
async def on_message(message):
    if message.content.startswith('!'):
        msgIn = message.content[1:]
        msgIn = shlex.split(msgIn)
        async for command in commands.allCommands:
            if msgIn[0] == command.name:
                (out,outFile) = command.execute(msgIn[1:])
                if out is not None:
                    await client.send_message(message.channel, out)
                if outFile is not None:
                    await client.send_file(message.channel, outFile)
                    
client.run()
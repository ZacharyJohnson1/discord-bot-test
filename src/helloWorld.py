import discord
import re

#create client
discord_client = discord.Client()

'''event to debug ready state of bot'''
@discord_client.event
async def on_ready():

    print('bot is online')


'''event to handle messages addressed at bot'''
@discord_client.event
async def on_message(msg):

    if msg.author == discord_client.user or msg == None:
        return

    user_msg_greeting = r'\bhello\b|\bhi\b|\bhey\b'
    user_msg_content = str(msg.content).lower()

    match = re.search(user_msg_greeting, user_msg_content)
    if match:
        await msg.channel.send('Hello')
        await msg.add_reaction('\U0001F44B')


'''echo user reactions'''
@discord_client.event
async def on_reaction_add(reaction, user):

    print(reaction, user)
    await reaction.message.channel.send(f'{user} reacted with {reaction.emoji}')


'''read token from file'''
with open('token.txt') as token_file_client:
    token = token_file_client.readline(-1)

#run client
discord_client.run(token)
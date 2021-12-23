import discord
import re

#create client
intents = discord.Intents.default()
intents.members = True
discord_client = discord.Client(intents=intents)

#read token from file
with open('token.txt') as token_file_client:
    token = token_file_client.readline(-1)


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
        await msg.channel.send('Hello World!')
        await msg.add_reaction('\U0001F44B')


'''echo user reactions'''
@discord_client.event
async def on_reaction_add(reaction, user):

    if user != discord_client.user:
        await reaction.message.channel.send(f'{user} reacted with {reaction.emoji}')


'''track edited messages'''
@discord_client.event
async def on_message_edit(before, after):

    await before.channel.send(f'{before.author} edited a message:\nBefore: {before.content}\nAfter: {after.content}')


''' main '''
if __name__ == "__main__":

    #run client
    discord_client.run(token)
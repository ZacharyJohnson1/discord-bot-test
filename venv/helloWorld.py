import discord

#create client
discord_client = discord.Client()

#event to debug ready state of bot
@discord_client.event
async def on_ready():

    print('bot is online')


#event to handle messages addressed at bot
@discord_client.event
async def on_message(msg):

    if msg.author == discord_client.user:
        return

    content = str(msg.content).lower()
    if content.find('hello') or content.find('hi') or content.find('hey'):
        await msg.channel.send('Hello')


#read token from file
with open('token.txt') as token_file_client:
    token = token_file_client.readline(-1)
#run client
discord_client.run(token)
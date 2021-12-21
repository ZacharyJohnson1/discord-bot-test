import discord

#create client
discord_client = discord.Client()

#read token from file
with open('token.txt') as token_file_client:
    token = token_file_client.readline(-1)


'''event to debug ready state of bot'''
@discord_client.event
async def on_ready():

    print('bot is online')


'''assigning roles with reactions'''
@discord_client.event
async def on_raw_reaction_add(payload):

    emoji_happy_unicodes = [
        '\U0001F600',
        '\U0001F603',
        '\U0001F604',
        '\U0001F601',
        '\U0001F642',
        '\U0001F643',
        '\U0001F60A'
    ]

    emoji_sad_unicodes = [
        '\U0001F62D'
    ]

    payload_message_id = payload.message_id
    target_message_id = 922283125843845241

    if payload_message_id == target_message_id:
        print(payload.emoji.name)
        if payload.emoji.name in emoji_happy_unicodes:
            print('happy')

        elif payload.emoji.name in emoji_sad_unicodes:
            print('sad')


''' main '''
if __name__ == "__main__":

    #run client
    discord_client.run(token)
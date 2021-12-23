import discord

#create client
intents = discord.Intents.default()
intents.members = True
discord_client = discord.Client(intents=intents)

#read token from file
with open('token.txt') as token_file_client:
    token = token_file_client.readline(-1)

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

'''event to debug ready state of bot'''
@discord_client.event
async def on_ready():

    print('bot is online')


'''assigning roles with reactions'''
@discord_client.event
async def on_raw_reaction_add(payload):

    payload_message_id = payload.message_id
    target_message_id = 922283125843845241
    guild_id = payload.guild_id
    guild = discord_client.get_guild(guild_id)

    if payload_message_id == target_message_id:
        if payload.emoji.name in emoji_happy_unicodes:
            role = discord.utils.get(guild.roles, name='Happy')
            await payload.member.add_roles(role)
        elif payload.emoji.name in emoji_sad_unicodes:
            role = discord.utils.get(guild.roles, name='Sad')
            await payload.member.add_roles(role)


'''remove roles with reactions'''
@discord_client.event
async def on_raw_reaction_remove(payload):

    payload_message_id = payload.message_id
    target_message_id = 922283125843845241
    guild_id = payload.guild_id
    guild = discord_client.get_guild(guild_id)

    if payload_message_id == target_message_id:
        member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
        if payload.emoji.name in emoji_happy_unicodes:
            role = discord.utils.get(guild.roles, name='Happy')
            await member.remove_roles(role)
        elif payload.emoji.name in emoji_sad_unicodes:
            role = discord.utils.get(guild.roles, name='Sad')
            await member.remove_roles(role)


''' main '''
if __name__ == "__main__":

    #run client
    discord_client.run(token)
import discord

discord_client = discord.Client()
<<<<<<< HEAD

with open('token.txt') as token_file_client:
    token = token_file_client.readline(-1)

discord_client.run(token)
=======
with open('token.txt') as token_file_client:
    token = token_file_client.readlines()

discord_client.run(token[0])
>>>>>>> 4ab96f1d306aa370cbbfa3eacc31a35c9157b737

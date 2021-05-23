import discord

discord_client = discord.Client()
with open('token.txt') as token_file_client:
    token = token_file_client.readlines()

discord_client.run(token[0])
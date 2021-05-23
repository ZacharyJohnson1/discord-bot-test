import discord

discord_client = discord.Client()

with open('token.txt') as token_file_client:
    token = token_file_client.readline(-1)

discord_client.run(token)

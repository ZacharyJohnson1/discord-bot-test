import discord
from discord.ext import commands
from functools import reduce

#create client
discord_client = commands.Bot(command_prefix='!')

#read token from file
with open('token.txt') as token_file_client:
    token = token_file_client.readline(-1)


'''event to debug ready state of bot'''
@discord_client.event
async def on_ready():

    print('bot is online')


'''hello command'''
@discord_client.command()
async def hello(context, *args):
    if args != None:
        for arg in args:
            print(arg, sep=' ')
    await context.send(f'Hello {context.author}')


''' simple addition '''
@discord_client.command()
async def add(context, *args):

    if not check_list_digits(args):
        await context.send('Error: Invalid Arguments. Only Numbers Allowed.')

    values_str = ''
    if args != None and len(args) > 1:
        for arg in range(len(args)-1):
            values_str += f'{args[arg]} + '
        values_str += f'{args[-1]} '

        sum = reduce(lambda x, y: x + y, list(map(float, args)))
        await context.send(f'{values_str} = {sum}')
    else:
        await context.send(f' @{context.author} Invalid arguments')


''' simple subtraction '''
@discord_client.command()
async def subtract(context, *args):

    if not check_list_digits(args):
        await context.send('Error: Invalid Arguments. Only Numbers Allowed.')

    values_str = ''
    if args != None and len(args) > 1:
        for arg in range(len(args)-1):
            values_str += f'{args[arg]} - '
        values_str += f'{args[-1]} '

        diff = reduce(lambda x, y: x - y, list(map(float, args)))
        await context.send(f'{values_str} = {diff}')
    else:
        await context.send(f' @{context.author} Invalid arguments')

''' simple multiplication '''
@discord_client.command()
async def multiply(context, *args):

    if not check_list_digits(args):
        await context.send('Error: Invalid Arguments. Only Numbers Allowed.')

    values_str = ''
    if args != None and len(args) > 1:
        for arg in range(len(args)-1):
            values_str += f'{args[arg]} * '
        values_str += f'{args[-1]} '

        sum = reduce(lambda x, y: x * y, list(map(float, args)))
        await context.send(f'{values_str} = {sum}')
    else:
        await context.send(f' @{context.author} Invalid arguments')


''' simple division '''
@discord_client.command()
async def divide(context, *args):

    if not check_list_digits(args):
        await context.send('Error: Invalid Arguments. Only Numbers Allowed.')

    values_str = ''
    if args != None and len(args) > 1:
        for arg in range(len(args)-1):
            values_str += f'{args[arg]} / '
        values_str += f'{args[-1]} '

        diff = reduce(lambda x, y: x / y, list(map(float, args)))
        await context.send(f'{values_str} = {diff}')
    else:
        await context.send(f' @{context.author} Invalid arguments')


def check_list_digits(n):

    return all(element.isdigit() for element in n)


''' main '''
if __name__ == "__main__":

    #run client
    discord_client.run(token)
import discord
from discord.ext import commands
from crawling import stations, busses

#pip install discord.py
msg = ''
num = ''
bot = commands.Bot(command_prefix='#', intents=discord.Intents.all())
 
@bot.event
async def on_ready():
    print(f'Login bot: {bot.user}')
 
@bot.command(name='hello')
async def inpue_message(ctx, *, message=None):
    await ctx.channel.send(message)
    await ctx.channel.send(f'{ctx.author.mention}님 안녕하세요!')

@bot.command(name='station')
async def bus_station(ctx, *, message=None):
    global msg
    msg = message
    arr = stations(msg)
    for i in range(len(arr)):
        tmp = str(arr[i][0]) + ' : ' + arr[i][1]
        await ctx.channel.send(tmp)

@bot.command(name='bus')
async def bus_numbers(ctx, *, number=None):
    global num
    num = number
    bus_number, bus_location = busses(int(num), msg)
    for i in range(len(bus_number)):
        await ctx.channel.send(bus_number[i])
        await ctx.channel.send(bus_location[i])

bot.run('discord boy key')

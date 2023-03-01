import discord
from discord.ext import commands
 
bot = commands.Bot(command_prefix='#', intents=discord.Intents.all())
 
@bot.event
async def on_ready():
    print(f'Login bot: {bot.user}')
 
@bot.command()
async def hello(message):
    await message.channel.send(f'{message.author.mention}님 안녕하세요!')

bot.run('MTA4MDQ1NTYwMDY5OTM2MzM1OA.G3DBgW.bzx5gUzvmW1Jpv5aeIKt-weU9Xj_1QAfu5-zeQ')

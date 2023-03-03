import discord
from discord.ext import commands

#pip install discord.py
bot = commands.Bot(command_prefix='#', intents=discord.Intents.all())
 
@bot.event
async def on_ready():
    print(f'Login bot: {bot.user}')
 
@bot.command(name='hello')
async def inpue_message(ctx, *, message=None):
    await ctx.channel.send(message)
    await ctx.channel.send(f'{ctx.author.mention}님 안녕하세요!')

bot.run('discord bot key')

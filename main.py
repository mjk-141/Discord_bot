import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print(f'Login bot: {bot.user}')

@bot.command()
async def hello(message):
    await message.channel.send('Hi!')

bot.run()
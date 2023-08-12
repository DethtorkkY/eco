import discord
from discord.ext import commands
import random
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

items = {
    'бумага': '2-5 месяцев',
    'банановая кожура': '2-5 недель',
    'пластиковая бутылка': '400 лет'
}

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def decomposition(ctx, item):
    if item in items:
        time_to_decompose = items[item]
        await ctx.send(f'Предмет {item} разлагается примерно {time_to_decompose}')
    else:
        await ctx.send('Про такой предмет еще нет информации')

bot.run("token")

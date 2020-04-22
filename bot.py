import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')
Token = ''

@bot.event
async def on_ready():
  print("Bot is online")

@bot.event
async def on_member_join(member):
  channel = bot.get_channel(702443826916229160)
  await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
  channel = bot.get_channel(702443826916229160)
  await channel.send(f'{member} leave!')

bot.run('')
import discord
from discord.ext import commands
import json

with open('./setting.json', mode='r', encoding='utf8') as jFile:
  jdata = json.load(jFile)

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
  print("Bot is online")

@bot.event
async def on_member_join(member):
  channel = bot.get_channel(int(jdata["WelecomChannel"]))
  await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
  channel = bot.get_channel(int(jdata["WelecomChannel"]))
  await channel.send(f'{member} leave!')

@bot.command()
async def ping(ctx):
  await ctx.send(bot.latency)



bot.run(jdata["Token"])
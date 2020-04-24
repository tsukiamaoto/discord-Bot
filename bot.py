import discord
from discord.ext import commands
import json
import os

with open('./setting.json', mode='r', encoding='utf8') as jFile:
  jdata = json.load(jFile)

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
  print("Bot is online")


@bot.command()
async def load(ctx, extensionName):
  bot.load_extension(f'commands.{extensionName}')
  await ctx.send(f'Loaded {extensionName} done.')

@bot.command()
async def unload(ctx, extensionName):
  bot.unload_extension(f'commands.{extensionName}')
  await ctx.send(f'Unloaded {extensionName} done.')

@bot.command()
async def reload(ctx, extensionName):
  bot.reload_extension(f'commands.{extensionName}')
  await ctx.send(f'Reloaded {extensionName} done.')

#導入所有commands
for filename in os.listdir('./commands'):
  if filename.endswith('.py'): #格式是py
    bot.load_extension(f'commands.{filename[:-3]}')

if __name__ == "__main__":
  bot.run(jdata["Token"])
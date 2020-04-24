import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('./setting.json', mode='r', encoding='utf8') as jFile:
  jdata = json.load(jFile)

class Event(Cog_Extension):
  @commands.Cog.listener()
  async def on_member_join(self, member):
    channel = self.bot.get_channel(int(jdata["WelecomChannel"]))
    await channel.senxd(f'{member} join!')

  @commands.Cog.listener()
  async def on_member_remove(self, member):
    channel = self.bot.get_channel(int(jdata["WelecomChannel"]))
    await channel.send(f'{member} leave!')

  @commands.Cog.listener()
  async def on_message(self, msg):
    if msg.content == 'QQ':
      await msg.channel.send(f'哭阿')

def setup(bot):
  bot.add_cog(Event(bot))
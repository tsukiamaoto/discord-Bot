import discord
from discord.ext import commands
from core.classes import Cog_Extension

class React(Cog_Extension):
  @commands.command()
  async def 面試(self, ctx):
    await ctx.send(111)
def setup(bot):
  bot.add_cog(React(bot))
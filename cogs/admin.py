# -*- coding: utf-8 -*-

from discord.ext import commands
import discord
from helpers.checks import requires

class Admin(commands.Cog):
    """Administrative commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="restart")
    @requires(1000)
    async def restart(self, ctx):
        """Restarts the bot"""
        await self.bot.logout()

    @commands.group(name="cogs")
    @requires(1000)
    async def cogs_group(self, ctx: commands.Context):
        if ctx.invoked_subcommand == None:
            await ctx.channel.send("Usage: `!cogs <load | unload | reload> [cogs]`")

    #@cogs_group.command(name="load")

def setup(bot):
    bot.add_cog(Admin(bot))

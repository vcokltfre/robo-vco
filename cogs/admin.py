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

def setup(bot):
    bot.add_cog(Admin(bot))

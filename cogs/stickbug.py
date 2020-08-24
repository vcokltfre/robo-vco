# -*- coding: utf-8 -*-

from discord.ext import commands
import discord
from helpers.checks import requires
import requests
import gsbl

class Stickbug(commands.Cog):
    """Generate a stickbug video from an image"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="stickbug", aliases=["sb"])
    async def stickbug(self, ctx: commands.Context):
        async with ctx.channel.typing():
            attachments = ctx.message.attachments

            if len(attachments) != 1:
                await ctx.channel.send("You must attach one image with this command.")
                return

            response = requests.get(str(attachments[0].url), allow_redirects=True)

            with open("./data/temp/stick.png", 'wb') as f:
                f.write(response.content)

            video = gsbl.generate_stick_bug("./data/temp/stick.png")
            gsbl.save_video(video, "./data/temp/stick.mp4")

            await ctx.channel.send(file=discord.File("./data/temp/stick.mp4", "output.mp4"))

def setup(bot):
    bot.add_cog(Stickbug(bot))

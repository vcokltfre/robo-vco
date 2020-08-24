import discord
import helpers.pregenerator

from discord.ext import commands
from discord_logger import DiscordLogger
from helpers.config_helper import ConfigHelper

cfg = ConfigHelper().read()


class Bot(commands.Bot):
    """A subclassed commands.Bot"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = DiscordLogger(webhook_url=cfg["logger_hook"], **cfg["logger_ops"])
        self.logger.construct(title="Startup", description="Robo Vco is starting up.")
        self.logger.send()

    def load_extensions(self, cogs: list):
        """Loads a list of cogs"""
        loading_data = {
            "success":0,
            "failure":0
        }
        for cog in cogs:
            try:
                super().load_extension(cog)
                loading_data["success"] += 1
            except Exception as e:
                loading_data["failure"] += 1
                self.logger.construct(title="Startup", description=f"Cog `{cog}` failed to load.", error=e)
                self.logger.send()
        self.logger.construct(title="Startup", description="Cog loading has finished.", metadata=loading_data)
        self.logger.send()

    async def on_error(self, event: str, *args, **kwargs):
        self.logger.construct(title="Runtime Error", error=event, metadata=kwargs)
        self.logger.send()


if __name__ == "__main__":
    bot = Bot(
        command_prefix="!",
        max_messages=10000,
        #allowed_mentions=discord.AllowedMentions(everyone=False, users=True, roles=False),
        help_command=commands.MinimalHelpCommand(dm_help=True, no_category="General")
    )

    bot.load_extensions(cfg["cogs"])
    bot.run(cfg["token"])
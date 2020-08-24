from discord.ext import commands
from helpers.permissions import PermissionManager

def requires(level: int):
    async def check(ctx: commands.Context):
        roles = [role.name for role in ctx.author.roles]
        uid = str(ctx.author.id)

        valid = PermissionManager().has_perms(roles, uid, level)

        if valid:
            return True

        if not ctx.message.content.startswith("!help"):
            await ctx.send(f"You do not have the required permission level ({level}) required to run this command.", delete_after=15)
        return False

    return commands.check(check)

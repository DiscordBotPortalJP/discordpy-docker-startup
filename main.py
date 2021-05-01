from discord.ext import commands
from os import environ

bot = commands.Bot(command_prefix="!")


@bot.command()
async def ping(ctx: commands.Context) -> None:
    await ctx.reply("pong")


bot.run(environ["DISCORD_BOT_TOKEN"])

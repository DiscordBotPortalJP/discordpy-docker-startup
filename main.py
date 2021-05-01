import discord
from os import environ

client = discord.Client()

client.run(environ["BOT_TOKEN"])

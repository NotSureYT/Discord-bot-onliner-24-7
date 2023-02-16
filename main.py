import discord
import os
from discord.ext import commands

client=commands.Bot(command_prefix="your prefix here")

@client.event
async def on_ready():
  print("Your bot is online!")

client.run(os.environ['token'])

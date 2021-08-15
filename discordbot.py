from discord.ext import commands
import os
import discord

bot = commands.Bot(command_prefix='y.', help_command=None)
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_ready():
    print("Logged in ^^")

bot.run(token)

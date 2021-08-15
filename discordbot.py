from discord.ext import commands
import os
import discord

bot = commands.Bot(command_prefix='-_-;', help_command=None)
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_ready():
    print("Logged in ^^")
    
@bot.command
async def change(change, data=None, content=None):
    if content == None or data == None:
        return
    with oepn("test.json", "r") as f:
        test = json.load(f)
    test[str(data)] = str(content)
    with open("test.json", "w") as f:
        json.dump(test, f, indent=4)
    await change.send("jsonのデータ追加してやったぞ...\nだっる。")

bot.run(token)

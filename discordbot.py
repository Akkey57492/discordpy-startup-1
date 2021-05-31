from discord.ext import commands
import os
import traceback
import discord

bot = commands.Bot(command_prefix='y.', help_command=None)
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def hello(ctx):
    await ctx.channel.send('good')
@bot.command()
async def ping(ctx):
    await ctx.channl.send('pongだよ！！！！！！！！！')
@bot.command()
async def help(ctx):
    help = discord.Embed(title='Help', description='y.ping\ny.hello')
    await ctx.channel.send(embed=help)

bot.run(token)

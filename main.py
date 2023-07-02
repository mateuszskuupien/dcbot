import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.command()
async def sendx(ctx, *, arg):
    await ctx.send(arg)


bot.run(
    'MTEyNTAwNDM3MzY3MjU5MTQzMA.Gbjwtm.RmikAP4_K7axDu8f1-nHuEHPqbuqBBS5-dDF6E')

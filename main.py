import discord
import json
from discord.ext import commands, tasks



intents = discord.Intents().default()
intents.message_content = True



bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

with open('config.json') as f:
    data = json.load(f)
TOKEN = data['BOT_TOKEN']

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    channel = bot.get_channel(1125005010690920461)
    await channel.send('Ready to go')


@bot.command()
async def join(ctx):
    try:
        channel = ctx.author.voice.channel
        await channel.connect()
    except AttributeError:
        await ctx.send("You're currently not on any channel.")

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
    else:
        await ctx.send('I am not currently in a voice channel.')

@bot.command()
async def ping(ctx):
    await ctx.reply('<:zap:1127665844676206676> Pong! <:zap:1127665844676206676>')

@bot.command()
async def help(ctx):
    embed=discord.Embed(title="<:zap:1127665844676206676> Path of Enlightenment: Guidance from Prometheus", description="------", color=0x13aec3)
    embed.set_author(name="mathie", url="https://github.com/mateuszskuupien", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSeNU-w9yItRfskqQcAu83QpLx7vg7jtgUX15Jec7EBCg&s")
    embed.set_thumbnail(url="https://t4.ftcdn.net/jpg/05/62/26/83/360_F_562268305_PAhZKJquJnGun5zwCc1e2GjfXHG0sAGk.jpg")
    embed.add_field(name="!join <:zap:1127665844676206676>", value="Summon Prometheus, the celestial companion, and traverse the divine halls of Olympus together.", inline=False)
    embed.add_field(name="!leave", value="Release your connection to Prometheus, the titan of enlightenment, as you step back into the mortal world.", inline=False)
    embed.add_field(name="!ping", value=" Challenge your opponents to a mythical game of ping-pong, where lightning-fast reflexes reign supreme.", inline=False)
    embed.set_footer(text="\"Immortality is not the absence of death, but rather the eternal presence of one's deeds and legacy.\"")
    await ctx.send(embed=embed)
bot.run(TOKEN)

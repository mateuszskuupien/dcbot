import discord
import json
from discord.ext import commands, tasks

intents = discord.Intents().all()
client = commands.Bot(command_prefix='!', intents=intents, help_command=None, activity=discord.Activity(type=discord.ActivityType.listening, name="\U0001FA90 \n prometheusbot.com \U0001FA90 | \u2757help"))
voice_clients= {}
with open("config.json") as f:
    data = json.load(f)
TOKEN = data["BOT_TOKEN"]

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.reply("**Invalid command. Try using** `!help` **to figure out commands!**")

@client.event
async def on_ready():
    print(f"Logged in as {client.user.name} ({client.user.id})")

@client.event
async def on_member_join(member):
    channel = member.guild.system_channel
    if channel:
        await channel.send(f"Embrace wisdom, new traveler! ♆ {member.mention}! ♆")

@client.command()
async def join(ctx):
    try:
        if ctx.voice_client and ctx.voice_client.channel == ctx.author.voice.channel:
            await ctx.send("We are on the same channel already...")
        elif ctx.voice_client is not None and ctx.voice_client.is_connected():
            await ctx.voice_client.move_to(ctx.author.voice.channel)
        else:
            await ctx.author.voice.channel.connect()
    except AttributeError:
        await ctx.send("You're currently not on any channel.")

@client.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
    else:
        await ctx.send("I am not currently in a voice channel.")

@client.command(aliases=["PING","Ping","ping!","PING!","Ping!"])
async def ping(ctx):
    await ctx.reply("<:ping_pong:1128002634238935111> Pong! ")

@client.command()
async def help(ctx):
    embed=discord.Embed(title="<:classical_building:1127934014712459344> Guidance from Prometheus <:classical_building:1127934014712459344>", description="\u200b", color=0x13aec3)
    embed.set_author(name="mathie", url="https://github.com/mateuszskuupien", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSeNU-w9yItRfskqQcAu83QpLx7vg7jtgUX15Jec7EBCg&s")
    embed.set_thumbnail(url="https://t4.ftcdn.net/jpg/05/62/26/83/360_F_562268305_PAhZKJquJnGun5zwCc1e2GjfXHG0sAGk.jpg")
    embed.add_field(name="<:zap:1127665844676206676> !join", value="Summon Prometheus, the celestial companion, and traverse the divine halls of Olympus together.", inline=False)
    embed.add_field(name="<:trident:1127934014712459344> !leave", value="Release your connection to Prometheus, the titan of enlightenment, as you step back into the mortal world.", inline=False)
    embed.add_field(name="<:ping_pong:1127934014712459344> !ping", value="Challenge your opponent to a mythical game of ping-pong, where lightning-fast reflexes reign supreme.", inline=False)
    embed.add_field(name="", value="\u200b")
    embed.set_footer(text="Immortality is not the absence of death, but rather the eternal presence of one's deeds and legacy.")
    await ctx.send(embed=embed)

client.run(TOKEN)
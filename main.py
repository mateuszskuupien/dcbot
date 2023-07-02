import discord
import asyncio
from discord.ext import commands, tasks
import os
from dotenv import load_dotenv
import youtube_dl

load_dotenv()
DISCORD_TOKEN = os.getenv('MTEyNTAwNDM3MzY3MjU5MTQzMA.GN4gpi.vSVjZgXh8KMx67n8EDE6u2HadNM45MmAJ5gnrc')

intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source,volume)
        self.data = data
        self.title = data.get('title')
        self.url = ''

    @classmethod
    async def from_url(cls, url, *, loop = None, stream = False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            data = data['entries'][0]
        filename = data['title'] if stream else ytdl.prepare_filename(data)
        return filename

    @bot.command(name='join')
    async def join(self,ctx):
        if not ctx.message.author.voice:
            await ctx.send('{} is not connected to a voice channel'.format(ctx.message.author.name))
            return 
        else:
            channel = ctx.message.author.voice.channel
            await channel.connect()

    @bot.command(name='play')
    async def play(self,ctx,url):
        server = ctx.message.guild
        voice_channel = server.voice_client
        async with ctx.typing():
            filename = await YTDLSource.from_url(url, loop=bot.loop)
            voice_channel.play(discord.FFmpegPCMAudio(executable='C:\\Users\\mateu\\OneDrive\\Pulpit\\discordbot\\ffmpeg-2023-06-27-git-9b6d191a66-full_build\\bin', source=filename))
        await ctx.send('**Now Playing:** {}'.format(filename))

    @bot.command(name='pause')
    async def pause(self,ctx):
        voice_client = ctx.message.guild.voice_client
        if voice_client.is_playing():
            await voice_client.pause()
        else:
            await ctx.send('The bot is paused')

    @bot.command(name='resume')
    async def resume(self,ctx):
        voice_client = ctx.message.guild.voice_client
        if voice_client.is_paused():
            await voice_client.resume()
        else:
            await ctx.send('The bot is already playing')
    @bot.command(name='leave')
    async def leave(self,ctx):
        voice_client = ctx.message.guild.voice_client
        if voice_client.is_connected():
            await voice_client.disconnect()
        else:
            await ctx.send('Bot has not joined to a voice channel')

    @bot.command(name='stop')
    async def stop(self,ctx):
        voice_client = ctx.message.guild.voice_client
        if voice_client.is_playing():
            await voice_client.stop()
        else:
            await ctx.message('The bot is not playing any music')

    if __name__ == '__main__':
        bot.run('MTEyNTAwNDM3MzY3MjU5MTQzMA.GN4gpi.vSVjZgXh8KMx67n8EDE6u2HadNM45MmAJ5gnrc')
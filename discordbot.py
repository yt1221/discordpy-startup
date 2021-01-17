import os
import discord
from discord.ext import commands

#client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']
bot = commands.Bot(command_prefix='!')
muteList = []
channel_mem = []

@bot.event
async def on_ready():
    global muteList
    global channel_mem

    print('-----Logged in info-----')
    print(bot.user.name)
    print(bot.user.id)
    print(discord.__version__)
    print('------------------------')
    muteList = []
    channel_mem = []

@bot.command()
async def voicekickall(ctx):
    state = ctx.author.voice

    for member in state.channel.members:

        await member.move_to(None)

@bot.command()
async def vka(ctx):
    state = ctx.author.voice

    for member in state.channel.members:

        await member.move_to(None)

@bot.command()
async def voicekickmention(ctx):
    mentions = ctx.message.mentions

    for member in mentions:

        await member.move_to(None)

@bot.command()
async def vkm(ctx):
    mentions = ctx.message.mentions

    for member in mentions:

        await member.move_to(None)

@bot.command()
async def muteadd(ctx):
    global muteList
    global channel_mem

    muteList = ctx.message.mentions
    channel_mem = [i.id for i in muteList]

@bot.command()
async def mutereset(ctx):
    global muteList
    global channel_mem

    muteList = []
    channel_mem = []


@bot.event
async def on_voice_state_update(member,before,after):
    global muteList
    global channel_mem

    if len(channel_mem) == 0:
        return

    if member.id in channel_mem:

        if not after.mute:
            for member in muteList:

                await member.edit(mute=True)

bot.run(TOKEN)

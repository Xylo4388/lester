import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from discord.ext.commands import CommandError
from discord.ext.commands import Bot, has_permissions, CheckFailure
from discord.utils import get
import sys
import os
import base64
import time
import json
import requests
from collections.abc import Sequence
from discord import Client
import DiscordUtils
from dotenv import load_dotenv

load_dotenv()


bot = commands.Bot(command_prefix=["!"], help_command=None)

async def is_owner(ctx):
    return ctx.author.id == 569334038326804490
    return ctx.author.id == 241062161059676161

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("with Females."))

@bot.command()
async def dm(ctx):
    await ctx.channel.send("Creating dm with {name}".format(name=ctx.author.name))
    print("Started direct message")
    channel = await ctx.author.create_dm()
    print(channel)
    print(ctx.author)
    await channel.send("heyy")
    await channel.send("are you a female")

@bot.command()
async def roast(ctx):
    response = requests.get('https://insult.mattbas.org/api/insult.txt')
    await ctx.channel.send(response.text)

@bot.command()
async def compliment(ctx):
    response = requests.get('https://complimentr.com/api')
    text = json.loads(response.text)
    await ctx.channel.send(text['compliment'])


@bot.command()
async def help(ctx):
    print("sending help message to", (ctx.author.name))
    embed1=discord.Embed(title="Help Page 1", description='Use the prefix "!" to use them!')
    embed1.set_author(name="Version: v1.0.2", url="https://github.com/Xylo4388")
    embed1.add_field(name="!help", value="Shows this list of commands.", inline=False)
    embed1.add_field(name="!dm", value="Creates a dm with ~ Yours truly. Lester", inline=False)
    embed1.add_field(name="!yt or !youtube", value="Sends a link to the Authors YouTube Channel.", inline=False)
    embed1.add_field(name="!support", value="Gives you a link to our Discord server for support.", inline=False)
    embed1.add_field(name="!daddy", value="You'll see :stuck_out_tongue_winking_eye:", inline=False)
    embed1.add_field(name="!roast", value="Roasts you.", inline=False)
    embed1.add_field(name="!compliment", value="Compliments you.", inline=False)

    embed2=discord.Embed(title="Help Page 2", description='Use the prefix "!" to use them!')
    embed2.set_author(name="Version: v1.0.0", url="https://github.com/Xylo4388")
    embed2.add_field(name="!github", value="Gives the link to the authors GitHub", inline=False)
    embed2.add_field(name="!shut", value="Turns me off :wink:", inline=False)
    embed2.add_field(name="!restart", value="Will turn you on.", inline=False)
    embed2.add_field(name="!cook", value="I am at your service, m'lady.", inline=False)
    embed2.add_field(name="!stats", value="Will check YouTube stats (CURRENTLY BROKEN)", inline=False)


    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx)
    paginator.add_reaction('⬅', "back")
    paginator.add_reaction('➡', "next")
    paginator.remove_reactions = True
    embeds = [embed1, embed2]
    await paginator.run(embeds)

@bot.command(aliases=['yt', 'youtube'])
async def youtoob(ctx):
    print("sending YouTube link to", (ctx.author.name))
    embed=discord.Embed(title="Authors YouTube Channel", description="https://youtube.com/igni4w")
    await ctx.channel.send(embed=embed)

@bot.command()
async def daddy(ctx):
    print("Sending Daddy message to", (ctx.author.name))
    await ctx.channel.send("Yes m'lady?")

@bot.command()
async def support(ctx):
    embed=discord.Embed(title="If you need any support, Join our Discord Server", description='https://discord.gg/zJC3twSBHy')
    await ctx.channel.send(embed=embed)

@bot.command()
async def github(ctx):
    await ctx.channel.send("Here is the Authors GitHub profile:")
    await ctx.channel.send("https://github.com/Xylo4388")

@bot.command(aliases=['stop', 'shutdown'])
@commands.check(is_owner)
async def shut(ctx):
    await ctx.channel.send("Shutting myself down, cus im not horny like you teenagers.")
    await ctx.bot.logout()

@bot.command()
@commands.check(is_owner)
async def restart(ctx):
    await ctx.channel.send("My people need me. I will be back in a short period of time.")
    os.execv(sys.executable, ['python'] + sys.argv)

@bot.command()
async def cook(ctx):
    await ctx.channel.send("""
    Hello m'lady. *Tips Fedora*
Would you like cookies or cake?
    """)

@bot.event
async def on_message(ctx):
    if ctx.author.id != bot.user.id:
        if not ctx.guild:
            if "yes" in ctx.content.lower():
                epic = """
    Good good. My name is Lester. I am a professional redditor with over
    twenty years of experience. I was wondering if you would like to spend
    some time with me together. I would really appreciate it!! Btw, if you're
    curious, it's 6 inches long ;) Have a wonderful evening m'lady! *Tips Fedora*
                """
                e = discord.Embed(title="If you're interested in my \"resume\" click here! ~",
                          url="https://bit.ly/lesterbot",
                          description="Thank you for reading! ^-^")
                await ctx.channel.send(epic)
                await ctx.channel.send(embed=e)
            if "no" in ctx.content.lower():
                notepic = """
                Do you mind fucking off for me? thanks!
                """
                await ctx.channel.send(notepic)
            if "no u" in ctx.content.lower():
                nou = """
                Fuck you
                """
                await ctx.channel.send(nou)
            if "cum for me" in ctx.content.lower():
                cum = """
                *cums cutely*
                """
                await ctx.channel.send(cum)
            if "cum" in ctx.content.lower():
                sex = """
                *sex*
                """
                await ctx.channel.send(sex)
            if "sex" in ctx.content.lower():
                uwu = """
                *cum*
                """
                await ctx.channel.send(uwu)
        else:
            if "cookies" in ctx.content.lower():
                cookies = """
                *gives cookies*
                """
                await ctx.channel.send(cookies)
            if "virus" in ctx.content.lower():
                virus = """
                safe halal download ﷽ click free safe virus approved बहुत सुरक्षित और अच्छा
                http://www.5z8.info/peepshow_rctw
                """
                await ctx.channel.send(virus)
            if "cake" in ctx.content.lower():
                cake = """
                *gives cake*
                """
                await ctx.channel.send(cake)

    await bot.process_commands(ctx)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.channel.send(":sob: If you believe this command should be added, Join our Support Server, https://discord.gg/zJC3twSBHy")
    elif isinstance(error, CheckFailure):
        await ctx.channel.send("Oh, so you're a badlion client user? Sorry, but your opinion is irrelevant.")
    else:
        print("An unhandled error has occured.")
        await ctx.channel.send(":flushed: Looks like <@569334038326804490> f*cked up something again. Pls spam his DMs so he fixes it!!")
        await ctx.channel.send("```{error}```".format(error=error))

bot.run(os.getenv('TOKEN'))

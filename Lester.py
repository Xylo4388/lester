import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from discord.ext.commands import CommandError
from discord.ext.commands import Bot, has_permissions, CheckFailure
from discord.utils import get
from discord import Client, Intents, Embed
from discord_slash import SlashCommand, SlashContext
import sys
import os
import base64 
import time
import json
import requests
import re
from collections.abc import Sequence
from discord import Client
import DiscordUtils
from dotenv import load_dotenv
import random

<<<<<<< HEAD
load_dotenv()
#
# def get_prefix(client,message):
#     with open("prefixes.json", "r") as f:
#         prefixes = json.load(f)
#
#     return prefix[str(message.guild.id)]
=======
load_dotenv() 
>>>>>>> 5c919bf6c785c936a66a571101db6d515bec16d3

bot = commands.Bot(command_prefix=["l.", "L."], help_command=None)
slash = SlashCommand(bot)

# @bot.event
# async def on_guild_join(guild):
#     with open("prefixes.json", "r") as f:
#         prefixes = json.load(f)
#
#     prefixes[str(guild.id)] = ["l.", "L."]
#
#     with open("prefixes.json", "w") as f:
#         json.dump(prefixes,f)

async def is_owner(ctx):
    return ctx.author.id == 569334038326804490
    return ctx.author.id == 241062161059676161

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name="Dm me the word 'tomato'"))

@bot.command()
async def help(ctx):
    print("sending help message to", (ctx.author.name))

    embed1=discord.Embed(title="Help Page 1", description='Use the prefix "l." to use them!')
    embed1.set_author(name="Version: v1.0.3", url="https://github.com/Xylo4388")
    embed1.add_field(name="l.help", value="Shows this list of commands.", inline=False)
    embed1.add_field(name="l.dm", value="Creates a dm with ~ Yours truly. Lester", inline=False)
    embed1.add_field(name="l.yt or !youtube", value="Sends a link to the Authors YouTube Channel.", inline=False)
    embed1.add_field(name="l.support", value="Gives you a link to our Discord server for support.", inline=False)
    embed1.add_field(name="l.daddy", value="You'll see :stuck_out_tongue_winking_eye:", inline=False)
    embed1.add_field(name="l.roast", value="Roasts you.", inline=False)
    embed1.add_field(name="l.compliment", value="Compliments you.", inline=False)

    embed2=discord.Embed(title="Help Page 2", description='Use the prefix "l." to use them!')
    embed2.set_author(name="Version: v1.0.3", url="https://github.com/Xylo4388")
    embed2.add_field(name="l.github", value="Gives the link to the authors GitHub", inline=False)
    embed2.add_field(name="l.shut", value="Turns me off :wink:", inline=False)
    embed2.add_field(name="l.restart", value="Will turn you on.", inline=False)
    embed2.add_field(name="l.cook", value="I am at your service, m'lady.", inline=False)
    embed2.add_field(name="l.stats", value="Will check YouTube stats (CURRENTLY BROKEN)", inline=False)
    embed2.add_field(name="l.sus", value="Sends a suspicious message :wink:", inline=False)

    embed3=discord.Embed(title="Help Page 3", description='Use the prefix "l." to use them!')
    embed3.set_author(name="Version: v1.0.3", url="https://github.com/Xylo4388")
    embed3.add_field(name="l.scan (link)", value="(Coming in v1.0.4)", inline=False)
    embed3.add_field(name="l.info {User ID}", value="Will tell you when a member joined your server", inline=False)

    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx)
    paginator.add_reaction('⬅', "back")
    paginator.add_reaction('➡', "next")
    paginator.remove_reactions = True
    embeds = [embed1, embed2, embed3]
    await paginator.run(embeds)

#
# @bot.command()
# @commands.has_permissions(administrator = True)
# async def prefix(ctx, prefix):
#     with open("prefixes.json", "r") as f:
#         prefixes = json.load(f)
#
#     prefix[str(guild.id)] = prefix
#
#     with open("prefixes.json", "w") as f:
#         json.dump(prefixes,f)

@bot.event
async def on_message(ctx, msg):
    if msg.mentions[0] == 816151000673943613:
        await ctx.channel.send("My prefix is l.")

@bot.command()
async def dm(ctx):
    await ctx.channel.send("Creating dm with {name}".format(name=ctx.author.name))
    print("Started direct message")
    channel = await ctx.author.create_dm()
    print(channel)
    print(ctx.author)
    await channel.send("heyy")
    await channel.send("are you a female")

# @bot.command()
# async def scan(ctx, arg):
#     s = re.search("(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)", arg)
#     pattern = ''
#     test_string = ''
#     m = re.match(pattern, test_string)
#     if m:
#         await ctx.send("Scanning {}".format(arg))

# @bot.event()
# async def on_message(ctx, arg):
#     s = re.search("(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)", arg)
#     pattern = ''
#     test_string = ''
#     m = re.match(pattern, test_string)
#     if m:
#         await ctx.send("Scanning {}".format(arg))

@bot.command()
async def info(ctx, *, member: discord.Member):
    fmt = '{0} joined {0.guild.name} on {0.joined_at} and has {1} role(s).'
    await ctx.send(fmt.format(member, len(member.roles)-1))

@info.error
async def info_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('This member is not in this server. Please mention an actual member!')

@bot.command()
async def sus(ctx):
    if ctx.author.id != bot.user.id:
        copypasta2 = ("Did someone say sus 😱😱😱 HOLY FUCKING SHIT‼️‼️‼️‼️ IS THAT A MOTHERFUCKING AMONG US REFERENCE??????!!!!!!!!!!11!1!1!1!1!1!1! 😱😱😱😱😱😱😱 AMONG US IS THE BEST FUCKING GAME 🔥🔥🔥🔥💯💯💯💯 RED IS SO SUSSSSS 🕵️🕵️🕵️🕵️🕵️🕵️🕵️🟥🟥🟥🟥🟥 COME TO MEDBAY AND WATCH ME SCAN 🏥🏥🏥🏥🏥🏥🏥🏥 🏥🏥🏥🏥 WHY IS NO ONE FIXING O2 🤬😡🤬😡🤬😡🤬🤬😡🤬🤬😡 OH YOUR CREWMATE? NAME EVERY TASK 🔫😠🔫😠🔫😠🔫😠🔫😠 Where Any sus!❓ ❓ Where!❓ ❓ Where! Any sus!❓ Where! ❓ Any sus!❓ ❓ Any sus! ❓ ❓ ❓ ❓ Where!Where!Where! Any sus!Where!Any sus Where!❓ Where! ❓ Where!Any sus❓ ❓ Any sus! ❓ ❓ ❓ ❓ ❓ ❓ Where! ❓ Where! ❓ Any sus!❓ ❓ ❓ ❓ Any sus! ❓ ❓ Where!❓ Any sus! ❓ ❓ Where!❓ ❓ Where! ❓ Where!Where! ❓ ❓ ❓ ❓ ❓ ❓ ❓ Any sus!❓ ❓ ❓ Any sus!❓ ❓ ❓ ❓ Where! ❓ Where! Where!Any sus!Where! Where! ❓ ❓ ❓ ❓ ❓ ❓ I think it was purple!👀👀👀👀👀👀👀👀👀👀It wasnt me I was in vents!!!!!!!!!!!!!!😂🤣😂🤣😂🤣😂😂😂🤣🤣🤣😂😂😂")
        copypasta1 = ("Oh my fucking god guys I am fucking fuming. So the other day at work my boss told us that he recently discovered the video game Among Us, and ever since, his behaviour has become rather concerning. He now refers to me and my coworkers as 'crewmates'. Last Wednesday, when he noticed my teenage colleague slacking off at his workstation, he yelled at him saying he was 'faking his tasks' and is 'acting sus'. I confronted my boss telling him that his behaviour lately has been egregious and immature, and he proceeded to call me an idiot and yelled kicked! The next day I caught him dancing around in his office blasting among drip from his desktop at full volume. I entered his office to kindly ask him to turn off the music since it was distracting to me and my coworkers. He looked at me angrily, telling me he has called an 'emergency meeting', instructing me to have a seat. I asked him what was the matter and he told me that I have been acting extremely 'sus'. He repeatedly yelled you're the impostor, telling me to say goodbye to my job because I have been ejected. I fucking lost my job and I dont know what to do. Please help me Reddit! I have nowhere else to turn.")
        copypasta3 = ("""
        So uh. If you're playing Among Us. On a voice call. And you're killed... why would you NOT immediately tell everyone who killed you? Isn't the goal to win if you're crew? Like if you're not gonna tell people on the voice call, why keep doing tasks? What's the point of using the voice comms at all? You're still in it when "dead". To me if a fucking person doesn't use it when they're dead they're throwing. I'd 100% tell my team who killed me if I was killed. The point is for the crew to find out who the impostor is. If you're part of the crew, you should be telling them if you know. If you're not going to do that, you're literally int'ing and throwing. So then why bother doing tasks if you don't want to win? End discussion.
        """)
        copypasta4 = ("""
        I am a concerned mother with a 13 year old child and I am here to seek help regarding my son. Last week when we went to the supermarket, my son pointed to a red trash can and started jumping around screaming “THAT’S AMONG US! THAT TRASH CAN IS SUS! RED IS THE IMPOSTOR!” As soon as he did that, the manager told us to leave. I told him that my son is just excited about something, and apologised. But the manager still told us to leave so I picked up the red trash can that my son was going crazy over and threw it on the managers head. Then my son shouted “DEAD BODY REPORTED.” Can someone please tell me what on earth is wrong with him?
        """)

        list = [copypasta1, copypasta2, copypasta3, copypasta4]
        randomlist = random.choice(list)
        await ctx.channel.send(randomlist)

@bot.command()
async def roast(ctx):
    response = requests.get('https://insult.mattbas.org/api/insult.txt')
    await ctx.channel.send(response.text)

@bot.command()
async def compliment(ctx):
    response = requests.get('https://complimentr.com/api')
    text = json.loads(response.text)
    await ctx.channel.send(text['compliment'])

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
                epic = """Good good. My name is Lester. I am a professional redditor with over
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
            if "tomato" in ctx.content.lower():
                tomato = """
                You have been infected
Now change your status to "Dm me the word "Tomato""
The infection shall spread silently

Only rule is to not spoil the game for others by telling people what
saying tomato does
                """
                await ctx.channel.send(tomato)
        else:
            if "cookies" in ctx.content.lower():
                cookies = """
                *gives cookies*
                """
                await ctx.channel.send(cookies)
            if "virus" in ctx.content.lower():
                virus = """safe halal download ﷽ click free safe virus approved बहुत सुरक्षित और अच्छा
<http://www.5z8.info/peepshow_rctw>
ओह माय चोदने वाले भगवान दोस्तों मैं चुदाई कर रहा हूँ। तो दूसरे दिन काम पर मेरे बॉस ने हमें बताया कि उन्होंने हाल ही में वीडियो गेम अमंग अस की खोज की, और तब से, उनका व्यवहार काफी चिंताजनक हो गया है। पिछले बुधवार को, जब उन्होंने मेरे किशोर सहकर्मी को अपने कार्यस्थल पर थप्पड़ मारते देखा, तो उन्होंने उस पर चिल्लाते हुए कहा कि वह "अपने कार्यों को धोखा दे रहा है" और "असहाय कर रहा है"। मैंने अपने बॉस से यह कहते हुए सामना किया कि उसका व्यवहार हाल ही में अहंकारी और अपरिपक्व रहा है, और उसने मुझे बेवकूफ कह और चललय "लत मर द!" अगल दन मन उस अपन करयलय म चर ओर नचत हए अपन डसकटप स ​​​​पर मतर म "डरप क बच" वसफट करत हए पकड। उसन गसस स मर तरफ दख, मझस कह क उसन एक "आपतकलन बठक" बलई ह, जसम मझ बठन क नरदश दय गय ह। मन उनस पछ क ममल कय ह और उनहन मझस कह क म बहद "सस" अभनय कर रह ह। वह बर-बर चललत थ "तम धखबज ह", मझ अपन नकर क अलवद कहन क लए कह रह थ कयक मझ "बदखल" कर दय गय थ। मन कमबखत अपन नकर ख द और मझ नह पत क कय करन ह। कपय मर मदद कर रडट! मर पस मडन क लए और कह नह ह।
                """
                await ctx.channel.send(virus)
            if "cake" in ctx.content.lower():
                cake = """
                *gives cake*
                """
                await ctx.channel.send(cake)
            # if "@Lester" in ctx.content.lower():
            #     prefix = """
            #     My prefix is l.
            #     """
            #     await ctx.channel.send(prefix)

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

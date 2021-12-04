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
from discord_components import DiscordComponents, Button, ButtonStyle

load_dotenv()

sus = """
:warning: **This link is Suspicious** :warning:
"""
notsus = """
:shield: **This link is Safe** :shield:
"""

bot = commands.Bot(command_prefix=["l.", "L."], help_command=None)
e = Client()
slash = SlashCommand(bot)
ddb = DiscordComponents(e)

async def is_owner(ctx):
    return ctx.author.id == 569334038326804490
    return ctx.author.id == 241062161059676161

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name="Dm me the word 'tomato'"))

@bot.command()
async def invite(ctx):
    await ctx.channel.send(
    "Invite me to your own server!!",
    components=[
    Button(style=ButtonStyle.URL, label="Invite me To your own server!", url="https://bit.ly/invitelester"),
    ],
    )
# @bot.event
# async def on_message(message):
#     response = await message.channel.send("discord.gg")
#     await message.delete()
#     await response.delete()


@bot.command()
async def help(ctx):
    print("sending help message to", (ctx.author.name))

    embed1=discord.Embed(title="Help Page 1", description='Use the prefix "l." to use them!')
    embed1.set_author(name="Version: v1.0.4", url="https://github.com/Xylo4388")
    embed1.add_field(name="l.help", value="Shows this list of commands.", inline=False)
    embed1.add_field(name="l.dm", value="Creates a dm with ~ Yours truly. Lester", inline=False)
    embed1.add_field(name="l.yt or l.youtube", value="Sends a link to the Authors YouTube Channel.", inline=False)
    embed1.add_field(name="l.support", value="Gives you a link to our Discord server for support.", inline=False)
    embed1.add_field(name="l.daddy", value="You'll see :stuck_out_tongue_winking_eye:", inline=False)
    embed1.add_field(name="l.roast", value="Roasts you.", inline=False)
    embed1.add_field(name="l.compliment", value="Compliments you.", inline=False)

    embed2=discord.Embed(title="Help Page 2", description='Use the prefix "l." to use them!')
    embed2.set_author(name="Version: v1.0.4", url="https://github.com/Xylo4388")
    embed2.add_field(name="l.github", value="Gives the link to the authors GitHub", inline=False)
    embed2.add_field(name="l.shut", value="Turns me off :wink:", inline=False)
    embed2.add_field(name="l.restart", value="Will turn you on.", inline=False)
    embed2.add_field(name="l.cook", value="I am at your service, m'lady.", inline=False)
    embed2.add_field(name="l.stats", value="Will check YouTube stats (Coming Soon)", inline=False)
    embed2.add_field(name="l.sus", value="Sends a suspicious message :wink:", inline=False)

    embed3=discord.Embed(title="Help Page 3", description='Use the prefix "l." to use them!')
    embed3.set_author(name="Version: v1.0.4", url="https://github.com/Xylo4388")
    embed3.add_field(name="l.scan (link)", value="Will scan a link to check if it's suspicious (Coming Soon)", inline=False)
    embed3.add_field(name="l.info {User ID}", value="Will tell you when a member joined your server", inline=False)
    embed3.add_field(name="l.mclive", value="Will update you about the most recent Minecraft Live", inline=False)
    embed3.add_field(name="l.yourmum", value="Will become your mum", inline=False)
    embed3.add_field(name="l.invite", value="Invite me to Your own Server!", inline=False)

    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx)
    paginator.add_reaction('⬅', "back")
    paginator.add_reaction('➡', "next")
    paginator.remove_reactions = True
    embeds = [embed1, embed2, embed3]
    await paginator.run(embeds)

@bot.event
async def on_message(message):
    if "suggestion:" in message.content.lower():
        emoji1 = '✅'
        emoji2 = '❌'
        await message.add_reaction(emoji1)
        await message.add_reaction(emoji2)

@bot.command()
@commands.cooldown(1,60,commands.BucketType.user)
async def dm(ctx, user: discord.User):
    if user:
        await ctx.channel.send("Creating dm with {name}".format(name=user.name))
        print("Started direct message")

        epicUser = await user.create_dm()
        await epicUser.send("heyy")
        await epicUser.send("are you a female")

    else:
        await ctx.channel.send("Creating dm with {name}".format(name=ctx.author.name))
        print("Started direct message")

        channel = await ctx.author.create_dm()
        await channel.send("heyy")
        await channel.send("are you a female")

@bot.command(aliases=['minecraftlive', 'MinecraftLive', 'mclive'])
async def mcl(ctx):
    print("sending Minecraft Live 2021 message to", (ctx.author.name))
    await ctx.channel.send("""
    Minecraft Live 2021 was about the 1.19 update!
The 1.19 update is going to be called the "Wild Update"!
In this update, they are going to be doing the following:
    **Adding Frogs**
    **Adding Boats with Chests**
    **Adding ways to get Renewable Clay**
    **Adding Mud Blocks**
    **Adding Fireflies**
    **Updating Swamps**
    **Adding The Deep Dark (The Warden and its Dungeon)**
    **Adding The Allay (Winner of the Mob Vote in Minecraft Live 2021)**
    **Adding Tadpoles**
    **Adding Bedrock Edition and Java Edition to the Xbox Game Pass**

More info can be found at:
https://www.minecraft.net/en-us/article/minecraft-live-2021-the-recap
    """)

@bot.command()
async def info(ctx, *, member: discord.Member):
    print("sending info message to", (ctx.author.name))
    fmt = '{0} joined {0.guild.name} on {0.joined_at} and has {1} role(s).'
    await ctx.send(fmt.format(member, len(member.roles)-1))

@bot.command()
async def sus(ctx):
    print("sending a suspicious message to", (ctx.author.name))
    if ctx.author.id != bot.user.id:
        copypasta1 = ("Did someone say sus 😱😱😱 HOLY FUCKING SHIT‼️‼️‼️‼️ IS THAT A MOTHERFUCKING AMONG US REFERENCE??????!!!!!!!!!!11!1!1!1!1!1!1! 😱😱😱😱😱😱😱 AMONG US IS THE BEST FUCKING GAME 🔥🔥🔥🔥💯💯💯💯 RED IS SO SUSSSSS 🕵️🕵️🕵️🕵️🕵️🕵️🕵️🟥🟥🟥🟥🟥 COME TO MEDBAY AND WATCH ME SCAN 🏥🏥🏥🏥🏥🏥🏥🏥 🏥🏥🏥🏥 WHY IS NO ONE FIXING O2 🤬😡🤬😡🤬😡🤬🤬😡🤬🤬😡 OH YOUR CREWMATE? NAME EVERY TASK 🔫😠🔫😠🔫😠🔫😠🔫😠 Where Any sus!❓ ❓ Where!❓ ❓ Where! Any sus!❓ Where! ❓ Any sus!❓ ❓ Any sus! ❓ ❓ ❓ ❓ Where!Where!Where! Any sus!Where!Any sus Where!❓ Where! ❓ Where!Any sus❓ ❓ Any sus! ❓ ❓ ❓ ❓ ❓ ❓ Where! ❓ Where! ❓ Any sus!❓ ❓ ❓ ❓ Any sus! ❓ ❓ Where!❓ Any sus! ❓ ❓ Where!❓ ❓ Where! ❓ Where!Where! ❓ ❓ ❓ ❓ ❓ ❓ ❓ Any sus!❓ ❓ ❓ Any sus!❓ ❓ ❓ ❓ Where! ❓ Where! Where!Any sus!Where! Where! ❓ ❓ ❓ ❓ ❓ ❓ I think it was purple!👀👀👀👀👀👀👀👀👀👀It wasnt me I was in vents!!!!!!!!!!!!!!😂🤣😂🤣😂🤣😂😂😂🤣🤣🤣😂😂😂")
        copypasta2 = ("Oh my fucking god guys I am fucking fuming. So the other day at work my boss told us that he recently discovered the video game Among Us, and ever since, his behaviour has become rather concerning. He now refers to me and my coworkers as 'crewmates'. Last Wednesday, when he noticed my teenage colleague slacking off at his workstation, he yelled at him saying he was 'faking his tasks' and is 'acting sus'. I confronted my boss telling him that his behaviour lately has been egregious and immature, and he proceeded to call me an idiot and yelled kicked! The next day I caught him dancing around in his office blasting among drip from his desktop at full volume. I entered his office to kindly ask him to turn off the music since it was distracting to me and my coworkers. He looked at me angrily, telling me he has called an 'emergency meeting', instructing me to have a seat. I asked him what was the matter and he told me that I have been acting extremely 'sus'. He repeatedly yelled you're the impostor, telling me to say goodbye to my job because I have been ejected. I fucking lost my job and I dont know what to do. Please help me Reddit! I have nowhere else to turn.")
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
async def yourmum(ctx):
    print("Becoming {name}'s Mum".format(name=ctx.author.name))
    await ctx.channel.send("""
    Please get off the computer now, you need to do the dishes. Or you're grounded.
    """)

@bot.command()
async def roast(ctx):
    print("Roasting", (ctx.author.name))
    response = requests.get('https://insult.mattbas.org/api/insult.txt')
    await ctx.channel.send(response.text)

@bot.command()
async def compliment(ctx):
    print("Complimenting", (ctx.author.name))
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
    print("sending support discord to", (ctx.author.name))
    await ctx.channel.send(
    "Join our Support Server!",
    components=[
    Button(style=ButtonStyle.URL, label="Join Here!", url="https://discord.gg/zJC3twSBHy"),
    ],
    )

@bot.command()
async def github(ctx):
    print("sending github link to", (ctx.author.name))
    await ctx.channel.send("Here is the Authors GitHub profile:")
    await ctx.channel.send("https://github.com/Xylo4388")

@bot.command(aliases=['stop', 'shutdown'])
@commands.check(is_owner)
async def shut(ctx):
    print("Stopping Lester thanks to", (ctx.author.name))
    await ctx.channel.send("Shutting myself down, cus im not horny like you teenagers.")
    await ctx.bot.logout()

@bot.command()
@commands.check(is_owner)
async def restart(ctx):
    print("Lester is now restarting thanks to", (ctx.author.name))
    await ctx.channel.send("My people need me. I will be back in a short period of time.")
    os.execv(sys.executable, ['python'] + sys.argv)

@bot.command()
async def cook(ctx):
    print("sending Cook message to", (ctx.author.name))
    await ctx.channel.send("""
    Hello m'lady. *Tips Fedora*
Would you like cookies or cake?
    """,
    components=[[
    Button(style=ButtonStyle.blue, label="Cookies"), Button(style=ButtonStyle.red, label="Cake"),
    ]],
    )
@bot.event
async def on_button_click(interaction):
    if interaction.component.label.startswith("Cookies"):
        await interaction.channel.send('*gives cookies*')
    if interaction.component.label.startswith("Cake"):
        await interaction.channel.send('*gives cake*')

# @bot.command()
# async def scan(ctx):
#     re.search("http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]")

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
            if "thankyou" in ctx.content.lower():
                thx = """
                You're Welcome!
                """
                await ctx.channel.send(thx)
            if "hate myself" in ctx.content.lower():
                response = requests.get('https://complimentr.com/api')
                text = json.loads(response.text)
                await ctx.channel.send(text['compliment'])
            if "i wanna die" in ctx.content.lower():
                dontdie = """
                Please don't end this, you have a much longer life to live. It will only get better from here. You can do this :hugging:
We all love you. If you need some help google "Help Hotlines".
You got this bro. :fist:
                """
                await ctx.channel.send(dontdie)

    await bot.process_commands(ctx)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.channel.send("""
        :sob: ``If you believe this command should be added, Join our Support Server``
        https://discord.gg/zJC3twSBHy
        """)
    elif isinstance(error, CheckFailure):
        await ctx.channel.send("Oh, so you're a badlion client user? Sorry, but your opinion is irrelevant.")
    else:
        print("An unhandled error has occured.")
        await ctx.channel.send("```{error}```".format(error=error))

bot.run(os.getenv('TOKEN'))

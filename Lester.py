from cProfile import label
import discord
from discord.ext import commands
import asyncio
from discord import app_commands
from dotenv import load_dotenv
import os
import google.generativeai as genai
from collections import defaultdict, deque
import json

load_dotenv()

TOKEN = os.environ["TOKEN"]
GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# Define bot with command prefix and intents
intents = discord.Intents.all()
intents.typing = False
intents.presences = False
intents.message_content = True
bot = commands.Bot(command_prefix="‎ ", intents=intents)

# Memory System
MEMORY_FILE = "memory.json"

# Load memory from JSON
if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r") as f:
        data = json.load(f)
        memory = defaultdict(lambda: deque(maxlen=50), {user: deque(messages, maxlen=50) for user, messages in data.get("messages", {}).items()})
        preferences = data.get("preferences", defaultdict(dict))
else:
    memory = defaultdict(lambda: deque(maxlen=50))
    preferences = defaultdict(dict)

# Save memory to JSON
def save_memory():
    with open(MEMORY_FILE, "w") as f:
        json.dump({
            "messages": {user: list(messages) for user, messages in memory.items()},
            "preferences": preferences
        }, f)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
        await bot.change_presence(
            status=discord.Status.online,
            activity=discord.Activity(
                type=discord.ActivityType.listening, name="/help | DM me for a chat!"
            ),
        )
    except Exception as e:
        print(f"Error syncing commands: {e}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if isinstance(message.channel, discord.DMChannel):
        user_id = str(message.author.id)
        memory[user_id].append(f"User: {message.content}")
        save_memory()

        conversation = "\n".join(memory[user_id])
        async with message.channel.typing():
            try:
                prompt = f"""
                You are Lester, a human with a laid-back personality. You don't take anything too seriously. You misspell words for fun, use sarcasm, and rarely apologize.
                Here are the user's preferences: {json.dumps(preferences.get(user_id, {}), indent=2)}
                
                This is the conversation so far:
                {conversation}
                
                Reply to the last user message: {message.content}
                """
                response = model.generate_content(prompt)
                memory[user_id].append(f"Lester: {response.text}")
                save_memory()
                await message.reply(response.text)
            except Exception as e:
                await message.reply("Bruh I kinda broke 💀")

    await bot.process_commands(message)

@bot.tree.command(name="help", description="Shows list of commands")
async def help(interaction: discord.Interaction):
    embed = discord.Embed(title="Help Page", description='Use / to use commands!')
    embed.set_author(name="Version: v1.0.4")
    embed.add_field(name="help", value="Shows this list of commands.", inline=False)
    embed.add_field(name="invite", value="Invite me to your server.", inline=False)
    embed.add_field(name="support", value="Join the support server.", inline=False)
    embed.add_field(name="favourite", value="Set user preferences.", inline=False)

    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="invite", description="Invite Lester to your server")
async def invite(interaction: discord.Interaction):
    await interaction.response.send_message("[Click here to invite me!](https://bit.ly/invitelester)")

@bot.tree.command(name="support", description="Join the support server")
async def support(interaction: discord.Interaction):
    await interaction.response.send_message("Join the support server: https://discord.gg/zJC3twSBHy")

@bot.tree.command(name="favourite", description="Set your favourites")
@app_commands.describe(topic="Set topic", value="user input for 'Topic'")
async def set_preference(interaction: discord.Interaction, topic: str, value: str):
    user_id = str(interaction.user.id)
    preferences[user_id][topic] = value
    save_memory()
    await interaction.response.send_message(f"Got it! I'll remember that your favourite {topic} is {value}.")

bot.run(TOKEN)

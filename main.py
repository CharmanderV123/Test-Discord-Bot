import discord, os

# Imports load_dotenv function from dotenv module

from dotenv import load_dotenv

# Retrieves the .env file thats in the same folder

load_dotenv()

# Obtains the Token for API

TOKEN = "MTE3NTk1NTkxNDc2MzgwNDczMw.Gzn32I.9AhO9Xx4ArV0ertu3Hcejwnd2OZJjA0tRnzVQo"

# print(TOKEN, "Token Value")

bot = discord.Client(intents=discord.Intents.default())

@bot.event

async def on_ready():

    guild_count = 0

    for guild in bot.guilds:

        print(f"- {guild.id} (name: {guild.name})")

        guild_count = guild_count + 1

    print("SampleBot is in " + str(guild_count) + " guilds.")

@bot.event

async def on_message(message):
    
    if message.content == "hello":

        await message.channel.send("hey dirtbag")

bot.run(TOKEN)
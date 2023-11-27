import discord, os

from random import randint

# Imports load_dotenv function from dotenv module

from dotenv import load_dotenv

# Retrieves the .env file thats in the same folder

load_dotenv()

# Obtains the Token for API

TOKEN = "MTE3NTk1NTkxNDc2MzgwNDczMw.Gzn32I.9AhO9Xx4ArV0ertu3Hcejwnd2OZJjA0tRnzVQo"

# print(TOKEN, "Token Value")

bot = discord.Client(intents=discord.Intents.all())

#List of Possible Greetings

content_list = ["hello","hi", "yo", "hey"]

#List of Possible Responses

response_list = ["Hello Friend", "Hi Friend", "Yolo Friend", "Hey Friend"]

@bot.event

async def on_ready():

    guild_count = 0

# Determines the number of Servers the Bot is in along with name and id

    for guild in bot.guilds:

        print(f"- {guild.id} (name: {guild.name})")

        guild_count = guild_count + 1

    print("SampleBot is in " + str(guild_count) + " guilds.")

@bot.event

# Retrieves message sent by users and if the content_list contains it a message from the response list will be randomly selected and used to respond

async def on_message(message):
    temp = randint(0,4)
    
    if message.content.lower() in content_list:

        await message.channel.send(response_list[temp])

bot.run(TOKEN)
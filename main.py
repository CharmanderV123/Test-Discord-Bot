import discord

bot = discord.Client()

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

bot.run("NzA0OTcwNzUyNzQyNjUzOTYz.Xqk5ww.1U_-WdW4aeGWCNF7bOJkLAu_2TM")
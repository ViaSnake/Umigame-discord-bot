import discord, os

client = discord.Client()

@client.event
async def on_message(message):
  if message.channel.name == "ウミガメのスープ":
    if message.content[-1] == "?" or message.content[-1] == "？":
      await message.add_reaction("⭕")
      await message.add_reaction("❌")
      await message.add_reaction("🤔")
      
    if message.content[0] == "!":
      if message.content[1:] == "help":
        await message.channel.send("ヘルプ")

client.run(os.environ["TOKEN"])
import discord, os

client = discord.Client()

@client.event
async def on_message(message):
  if message.channel.name == "ウミガメのスープ":
    if message.content[-1] == "?" or message.content[-1] == "？":
      await message.add_reaction("⭕")
      await message.add_reaction("❌")
      await message.add_reaction("🤔")
      
    if message.content[0] == "?":
      if message.content[1:] == "about":
        embed=discord.Embed(title="ウミガメのスープbotについて", description="メッセージの最後が「?」もしくは「？」である時に、リアクションで「⭕」「❌」「🤔」が付与されます。「⭕」はYESの意味。「❌」はNOの意味。「🤔」は分からない/関係ないの意味。ウミガメのスープの意味はggrks")
        await message.channel.send(embed=embed)

client.run(os.environ["TOKEN"])

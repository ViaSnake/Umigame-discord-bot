import discord, os

@bot.event
async def on_message(message):
  if message.channel.name == "ウミガメのスープ":
    if message.content.endswith("?") or message.content.endswith("？"):
      await message.add_reaction("⭕")
      await message.add_reaction("❌")
      await message.add_reaction("🤔")
    elif message.content.endswith("。"):
      await message.add_reaction("🆗")
      await message.add_reaction("🆖")
    elif message.content == "?about":
      embed=discord.Embed(title="ウミガメのスープbotについて", description="メッセージの最後が「?」もしくは「？」である時に、リアクションで「⭕」「❌」「🤔」が付与されます。「⭕」はYESの意味。「❌」はNOの意味。「🤔」は分からない/関係ないの意味。回答を行いたい場合は、文章の最後に「。」をつけることで「:ok:」「:ng:」がリアクションとして付与される。「:ok:」は正解の意味。「:ng:」は不正解の意味")
      await message.channel.send(embed=embed)

client.run(os.environ["TOKEN"])

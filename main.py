import discord, os

client = discord.Client()

@client.event
async def on_message(message):
  if message.channel.name == "ウミガメのスープ":
    if message.content.endswith("?") or message.content.endswith("？"):
      await message.add_reaction("⭕")
      await message.add_reaction("❌")
      await message.add_reaction("🤔")
    elif message.content.endswith("。"):
      await message.add_reaction("🆗")
      await message.add_reaction("🆖")
    
    if message.content == "?about":
      embed=discord.Embed(title="ウミガメのスープbotについて", description="")
      embed=embed.add_field(name="問題提示方法", value="メッセージが「?q」で始まる時に自動的に問題出ると認識されます。", inline=False)
      embed=embed.add_field(name="質問方法", value="メッセージが「?」もしくは「？」で終わる時に、自動的にリアクションで「⭕」「❌」「🤔」が付与されます。「⭕」はYESの意味。「❌」はNOの意味。「🤔」は分からない/関係ないの意味。", inline=False)
      embed=embed.add_field(name="回答方法", value="回答を行いたい場合は、文章の最後に「。」をつけることで「:ok:」「:ng:」がリアクションとして付与される。「:ok:」は正解の意味。「:ng:」は不正解の意味", inline=False)
      await message.channel.send(embed=embed)
      await message.delete()
    elif message.content.startswith("?q") :
      embed=discord.Embed(title="問題", description=message.content, color=0x00ff00)
      embed.set_author(name="{} が問題を作成".format(message.author))
      await message.channel.send(embed=embed)
      await message.delete()

@client.event
async def on_raw_message_delete(payload):
  channel = client.get_channel(752948742742868050)
  embed=discord.Embed(title="on_raw_message_delete", color=0xff0000, description="channel_id[{}]\nmessage_id[{}]\nguild_id[{}]".format(payload.channel_id, payload.message_id, payload.guild_id))
  await channel.send(embed=embed)

client.run(os.environ["TOKEN"])

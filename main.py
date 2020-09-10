import discord, os
from discord.ext import commands

bot = commands.Bot(command_prefix='?')
bot.remove_command('help')

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
  await bot.process_commands(message)

@bot.command()
async def help(ctx):
    embed=discord.Embed(title="ウミガメbot", description="?help - ヘルプ\n?about - 情報\n?q [question] - 問題出題")
    await ctx.send(embed=embed)
    await ctx.message.delete()

@bot.command()
async def about(ctx):
    embed=discord.Embed(title="ウミガメbot")
    embed=embed.add_field(name="問題出題方法", value="メッセージが「?q」で始まる時に自動的に問題と認識されます。\n例： `?q これは問題です。`", inline=False)
    embed=embed.add_field(name="質問方法", value="メッセージが「?」もしくは「？」で終わる時に、自動的にリアクションで「⭕」「❌」「🤔」が付与されます。\n「⭕」はYESの意味。「❌」はNOの意味。「🤔」は分からない/関係ないの意味。\n例：`これは質問です？` `This is question?`", inline=False)
    embed=embed.add_field(name="回答方法", value="回答を行いたい場合は、文章の最後に「。」をつけることで「:ok:」「:ng:」がリアクションとして付与される。「:ok:」は正解の意味。「:ng:」は不正解の意味", inline=False)
    await ctx.send(embed=embed)
    await ctx.message.delete()

@bot.command()
async def q(ctx, arg):
    embed=discord.Embed(title="問題", description=arg, color=0x00ff00)
    embed.set_author(name="{} が問題を作成".format(ctx.author))
    await ctx.send(embed=embed)
    await ctx.message.delete()
    
bot.run(os.environ["TOKEN"])

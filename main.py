import discord, os, uuid
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
  embed=discord.Embed(title="ウミガメbot")
  embed=embed.add_field(name="ヘルプ", value="`?help`", inline=True)
  embed=embed.add_field(name="説明", value="`?about`", inline=True)
  embed=embed.add_field(name="出題", value="`?q [question]`", inline=True)
  embed=embed.add_field(name="情報", value="`?info [channel/rythm]`", inline=True)
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
async def question(ctx, *, arg):

  async def create_text_channel(message, channel_name):
    category_id = message.channel.category_id
    category = message.guild.get_channel(category_id)
    new_channel = await category.create_text_channel(name=channel_name)
    return new_channel
  
  embed=discord.Embed(title="問題", description=arg, color=0x00ff00)
  embed.set_author(name="{} が問題を作成".format(ctx.author))
  await ctx.send(embed=embed)
  await ctx.message.delete()

  new_channel = await create_text_channel(ctx.message, channel_name=str(uuid.uuid4())[-6:])
  await ctx.send(f'{new_channel.mention} を作成しました')
  await ctx.message.delete()

@bot.command()
async def info(ctx, arg):
  if arg == "channel":
    embed=discord.Embed(title="チャンネル情報", description="このDiscordサーバーの各種チャンネルに関する説明です。追加したいチャンネルが有る場合は言ってくれ。気が向いたら追加する。Twitter、YouTubeに限らず割と何でも情報突っ込んだりできるぞ。")
    embed.add_field(name="テキストチャンネル", value="#チャット - チャットチャンネル\n#画像 - 画像のアップロード場所", inline=False)
    embed.add_field(name="情報チャンネル", value="#雀魂 - ゲーム「雀魂」に関する情報\n#シノアリス - ゲーム「シャドウバース」に関する情報\n#ファンタシースターオンライン２ - ゲーム「ファンタシースターオンライン２」に関する情報\n#ポケモンカード - ポケモンカードに関する情報\n*情報がいらないチャンネルはミュート推奨。作っておいてあれだけど、うるさい。", inline=False)
    embed.add_field(name="ボイスチャンネル", value="#AFK - 値落ちしても安心！放置していると移動させられるぞ\n#一般 - 喋りたい時に使ってどうぞ。", inline=False)
    await ctx.send(embed=embed)
    await ctx.message.delete()
  elif arg == "rythm":
    embed=discord.Embed(title="ボットの使い方", description="まずボットについて話す。ボットにも色々と種類があるが、全てを網羅するのは不可能。この世のボットの真理について知りたいやつはWikipediaでも見てこい。（https://ja.wikipedia.org/wiki/Bot ） このサーバーに導入されているボットの種類は、音楽ボット１・音楽ボット２・音楽ボット３だ。豊富な種類を取り揃えているぞ。要望があればいくらでも音楽ボットを取り揃えるぞ。遠慮なく言ってくれ。\n\nじゃあ使い方に移るぞ。 基本的な使い方は[記号]play [URL]だ。\n[記号]に代入される記号は! > * の３種類 [URL]に代入可能なURLはYouTube SoundCloud Twitch Vimeo Mixer だ。各種サービスについてはこのメッセージの下を確認してくれ。\n\nこれらの情報を代入した場合の例を次に示すぞ。 !play https://www.youtube.com/watch?v=UzRVEQDxiOo !は @Rythm >は @Rythm 2 は @Rythm Canary に紐付いているぞ。例の場合は最初の!playの!部分を該当する記号に置き換えろください。\n\nちなみにここまで読んでもらって申し訳ないが、前提を話すのを忘れていた。 ボイスチャンネルに接続している必要がある。あとこれらのコマンドを記述するテキストチャンネルは #ボットコマンド を使ってくれ。 ボットは次々にメッセージを送信してくる場合があって他の人の迷惑になるかもしれない、だからマナーとしてよろしく頼むぞ。 もしもうるさい場合は #ボットコマンド チャンネルをミュートしてくれ。これは最低限自分で取り組むべき努力だ。この努力を怠る奴にこの雀荘への立ち入り許可は下りない。\n\nちなみに他にも色々コマンドがあるのだが、主に必要とされるコマンドについてまとめておくぞ。 `[記号]loop` `[記号]skip` アメリカ語つよつよの君なら単語見て分かるよな？loopは延々と繰り返して、skipは曲のスキップだ。\n\nちなみにこのボットはキューシステムというのを採用しているぞ。 キューってのはつまりは、順番だ。再生したい曲をプレイリストにぶん投げていって、一番古くぶん投げられた曲を再生するっていう仕組みだ。便利だろ？ あと再生リストにも対応している。色々他にも機能はある、色々試してみてくれ。\n\nちなみに`[記号]help` でコマンドとか使い方が確認できる。全部アメリカ語だから自分で翻訳するなりしてくれ。")
    embed.add_field(name="YouTube", value="||YouTubeは知ってるよな？tを小文字にするやつは滅べ。 https://www.youtube.com/||", inline=True)
    embed.add_field(name="SoundCloud", value="||も ち ろ ん SoundCloudも知ってるよな？え？知らない？じゃあこの機会に知っていけ。めっちゃ便利だぞ https://soundcloud.com/||", inline=True)
    embed.add_field(name="Twitch", value="||天下のAmazon様のお通りだ！Amazon傘下のストリーミングサービス。YouTubeのゲームライブ特化版だと思っていいぞ。ここまで知ったんだついでに俺のチャンネルをフォローしていけ。 https://www.twitch.tv/||", inline=True)
    embed.add_field(name="Viemo", value="||稀に良く聞く名前だから知ってるよな。ちなみに俺は知らん。動画共有サービスだ。YouTube劣化版だ。これをつぶやくとアンチっていうファンがつくぞ！！ https://vimeo.com/||", inline=True)
    embed.add_field(name="Mixer", value="||昔Beamっていう名前だったサービスだ。Microsoftに買収されてMixerになったぞ！Amazonに負けまいと買収したけど、2020年に終了したぞ！俺のチャンネルもあるけど使いにくい・人こない・つまらないの三拍子が揃っていたから無視しとけ！ https://mixer.com/ ちなみにサービス終了後はFaceBook Gamingに買収されたぞ。使いにくさは改善されなかったから知る必要はないぞ。||", inline=True)
    embed.add_field(name="補足", value="||優しいから全ての情報を書いてあげたが、記憶で書いてるから情報の正確性については1ミリも保証しないからよろしく。他の情報についてはggrks。||", inline=True)
    await ctx.send(embed=embed)
    await ctx.message.delete()
  else:
    await ctx.message.delete()
    
bot.run(os.environ["TOKEN"])

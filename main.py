import discord
import twitter

import os
from dotenv import load_dotenv

load_dotenv()


#TwitterAPIKey
Consumer_Key=os.environ['CONSUMER_KEY']
Consumer_Secret=os.environ['CONSUMER_SECRET']
AccessToken=os.environ['ACCESSTOKEN']
AccessTokenSecret=os.environ['ACCESSTOKENSECRET']


#DiscordBot Tokenを入れる
TOKEN = os.environ['TOKEN']

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動したらインタプリタにログイン通知が表示される
@client.event
async def on_ready():
    print('ログインしました')
    print('Discord-Twitter-PostBotを起動します。')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):

    CommandTrigger="/tw"
    Twitter=140

    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    
    if message.content == '/neko':
        await message.channel.send('にゃーん')

    if message.content.startswith(CommandTrigger):
        #取得したキーとアクセストークンを設定する。
        Oauth = twitter.OAuth(AccessToken,AccessTokenSecret,Consumer_Key,Consumer_Secret)
        twi = twitter.Twitter(auth=Oauth)

        #コマンドは投稿しない、ディスコードネームに置換する
        message.content=message.content.replace(CommandTrigger,message.author.name+":")

    #140文字以下か判定する
        if len(message.content) <= Twitter:
            #Twitterに投稿
            twi.statuses.update(status=message.content)
        else:
            mes="Twitterへの投稿に失敗しました、文字数を減らしてください。"
            await message.channel.send(mes)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
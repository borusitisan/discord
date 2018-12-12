import discord 

client = discord.Client()

# 起動時に通知してくれる処理
@client.event
async def on_ready():
    print('ログインしました')

# 「/neko」と発言したら「にゃーん」が返る処理
@client.event
async def on_message(message):
    if message.content.startswith('/neko'):
        reply = 'にゃーん'
        await client.send_message(message.channel, reply)

client.run('NTE3ODgzMjk4NjI2OTI4NjQx.DuIsFw.3zL3UJVPKhxOaoS7HKipbLyHYto')
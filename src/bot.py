# bot.py
import datetime
from time import sleep
import discord

DISCORD_TOKEN = 'MTE3MzU2MDg2NTE4MjcxNTk1NQ.GLZCfu.wlDKpTpF-ZFUKFN_hYxm49sQgXdrLvEm7dLaek' # don't tell me nothing bout security god dammit
DISCORD_GUILD = 'Server von Horst Konrader'
DISCORD_CHANNEL = 1173563257466920963

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == DISCORD_GUILD:
            break

    while(1):
        current_time = datetime.datetime.now()
        if current_time.hour == 9 and current_time.minute == 11:
            channel = client.get_channel(DISCORD_CHANNEL)
            with open('src\911.gif', 'rb') as f:
                gif = discord.File(f)
                await channel.send(file=gif)
                print(f'message sent')
            sleep(5)

client.run(DISCORD_TOKEN)

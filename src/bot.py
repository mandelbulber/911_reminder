# bot.py
from asyncio import sleep
import datetime
import discord

DISCORD_TOKEN = 'MTE3MzU2MDg2NTE4MjcxNTk1NQ.GLZCfu.wlDKpTpF-ZFUKFN_hYxm49sQgXdrLvEm7dLaek' # don't tell me nothing bout security god dammit
DISCORD_GUILD = 'Server von Horst Konrader'

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
        if current_time.second == 10:
        #if current_time.hour == 9 and current_time.minute == 11:
            # post a message in a channel
            channel = client.get_channel(1173563257466920963)
            await channel.send('9.11')
            sleep(5)
            print(f'message sent')

client.run(DISCORD_TOKEN)

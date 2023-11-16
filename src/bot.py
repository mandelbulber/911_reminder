import datetime
from time import sleep
import discord

DISCORD_TOKEN = 'MTE3NDcyMDE4MDA0ODM3NTg0OA.GP-HTe.PcijwPixLfj5mTsANN-v_KrWicP_Ngq8mLuh8I' # don't tell me nothing bout security god dammit
DISCORD_GUILD = 'Konis Discord'
DISCORD_CHANNEL = 982685695233630299

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
            with open('/home/dev/911_reminder/911.gif', 'rb') as f:
                gif = discord.File(f)
                await channel.send(file=gif)
                print(f'message sent')
            sleep(500)

client.run(DISCORD_TOKEN)

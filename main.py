import nextcord
import os
from nextcord.ext import commands, tasks, application_checks
import asyncio
import time

guildidserver =  # Change this to the server id
userid =  # Set to your UserID
tokenrunprogram = "" # Set this to the token
intents = nextcord.Intents.default()
intents.presences = True
bot = commands.Bot(intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=nextcord.Game(name="Pinging someone"))
    os.system('clear')
    print(f'Signed into {bot.user}')

@bot.slash_command(description="NO STOP THIS WILL MAKE YOU GO CRAZY!", guild_ids=[guildidserver])
async def spam(interaction: nextcord.Interaction):
    for index in range(999999999999999999):
        await interaction.send(f"<@{userid}>")
        time.sleep(0.3)

bot.run(f'{tokenrunprogram}')
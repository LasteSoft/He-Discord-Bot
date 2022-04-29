
import asyncio

import discord
from discord.ext import commands

from ujson import load


with open("secret_file.json") as f:
    secret_file = load(f)

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or(["he!","he.","He!","hE.","He.","hE!"]),
    activity=discord.Game(name=f"起動準備"),
    status=discord.Status.dnd,
    intents=discord.Intents.all(),
    help_command=None,
)
bot.secret_file = secret_file

@bot.listen()
async def setup_hook():
    await bot.load_extension("jishaku")

@bot.listen()
async def on_ready():
    await bot.change_presence(ctivity=discord.Game(name="Test"))

async def main():
    await bot.start(bot.secret_file["TOKEN"])

asyncio.run(main())

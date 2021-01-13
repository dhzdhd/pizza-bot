import os

from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
INTENTS = Intents.all()


def _init_bot():
    bot = commands.Bot(command_prefix='.', intents=INTENTS)
    bot.run(BOT_TOKEN)


if __name__ == '__main__':
    _init_bot()

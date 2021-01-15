import asyncpg
import logging
import os

from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
POSTGRE_HOST = os.getenv("POSTGRE_HOST")
POSTGRE_PASSWORD = os.getenv("POSTGRE_PASSWORD")
POSTGRE_DSN = os.getenv("POSTGRE_DSN")
POSTGRE_USER = os.getenv("POSTGRE_USER")
POSTGRE_PORT = os.getenv("POSTGRE_PORT")
POSTGRE_DATABASE = os.getenv("POSTGRE_DATABASE")
INTENTS = Intents.all()


class Logger(object):
    def __init__(self, command):
        self.command = command

    def __call__(self, *args, **kwargs):
        logging.info()
        return self.command(*args, **kwargs)


async def asyncpg_pool():
    """ A database connection pool for creating db connections with ease (PostGRE) """
    pool = await asyncpg.create_pool(
        host=POSTGRE_HOST,
        password=POSTGRE_PASSWORD,
        dsn=POSTGRE_DSN,
        user=POSTGRE_USER,
        port=POSTGRE_PORT,
        database=POSTGRE_DATABASE
    )
    return pool


def _init_bot() -> None:
    bot = commands.Bot(command_prefix='.', intents=INTENTS)
    bot.run(BOT_TOKEN)
    bot.add_cog("cogs.events")


if __name__ == '__main__':
    _init_bot()

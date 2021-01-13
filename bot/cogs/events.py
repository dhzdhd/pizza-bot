from discord.ext.commands import Cog
from discord import Member


class Events(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @Cog.listener()
    async def on_ready(self) -> None:
        ...
        
    @Cog.listener()
    async def on_message(self, message: str) -> None:
        if isinstance(message, Member):
            if message.content = self.bot.user:
                await message.channel.send("Hello")


def setup(bot):
    bot.add_cog(Events(bot))
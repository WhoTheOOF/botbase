import discord
from discord.ext import commands

class BotBase(commands.AutoShardedBot):
    def __init__(self, **kwargs):
        intents = discord.Intents.all()
        super().__init__(
            command_prefix=["bb!", "bot!", "wtv"],
            max_messages=5000, # this limits how many messages your bot can store in its cache
            intents=intents,
            chunk_guilds_at_startup=False
            **kwargs,
            )

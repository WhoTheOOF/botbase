import discord, traceback, asyncpg, aiohttp, os
from discord.ext import commands

import util.config as config

# You will need the 'message_content' intent for using this setup, unless you want to add slash command support.

class BotBase(commands.AutoShardedBot):
    def __init__(self, **kwargs):
        intents = discord.Intents.all() # no need to define the 'message_content' intent since we called .all()
        super().__init__(
            command_prefix=["bb!", "bot!", "wtv"], # we defined multiple prefixes here, i don't know why but it just makes sense.
            max_messages=5000, # this limits how many messages your bot can store in its cache
            intents=intents,
            chunk_guilds_at_startup=False
            **kwargs,
            )

    async def start(self):
        self.session = aiohttp.ClientSession()
        self.db = await asyncpg.create_pool(config.YOUR_DB_KEY)

    
    async def close(self):
        await self.session.close()
        await self.db.close() # closes the database connection so your database doesn't cry for help
        await super().close()


    async def setup_hook(self):
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                try:
                    await self.load_extension(f"cogs.{filename[:-3]}")
                except commands.errors.ExtensionError:
                    traceback.print_exc()

    async def on_ready(self):
        print(f"Logged into discord as {self.bot.user} (with {self.bot.user.id} as my user ID!") # If this message is received, it means your bot is ready for use. aka connected to discord without issues

# this is to be done...

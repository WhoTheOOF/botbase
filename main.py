import discord, aiohttp, os, asyncpg, traceback # your general imports
from discord.ext import commands

import util.config as config # I use config, so this is a general import

# In this example, we will be assuming that you use cogs and a linux machine, windows will have its own thing I will add within the next week or so..
# The 'message_content' intent is required using this example, I won't cover slash anytime soon so have fun with that...ok maybe once...

intents = discord.Intents.all() # We don't need to define the 'message_content' intent since we used the 'all' factor of intents.

class BotBase(commands.AutoShardedBot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    async def start(self):
        self.session = aiohttp.ClientSession()
        self.db = await asyncpg.create_pool(config.YOUR_DB_KEY) # I use config because in my opinion, it's cool. so yeah..

    
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
        print(f"Logged into discord as {bot.user} (with {bot.user.id} as my user ID!") # If this message is received, it means your bot is ready for use. aka connected to discord without issues


bot = BotBase(
    command_prefix="bb!",
    intents=intents,
    chunk_guilds_at_startup=False, # can be set to true but that depends on your preference/usecase
    max_messages=1000, # this limits how many messages your bot will cache in its system. the number depends on your perference/usecase. don't set it too high unless you want a crash
    allowed_mentions=discord.AllowedMentions(everyone=False, roles=False, replied_user=True, users=True) # you can change all these to your likings, this is just for example sake
)

bot.run(config.YOUR_BOT_TOKEN) # We use config, which you can see, this isn't the best way to run a bot but I will cover advanced startup soon. i mean i use it but could be worse

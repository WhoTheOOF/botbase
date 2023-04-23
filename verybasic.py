import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True # enable this under dev portal
intents.message_content = True # be sure to enable it via the dev portal, and if you want to use presences too, just add intents.presences = True

bot = commands.Bot(intents=intents, command_prefix="prefix-goes-here") # change the "prefix-goes-here" to something like "bot!" or "**", allowing you to run [your-prefix]hello

@bot.event # generic event
async def on_ready():
    print(f"I've connected to discord as {bot.user} (my ID is {bot.user.id})")

@bot.command()
async def hello(ctx): # your param, which is always ctx but if its in a cog -> self, ctx
    await ctx.reply("hello!") # using the context reply feature, it directly replies.

bot.run('token') # run the bot of course

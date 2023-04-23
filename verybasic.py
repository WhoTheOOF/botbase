import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents, command_prefix="prefix-goes-here")

@bot.event
async def on_ready():
    print(f"I've connected to discord as {bot.user} (my ID is {bot.user.id})")

@bot.command()
async def hello(ctx):
    await ctx.reply("hello!")

bot.run('token')

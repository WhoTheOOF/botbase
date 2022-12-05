import discord
from discord.ext import commands

class ACog(commands.Cog):
    "Welcome to your first cog!"

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def embed(self, ctx): # the 'self' arg is required in cogs at all times, 'ctx' is just for context..i think you can understand it.
        """Put an embed out, because why not?"""
        e = discord.Embed(
            title = "Your Embed",
            description = "This is a description",
            color = 0x5865f2
        )
        await ctx.reply(embed=e)

    @commands.command()
    async def hello(self, ctx):
        """Hello!"""
        await ctx.reply(f"Hello {ctx.author.mention}!")

async def setup(bot):
    await bot.add_cog(ACog(bot))
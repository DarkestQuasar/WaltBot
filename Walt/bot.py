# -*- coding: utf-8 -*-
import os

import discord
from discord.ext import commands
from discord.ext.commands import Bot
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("DISCORD_TOKEN")


class GeneralCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kill(self, ctx):
        await ctx.send(f"Stopping upon the request of {ctx.author.mention}")
        await self.bot.close()
        exit(0)

    @commands.command()
    async def stop(self, ctx):
        await ctx.send(f"Stopping upon the request of {ctx.author.mention}")
        await self.bot.close()
        exit(0)

    @commands.command()
    async def hello_world(self, ctx):
        await ctx.send("Hello, World!")


bot = Bot(command_prefix="$")
bot.add_cog(GeneralCommands(bot))
bot.run(token)

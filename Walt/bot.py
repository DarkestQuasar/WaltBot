# -*- coding: utf-8 -*-
import os
import secrets

import discord
from discord.ext import commands
from discord.ext.commands import Bot
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("DISCORD_TOKEN")


def load_roasts(filename):
    with open(filename, "r") as f:
        content = f.readlines()
    content = [i.strip() for i in content]
    return content


class GeneralCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.roasts = load_roasts("roasts.txt")

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

    @commands.command()
    async def roast(self, ctx):
        choice = secrets.choice(self.roasts)
        await ctx.send(choice)

    # @discord.AuditLogActionCategory(after)
    # async def update(self, users, data, guild):
    #     await ctx.send(ctx)


if __name__ == "__main__":
    bot = Bot(command_prefix="$")
    bot.add_cog(GeneralCommands(bot))
    bot.run(token)

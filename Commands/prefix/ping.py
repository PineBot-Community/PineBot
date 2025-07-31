from discord.ext import commands
import discord

def setup(bot):
    @bot.command()
    async def ping(ctx):
        embed = discord.Embed(
            title="🏓 Pong!",
            description=f"Задержка: {round(bot.latency * 1000)} ms",
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed)

import discord
from discord.ext import commands
import platform
import datetime

def setup(bot):
    @bot.command()
    async def info(ctx):
        embed = discord.Embed(
            title="Информация о сервере",
            color=discord.Color.dark_blue()
        )
        embed.add_field(name="Название", value=ctx.guild.name, inline=False)
        embed.add_field(name="Владелец", value=str(ctx.guild.owner), inline=False)
        embed.add_field(name="Регион", value=str(ctx.guild.region), inline=False)
        embed.add_field(name="Участников", value=str(ctx.guild.member_count), inline=False)
        embed.add_field(name="Создан", value=ctx.guild.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=False)

        await ctx.send(embed=embed)

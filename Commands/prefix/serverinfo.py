import discord
from discord.ext import commands

def setup(bot):
    @bot.command()
    async def serverinfo(ctx):
        guild = ctx.guild
        embed = discord.Embed(
            title=f"Информация о сервере {guild.name}",
            color=discord.Color.blue()
        )
        embed.add_field(name="Создан", value=guild.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
        embed.add_field(name="Владелец", value=str(guild.owner), inline=False)
        embed.add_field(name="Участников", value=str(guild.member_count), inline=False)
        embed.add_field(name="Каналов", value=str(len(guild.channels)), inline=False)
        embed.set_thumbnail(url=guild.icon.url if guild.icon else None)

        await ctx.send(embed=embed)

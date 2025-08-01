import discord
from discord.ext import commands

# Заглушка. Можно добавить уровни, опыт, и т.д.
def setup(bot):
    @bot.command()
    async def rank(ctx, member: discord.Member = None):
        member = member or ctx.author
        embed = discord.Embed(
            title=f"Ранг пользователя {member}",
            description="Уровень: 1\nОпыт: 0/100",
            color=discord.Color.gold()
        )
        await ctx.send(embed=embed)

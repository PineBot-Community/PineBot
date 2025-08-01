import discord
from discord.ext import commands

warnings_db = {}  # Тот же словарь

def setup(bot):
    @bot.command()
    @commands.has_permissions(kick_members=True)
    async def warn(ctx, member: discord.Member, *, reason=None):
        user_id = member.id
        warnings_db[user_id] = warnings_db.get(user_id, 0) + 1
        embed = discord.Embed(
            title="Пользователь предупрежден",
            description=f"{member} получил предупреждение.\nПричина: {reason or 'Не указана'}\nВсего предупреждений: {warnings_db[user_id]}",
            color=discord.Color.orange()
        )
        await ctx.send(embed=embed)

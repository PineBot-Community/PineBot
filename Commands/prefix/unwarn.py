import discord
from discord.ext import commands

# Предполагается, что у тебя есть какая-то система предупреждений, например, в БД или JSON.
# Здесь пример заглушки.

warnings_db = {}  # Пример словаря: {user_id: warn_count}

def setup(bot):
    @bot.command()
    @commands.has_permissions(kick_members=True)
    async def unwarn(ctx, member: discord.Member):
        user_id = member.id
        if warnings_db.get(user_id, 0) > 0:
            warnings_db[user_id] -= 1
            embed = discord.Embed(
                title="Предупреждение снято",
                description=f"У пользователя {member} предупреждений стало: {warnings_db[user_id]}",
                color=discord.Color.green()
            )
        else:
            embed = discord.Embed(
                title="Нет предупреждений",
                description=f"У пользователя {member} нет предупреждений для снятия.",
                color=discord.Color.red()
            )
        await ctx.send(embed=embed)

import discord
from discord.ext import commands

def setup(bot):
    @bot.command()
    @commands.has_permissions(ban_members=True)
    async def ban(ctx, member: discord.Member, *, reason=None):
        try:
            await member.ban(reason=reason)
            embed = discord.Embed(
                title="Пользователь забанен",
                description=f"{member} был забанен.\nПричина: {reason or 'Не указана'}",
                color=discord.Color.red()
            )
        except Exception as e:
            embed = discord.Embed(
                title="Ошибка бана",
                description=str(e),
                color=discord.Color.red()
            )
        await ctx.send(embed=embed)

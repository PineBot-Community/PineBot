import discord
from discord.ext import commands

def setup(bot):
    @bot.command()
    async def leaderstats(ctx, member: discord.Member = None):
        member = member or ctx.author

        embed = discord.Embed(
            title=f"Статистика пользователя {member}",
            color=discord.Color.purple()
        )
        embed.add_field(name="Имя", value=str(member), inline=True)
        embed.add_field(name="ID", value=member.id, inline=True)
        embed.add_field(name="Статус", value=str(member.status).title(), inline=True)
        embed.add_field(name="Роли", value=", ".join([role.name for role in member.roles if role.name != "@everyone"]), inline=False)
        embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)

        await ctx.send(embed=embed)

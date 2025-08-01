import discord
from discord.ext import commands

def setup(bot):
    @bot.command()
    async def avatar(ctx, member: discord.Member = None):
        member = member or ctx.author
        embed = discord.Embed(
            title=f"Аватар пользователя {member}",
            color=discord.Color.green()
        )
        embed.set_image(url=member.avatar.url if member.avatar else member.default_avatar.url)
        await ctx.send(embed=embed)

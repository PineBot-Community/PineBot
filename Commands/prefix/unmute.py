import discord
from discord.ext import commands

def setup(bot):
    @bot.command()
    @commands.has_permissions(manage_roles=True)
    async def unmute(ctx, member: discord.Member):
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not role:
            await ctx.send("Роль Muted не найдена.")
            return

        await member.remove_roles(role)
        embed = discord.Embed(
            title="Пользователь размьючен",
            description=f"{member} больше не замьючен.",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)

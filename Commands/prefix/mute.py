import discord
from discord.ext import commands

def setup(bot):
    @bot.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(ctx, member: discord.Member, *, reason=None):
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not role:
            try:
                role = await ctx.guild.create_role(name="Muted")
                for channel in ctx.guild.channels:
                    await channel.set_permissions(role, send_messages=False, speak=False)
            except Exception as e:
                await ctx.send(f"Не удалось создать роль Muted: {e}")
                return

        await member.add_roles(role, reason=reason)
        embed = discord.Embed(
            title="Пользователь замьючен",
            description=f"{member} был замьючен.\nПричина: {reason or 'Не указана'}",
            color=discord.Color.dark_gray()
        )
        await ctx.send(embed=embed)

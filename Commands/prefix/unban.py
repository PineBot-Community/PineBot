import discord
from discord.ext import commands

def setup(bot):
    @bot.command()
    @commands.has_permissions(ban_members=True)
    async def unban(ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                embed = discord.Embed(
                    title="Пользователь разбанен",
                    description=f"{user} был разбанен.",
                    color=discord.Color.green()
                )
                await ctx.send(embed=embed)
                return

        await ctx.send(f"Пользователь {member} не найден в бан-листе.")

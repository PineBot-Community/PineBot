import discord
from discord import app_commands
from discord.ext import commands

class Rank(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="rank", description="Показать ранг пользователя")
    @app_commands.describe(member="Пользователь")
    async def rank(self, interaction: discord.Interaction, member: discord.Member = None):
        member = member or interaction.user
        embed = discord.Embed(
            title=f"Ранг пользователя {member}",
            description="Уровень: 1\nОпыт: 0/100",
            color=discord.Color.gold()
        )
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Rank(bot))

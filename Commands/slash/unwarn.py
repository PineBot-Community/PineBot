# unwarn.py
from discord import app_commands
import discord

warnings_db = {}

class SlashCommands:
    def __init__(self, bot):
        self.bot = bot

    async def setup(self):
        @app_commands.command(name="unwarn", description="Снять предупреждение")
        @app_commands.describe(member="Пользователь")
        @app_commands.checks.has_permissions(kick_members=True)
        async def unwarn(interaction: discord.Interaction, member: discord.Member):
            uid = member.id
            if warnings_db.get(uid, 0) > 0:
                warnings_db[uid] -= 1
                embed = discord.Embed(
                    title="Снято предупреждение",
                    description=f"{member}. Осталось: {warnings_db[uid]}",
                    color=discord.Color.green()
                )
            else:
                embed = discord.Embed(
                    title="Нет предупреждений",
                    description=f"У {member} нет предупреждений.",
                    color=discord.Color.red()
                )
            await interaction.response.send_message(embed=embed)

        self.bot.tree.add_command(unwarn)

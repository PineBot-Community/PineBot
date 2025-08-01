# warn.py
from discord import app_commands
import discord

warnings_db = {}

class SlashCommands:
    def __init__(self, bot):
        self.bot = bot

    async def setup(self):
        @app_commands.command(name="warn", description="Выдать предупреждение")
        @app_commands.describe(member="Пользователь", reason="Причина")
        @app_commands.checks.has_permissions(kick_members=True)
        async def warn(interaction: discord.Interaction, member: discord.Member, reason: str = None):
            uid = member.id
            warnings_db[uid] = warnings_db.get(uid, 0) + 1
            embed = discord.Embed(
                title="Предупреждение",
                description=f"{member} получил предупреждение.\nПричина: {reason or 'Не указана'}\nВсего: {warnings_db[uid]}",
                color=discord.Color.orange()
            )
            await interaction.response.send_message(embed=embed)

        self.bot.tree.add_command(warn)

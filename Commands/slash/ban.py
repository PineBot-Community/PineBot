from discord import app_commands
import discord

class SlashCommands:
    def __init__(self, bot):
        self.bot = bot

    async def setup(self):
        @app_commands.command(name="ban", description="Забанить пользователя")
        @app_commands.describe(member="Пользователь для бана", reason="Причина (необязательно)")
        @app_commands.checks.has_permissions(ban_members=True)
        async def ban(interaction: discord.Interaction, member: discord.Member, reason: str = None):
            try:
                await member.ban(reason=reason)
                embed = discord.Embed(
                    title="Пользователь забанен",
                    description=f"{member} забанен.\nПричина: {reason or 'Не указана'}",
                    color=discord.Color.red()
                )
                await interaction.response.send_message(embed=embed)
            except Exception as e:
                await interaction.response.send_message(f"Ошибка: {e}", ephemeral=True)

        self.bot.tree.add_command(ban)

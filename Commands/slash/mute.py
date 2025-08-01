from discord import app_commands
import discord

class SlashCommands:
    def __init__(self, bot):
        self.bot = bot

    async def setup(self):
        @app_commands.command(name="mute", description="Замутить пользователя")
        @app_commands.describe(member="Пользователь", reason="Причина (необязательно)")
        @app_commands.checks.has_permissions(manage_roles=True)
        async def mute(interaction: discord.Interaction, member: discord.Member, reason: str = None):
            role = discord.utils.get(interaction.guild.roles, name="Muted")
            if not role:
                try:
                    role = await interaction.guild.create_role(name="Muted")
                    for ch in interaction.guild.channels:
                        await ch.set_permissions(role, send_messages=False, speak=False)
                except Exception as e:
                    await interaction.response.send_message(f"Ошибка создания роли Muted: {e}", ephemeral=True)
                    return

            await member.add_roles(role, reason=reason)
            embed = discord.Embed(
                title="Пользователь замьючен",
                description=f"{member} был замьючен.\nПричина: {reason or 'Не указана'}",
                color=discord.Color.dark_gray()
            )
            await interaction.response.send_message(embed=embed)

        self.bot.tree.add_command(mute)

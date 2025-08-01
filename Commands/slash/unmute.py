from discord import app_commands
import discord

class SlashCommands:
    def __init__(self, bot):
        self.bot = bot

    async def setup(self):
        @app_commands.command(name="unmute", description="Снять мут с пользователя")
        @app_commands.describe(member="Пользователь")
        @app_commands.checks.has_permissions(manage_roles=True)
        async def unmute(interaction: discord.Interaction, member: discord.Member):
            role = discord.utils.get(interaction.guild.roles, name="Muted")
            if not role:
                await interaction.response.send_message("Роль Muted не найдена.", ephemeral=True)
                return

            await member.remove_roles(role)
            embed = discord.Embed(
                title="Размьючен",
                description=f"{member} больше не замьючен.",
                color=discord.Color.green()
            )
            await interaction.response.send_message(embed=embed)

        self.bot.tree.add_command(unmute)

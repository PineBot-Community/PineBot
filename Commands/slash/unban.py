from discord import app_commands
import discord

class SlashCommands:
    def __init__(self, bot):
        self.bot = bot

    async def setup(self):
        @app_commands.command(name="unban", description="Разбанить пользователя")
        @app_commands.describe(user="Имя пользователя в формате Name#0000")
        @app_commands.checks.has_permissions(ban_members=True)
        async def unban(interaction: discord.Interaction, user: str):
            banned = await interaction.guild.bans()
            name, disc = user.split('#')
            for entry in banned:
                u = entry.user
                if (u.name, u.discriminator) == (name, disc):
                    await interaction.guild.unban(u)
                    embed = discord.Embed(
                        title="Разбан",
                        description=f"{u} был разбанен.",
                        color=discord.Color.green()
                    )
                    await interaction.response.send_message(embed=embed)
                    return
            await interaction.response.send_message(f"Пользователь {user} не в бан-листе.", ephemeral=True)

        self.bot.tree.add_command(unban)

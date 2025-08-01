from discord import app_commands
import discord

class SlashCommands:
    def __init__(self, bot):
        self.bot = bot

    async def setup(self):
        @app_commands.command(name="avatar", description="Показать аватар пользователя")
        @app_commands.describe(user="Пользователь (по умолчанию — вы)")
        async def avatar(interaction: discord.Interaction, user: discord.User = None):
            user = user or interaction.user
            embed = discord.Embed(
                title=f"Аватар {user}",
                color=discord.Color.green()
            )
            embed.set_image(url=user.display_avatar.url)
            await interaction.response.send_message(embed=embed)

        self.bot.tree.add_command(avatar)

from discord import app_commands
import discord

class SlashCommands:
    def __init__(self, bot):
        self.bot = bot

    async def setup(self):
        @app_commands.command(name="about", description="Информация о боте")
        async def about(interaction: discord.Interaction):
            embed = discord.Embed(
                title="О боте",
                description="Этот бот создан для управления сервером и развлечений.",
                color=discord.Color.blurple()
            )
            embed.add_field(name="Версия", value="1.0.0")
            embed.set_footer(text=f"Запрос от {interaction.user}", icon_url=interaction.user.avatar.url if interaction.user.avatar else None)
            await interaction.response.send_message(embed=embed)

        self.bot.tree.add_command(about)

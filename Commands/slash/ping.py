import discord
from discord import app_commands

class SlashCommands:
    def __init__(self, bot: discord.Client):
        self.bot = bot

    async def setup(self):
        @app_commands.command(name="ping", description="Ответит Pong!")
        async def ping(interaction: discord.Interaction):
            try:
                embed = discord.Embed(
                    title="🏓 Pong!",
                    description=f"Задержка: {round(self.bot.latency * 1000)} ms",
                    color=discord.Color.blue()
                )
                await interaction.response.send_message(embed=embed)
            except Exception as e:
                print(f"Error in ping command: {e}")
                # Если уже ответили, можно отправить followup:
                if interaction.response.is_done():
                    await interaction.followup.send("Произошла ошибка при выполнении команды.")
                else:
                    # Если не ответили — пытаемся ответить ошибкой
                    await interaction.response.send_message("Произошла ошибка при выполнении команды.", ephemeral=True)

        self.bot.tree.add_command(ping)

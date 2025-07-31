import discord
from discord import app_commands
import asyncio

class SlashCommands:
    def __init__(self, bot: discord.Client):
        self.bot = bot

    async def setup(self):
        @app_commands.command(name="clear", description="Удалить сообщения из канала")
        @app_commands.describe(amount="Количество сообщений для удаления (по умолчанию 5, максимум 100)")
        async def clear(interaction: discord.Interaction, amount: int = 5):
            amount = max(1, min(amount, 100))

            await interaction.response.defer(ephemeral=True)

            total_deleted = 0
            chunk_size = 10

            try:
                while total_deleted < amount:
                    to_delete = min(chunk_size, amount - total_deleted)
                    deleted = await interaction.channel.purge(limit=to_delete)
                    total_deleted += len(deleted)

                    if len(deleted) < to_delete:
                        break

                    await asyncio.sleep(0.5)

                embed = discord.Embed(
                    title="Очистка сообщений",
                    description=f"Удалено сообщений: **{total_deleted}**",
                    color=discord.Color.green()
                )
            except Exception as e:
                embed = discord.Embed(
                    title="Ошибка при очистке",
                    description=f"Что-то пошло не так:\n```{e}```",
                    color=discord.Color.red()
                )

            await interaction.followup.send(embed=embed, ephemeral=True)

        self.bot.tree.add_command(clear)

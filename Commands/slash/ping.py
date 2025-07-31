import discord
from discord import app_commands

class Ping(discord.app_commands.CommandTree):
    def __init__(self, bot):
        super().__init__(bot)

    @app_commands.command(name="ping", description="Replies with Pong!")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message("Pong!")

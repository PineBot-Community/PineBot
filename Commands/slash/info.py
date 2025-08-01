from discord import app_commands
import discord

class SlashCommands:
    def __init__(self, bot):
        self.bot = bot

    async def setup(self):
        @app_commands.command(name="info", description="Информация о сервере")
        async def info(interaction: discord.Interaction):
            guild = interaction.guild
            embed = discord.Embed(title=f"Сервер {guild.name}", color=discord.Color.blue())
            embed.add_field(name="Владелец", value=str(guild.owner), inline=False)
            embed.add_field(name="Участников", value=str(guild.member_count), inline=False)
            embed.add_field(name="Каналов", value=str(len(guild.channels)), inline=False)
            embed.add_field(name="Создан", value=guild.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
            await interaction.response.send_message(embed=embed)

        self.bot.tree.add_command(info)

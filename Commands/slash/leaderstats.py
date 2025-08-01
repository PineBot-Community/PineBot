from discord import app_commands
import discord

class SlashCommands:
    def __init__(self, bot):
        self.bot = bot

    async def setup(self):
        @app_commands.command(name="leaderstats", description="Показать статистику пользователя")
        @app_commands.describe(member="Пользователь")
        async def leaderstats(interaction: discord.Interaction, member: discord.Member = None):
            member = member or interaction.user
            embed = discord.Embed(
                title=f"Статистика — {member}",
                color=discord.Color.purple()
            )
            embed.add_field(name="ID", value=str(member.id), inline=True)
            embed.add_field(name="Статус", value=str(member.status).title(), inline=True)
            embed.add_field(name="Роли", value=", ".join(r.name for r in member.roles if r.name != "@everyone"), inline=False)
            embed.set_thumbnail(url=member.display_avatar.url)
            await interaction.response.send_message(embed=embed)

        self.bot.tree.add_command(leaderstats)

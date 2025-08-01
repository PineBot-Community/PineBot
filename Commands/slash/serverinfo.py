import discord
from discord import app_commands
from discord.ext import commands

class Serverinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="serverinfo", description="Информация о сервере")
    async def serverinfo(self, interaction: discord.Interaction):
        guild = interaction.guild
        embed = discord.Embed(
            title=f"Информация о сервере {guild.name}",
            color=discord.Color.blue()
        )
        embed.add_field(name="Создан", value=guild.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
        embed.add_field(name="Владелец", value=str(guild.owner), inline=False)
        embed.add_field(name="Участников", value=str(guild.member_count), inline=False)
        embed.add_field(name="Каналов", value=str(len(guild.channels)), inline=False)
        embed.set_thumbnail(url=guild.icon.url if guild.icon else None)

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Serverinfo(bot))

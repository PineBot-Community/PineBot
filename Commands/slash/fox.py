from discord import app_commands
import discord
import aiohttp

class SlashCommands:
    def __init__(self, bot):
        self.bot = bot

    async def setup(self):
        @app_commands.command(name="fox", description="Показать случайную лису")
        async def fox(interaction: discord.Interaction):
            async with aiohttp.ClientSession() as session:
                async with session.get("https://randomfox.ca/floof/") as resp:
                    url = (await resp.json()).get("image") if resp.status == 200 else None

            embed = discord.Embed(title="Лиса 🦊", color=discord.Color.gold())
            if url:
                embed.set_image(url=url)
            else:
                embed.description = "Не удалось получить картинку."
            await interaction.response.send_message(embed=embed)

        self.bot.tree.add_command(fox)

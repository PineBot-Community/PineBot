from discord import app_commands
from discord.ui import Button, View
import discord
import random

cat_pics = [
    "https://cdn2.thecatapi.com/images/MTY3ODIyMQ.jpg",
    "https://cdn2.thecatapi.com/images/MTY3ODIyMw.jpg",
    "https://cdn2.thecatapi.com/images/MTY3ODIyNA.jpg"
]

class SlashCommands:
    def __init__(self, bot):
        self.bot = bot

    async def setup(self):
        @app_commands.command(name="cat", description="Показать случайного котика")
        async def cat(interaction: discord.Interaction):
            url = random.choice(cat_pics)
            embed = discord.Embed(title="Котик 🐱", color=discord.Color.orange())
            embed.set_image(url=url)

            button = Button(label="Сменить котика", style=discord.ButtonStyle.primary)

            async def button_callback(inter):
                if inter.user != interaction.user:
                    await inter.response.send_message("Это не твоя кнопка!", ephemeral=True)
                    return
                new_url = random.choice(cat_pics)
                embed.set_image(url=new_url)
                await inter.response.edit_message(embed=embed, view=view)

            button.callback = button_callback
            view = View()
            view.add_item(button)

            await interaction.response.send_message(embed=embed, view=view)

        self.bot.tree.add_command(cat)

from discord import app_commands
from discord.ui import Button, View
import discord
import random

dog_pics = [
    "https://images.dog.ceo/breeds/husky/n02110185_1469.jpg",
    "https://images.dog.ceo/breeds/retriever-golden/n02099601_2003.jpg",
    "https://images.dog.ceo/breeds/terrier-norwich/n02094258_2443.jpg"
]

class SlashCommands:
    def __init__(self, bot):
        self.bot = bot

    async def setup(self):
        @app_commands.command(name="dog", description="Показать случайного пёсика")
        async def dog(interaction: discord.Interaction):
            url = random.choice(dog_pics)
            embed = discord.Embed(title="Пёсик 🐶", color=discord.Color.blue())
            embed.set_image(url=url)

            button = Button(label="Сменить пёсика", style=discord.ButtonStyle.success)

            async def button_callback(inter):
                if inter.user != interaction.user:
                    await inter.response.send_message("Это не твоя кнопка!", ephemeral=True)
                    return
                new_url = random.choice(dog_pics)
                embed.set_image(url=new_url)
                await inter.response.edit_message(embed=embed, view=view)

            button.callback = button_callback
            view = View()
            view.add_item(button)

            await interaction.response.send_message(embed=embed, view=view)

        self.bot.tree.add_command(dog)

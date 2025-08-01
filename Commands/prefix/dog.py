import discord
from discord.ext import commands
from discord.ui import Button, View
import random

dog_pics = [
    "https://images.dog.ceo/breeds/husky/n02110185_1469.jpg",
    "https://images.dog.ceo/breeds/retriever-golden/n02099601_2003.jpg",
    "https://images.dog.ceo/breeds/terrier-norwich/n02094258_2443.jpg"
]

def setup(bot):
    @bot.command()
    async def dog(ctx):
        url = random.choice(dog_pics)
        embed = discord.Embed(
            title="Пёсик для тебя 🐶",
            color=discord.Color.blue()
        )
        embed.set_image(url=url)

        button = Button(label="Сменить пёсика", style=discord.ButtonStyle.success)

        async def button_callback(interaction):
            if interaction.user != ctx.author:
                await interaction.response.send_message("Это не твоя кнопка!", ephemeral=True)
                return
            new_url = random.choice(dog_pics)
            embed.set_image(url=new_url)
            await interaction.response.edit_message(embed=embed, view=view)

        button.callback = button_callback
        view = discord.ui.View()
        view.add_item(button)

        await ctx.send(embed=embed, view=view)

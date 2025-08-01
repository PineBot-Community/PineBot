import discord
from discord.ext import commands
from discord.ui import Button, View
import random

cat_pics = [
    "https://cdn2.thecatapi.com/images/MTY3ODIyMQ.jpg",
    "https://cdn2.thecatapi.com/images/MTY3ODIyMw.jpg",
    "https://cdn2.thecatapi.com/images/MTY3ODIyNA.jpg"
]

def setup(bot):
    @bot.command()
    async def cat(ctx):
        url = random.choice(cat_pics)
        embed = discord.Embed(
            title="Котик для тебя 🐱",
            color=discord.Color.orange()
        )
        embed.set_image(url=url)

        button = Button(label="Сменить котика", style=discord.ButtonStyle.primary)

        async def button_callback(interaction):
            if interaction.user != ctx.author:
                await interaction.response.send_message("Это не твоя кнопка!", ephemeral=True)
                return
            new_url = random.choice(cat_pics)
            embed.set_image(url=new_url)
            await interaction.response.edit_message(embed=embed, view=view)

        button.callback = button_callback
        view = View()
        view.add_item(button)

        await ctx.send(embed=embed, view=view)

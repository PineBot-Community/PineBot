import discord
from discord.ext import commands
import aiohttp

def setup(bot):
    @bot.command()
    async def fox(ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://randomfox.ca/floof/") as resp:
                if resp.status == 200:
                    data = await resp.json()
                    url = data.get("image")
                else:
                    url = None

        embed = discord.Embed(
            title="Рандомная лиса 🦊",
            color=discord.Color.gold()
        )
        if url:
            embed.set_image(url=url)
        else:
            embed.description = "Не удалось получить картинку."

        await ctx.send(embed=embed)

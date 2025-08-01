import discord
from discord.ext import commands

def setup(bot):
    @bot.command()
    async def about(ctx):
        embed = discord.Embed(
            title="О боте",
            description="Этот бот создан для управления сервером и развлечений.",
            color=discord.Color.blurple()
        )
        embed.add_field(name="Версия", value="1.0.0")
        embed.set_footer(text=f"Запрос от {ctx.author}", icon_url=ctx.author.avatar.url if ctx.author.avatar else None)
        await ctx.send(embed=embed)

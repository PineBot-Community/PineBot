import discord
from discord.ext import commands

def setup(bot):
    @bot.command()
    async def help(ctx):
        embed = discord.Embed(
            title="Помощь по командам",
            description="Список доступных команд:",
            color=discord.Color.teal()
        )
        embed.add_field(name="!ping", value="Проверить задержку", inline=False)
        embed.add_field(name="!clear [кол-во]", value="Удалить сообщения", inline=False)
        embed.add_field(name="!ban <пользователь> [причина]", value="Забанить пользователя", inline=False)
        embed.add_field(name="!unban <пользователь>", value="Разбанить пользователя", inline=False)
        embed.add_field(name="!mute <пользователь>", value="Выдать мут", inline=False)
        embed.add_field(name="!unmute <пользователь>", value="Снять мут", inline=False)
        embed.add_field(name="!warn <пользователь>", value="Выдать предупреждение", inline=False)
        embed.add_field(name="!unwarn <пользователь>", value="Снять предупреждение", inline=False)
        embed.set_footer(text=f"Запрос от {ctx.author}", icon_url=ctx.author.avatar.url if ctx.author.avatar else None)

        await ctx.send(embed=embed)

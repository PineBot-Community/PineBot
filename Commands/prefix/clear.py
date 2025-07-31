from discord.ext import commands
import discord
import asyncio

def setup(bot):
    @bot.command()
    async def clear(ctx, amount: int = 5):
        amount = max(1, min(amount, 100))  # Ограничение от 1 до 100

        total_deleted = 0
        chunk_size = 10  # Пакеты по 10 сообщений

        try:
            while total_deleted < amount:
                to_delete = min(chunk_size, amount - total_deleted)
                deleted = await ctx.channel.purge(limit=to_delete)
                total_deleted += len(deleted)

                if len(deleted) < to_delete:
                    break  # Сообщений меньше, чем запросили

                await asyncio.sleep(0.5)  # Пауза 0.5 секунды между пакетами

            embed = discord.Embed(
                title="Очистка сообщений",
                description=f"Удалено сообщений: **{total_deleted}**",
                color=discord.Color.green()
            )
        except Exception as e:
            embed = discord.Embed(
                title="Ошибка при очистке",
                description=f"Что-то пошло не так:\n```{e}```",
                color=discord.Color.red()
            )

        message = await ctx.send(embed=embed)
        await asyncio.sleep(5)
        await message.delete()

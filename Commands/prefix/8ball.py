from discord.ext import commands
import discord
import random

def setup(bot):
    @bot.command(name="8ball", help="Задай вопрос, и я отвечу 🎱")
    async def eight_ball(ctx, *, question: str = None):
        if question is None:
            embed = discord.Embed(
                title="❗ Вопрос не указан",
                description="Пожалуйста, укажи вопрос после команды.\nПример: `!8ball Будет ли завтра солнце?`",
                color=discord.Color.orange()
            )
            await ctx.send(embed=embed)
            return

        responses = [
            "Бесспорно.",
            "Предрешено.",
            "Никаких сомнений.",
            "Определённо да.",
            "Можешь быть уверен в этом.",
            "Мне кажется — «да».",
            "Вероятнее всего.",
            "Хорошие перспективы.",
            "Знаки говорят — «да».",
            "Да.",
            "Пока не ясно, попробуй снова.",
            "Спроси позже.",
            "Лучше не рассказывать тебе сейчас.",
            "Сконцентрируйся и спроси опять.",
            "Даже не думай.",
            "Мой ответ — «нет».",
            "По моим данным — «нет».",
            "Перспективы не очень хорошие.",
            "Весьма сомнительно."
        ]

        answer = random.choice(responses)
        embed = discord.Embed(
            title="🎱 Ответ от 8ball",
            color=discord.Color.dark_purple()
        )
        embed.add_field(name="Вопрос", value=question, inline=False)
        embed.add_field(name="Ответ", value=answer, inline=False)
        embed.set_footer(text=f"Запрос от {ctx.author}", icon_url=ctx.author.avatar.url if ctx.author.avatar else None)

        await ctx.send(embed=embed)

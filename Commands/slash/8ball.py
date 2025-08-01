from discord import app_commands
import discord
import random

class SlashCommands:
    def __init__(self, bot):
        self.bot = bot

    async def setup(self):
        @app_commands.command(name="8ball", description="🎱 Задай вопрос шару предсказаний")
        @app_commands.describe(question="Твой вопрос")
        async def _8ball(interaction: discord.Interaction, question: str):
            responses = [
                "Бесспорно.", "Предрешено.", "Никаких сомнений.", "Определённо да.",
                "Можешь быть уверен в этом.", "Мне кажется — «да».", "Вероятнее всего.",
                "Хорошие перспективы.", "Знаки говорят — «да».", "Да.",
                "Пока не ясно, попробуй снова.", "Спроси позже.",
                "Лучше не рассказывать тебе сейчас.", "Сконцентрируйся и спроси опять.",
                "Даже не думай.", "Мой ответ — «нет».", "По моим данным — «нет».",
                "Перспективы не очень хорошие.", "Весьма сомнительно."
            ]
            embed = discord.Embed(
                title="🎱 8ball",
                color=discord.Color.blurple()
            )
            answer = random.choice(responses)
            embed.add_field(name="Вопрос", value=question, inline=False)
            embed.add_field(name="Ответ", value=answer, inline=False)
            await interaction.response.send_message(embed=embed)

        self.bot.tree.add_command(_8ball)

from discord import app_commands
import discord

class SlashCommands:
    def __init__(self, bot):
        self.bot = bot

    async def setup(self):
        @app_commands.command(name="help", description="Список доступных команд")
        async def help_cmd(interaction: discord.Interaction):
            embed = discord.Embed(title="Помощь", description="Список наших команд:", color=discord.Color.teal())
            cmds = [
                ("/ping", "Проверить задержку"),
                ("/clear", "Удалить сообщения"),
                ("/8ball", "Задать вопрос шару"),
                ("/avatar", "Показать аватар"),
                ("/cat", "Котик"),
                ("/dog", "Пёсик"),
                ("/fox", "Лиса"),
                ("/ban", "Забанить пользователя"),
                ("/unban", "Разбанить"),
                ("/mute", "Замутить"),
                ("/unmute", "Демут"),
                ("/warn", "Выдать предупреждение"),
                ("/unwarn", "Снять предупреждение"),
                ("/leaderstats", "Статистика пользователя"),
                ("/info", "Сведения о сервере")
            ]
            for name, desc in cmds:
                embed.add_field(name=name, value=desc, inline=False)
            await interaction.response.send_message(embed=embed)

        self.bot.tree.add_command(help_cmd)

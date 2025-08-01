import discord
from discord.ext import commands
import os
import asyncio
from dotenv import load_dotenv
from watchdog.observers import Observer

from commands_loader import load_prefix_commands, reload_slash_commands, CommandsReloadHandler

# Загрузка токена из .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))

# Настройка интентов и префикса
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")

    try:
        load_prefix_commands(bot)           # Загрузка prefix команд
        await reload_slash_commands(bot)    # Загрузка + синхронизация slash команд
    except Exception as e:
        print(f"❌ Error in initial load: {e}")

    # Автообновление при изменениях в папках
    loop = asyncio.get_event_loop()
    event_handler = CommandsReloadHandler(loop, bot)
    observer = Observer()
    observer.schedule(event_handler, path="Commands/slash", recursive=True)
    observer.schedule(event_handler, path="Commands/prefix", recursive=True)
    observer.start()

    print("🔁 Watching for changes in command files...")

@bot.command()
@commands.is_owner()
async def reloadslash(ctx):
    await reload_slash_commands(bot)
    await ctx.send("🔁 Slash commands globally reloaded.")

bot.run(TOKEN)

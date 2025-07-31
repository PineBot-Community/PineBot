import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio
from watchdog.observers import Observer
from commands_loader import load_prefix_commands, reload_slash_commands, CommandsReloadHandler

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")

    try:
        load_prefix_commands(bot)
        await reload_slash_commands(bot)
    except Exception as e:
        print(f"Error in initial load: {e}")

    loop = asyncio.get_event_loop()
    event_handler = CommandsReloadHandler(loop, lambda: reload_slash_commands(bot))
    observer = Observer()
    observer.schedule(event_handler, path="Commands/slash", recursive=True)
    observer.schedule(event_handler, path="Commands/prefix", recursive=True)
    observer.start()
    print("Started watching commands folders for changes.")

@bot.command()
@commands.is_owner()
async def reloadslash(ctx):
    await reload_slash_commands(bot)
    await ctx.send("Global slash commands reloaded!")

bot.run(TOKEN)

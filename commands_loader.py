import pathlib
import importlib
import traceback
import asyncio
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def load_prefix_commands(bot):
    prefix_path = pathlib.Path("Commands/prefix")
    for file in prefix_path.glob("*.py"):
        if file.name != "__init__.py":
            module_name = f"Commands.prefix.{file.stem}"
            try:
                print(f"Loading prefix command: {module_name}")
                importlib.import_module(module_name).setup(bot)
            except Exception as e:
                print(f"Error loading prefix command {module_name}: {e}")
                traceback.print_exc()

async def load_slash_commands(bot):
    slash_path = pathlib.Path("Commands/slash")
    for file in slash_path.glob("*.py"):
        if file.name != "__init__.py":
            module_name = f"Commands.slash.{file.stem}"
            try:
                print(f"Loading slash command: {module_name}")
                mod = importlib.import_module(module_name)
                if hasattr(mod, "SlashCommands"):
                    slash_instance = mod.SlashCommands(bot)
                    await slash_instance.setup()
            except Exception as e:
                print(f"Error loading slash command {module_name}: {e}")
                traceback.print_exc()

async def reload_slash_commands(bot):
    try:
        print("Reloading slash commands...")
        bot.tree.clear_commands(guild=None)  # Очистка глобальных команд
        await load_slash_commands(bot)       # Загрузка всех команд
        synced = await bot.tree.sync()       # Глобальная синхронизация
        print(f"Reloaded and synced {len(synced)} global slash command(s).")
    except Exception as e:
        print(f"Error during slash commands reload: {e}")
        traceback.print_exc()

class CommandsReloadHandler(FileSystemEventHandler):
    def __init__(self, loop, bot):
        self.loop = loop
        self.bot = bot
        self.debounce_task = None

    def on_modified(self, event):
        if event.src_path.endswith('.py'):
            print(f"Detected file change: {event.src_path}")
            if self.debounce_task is None or self.debounce_task.done():
                self.debounce_task = asyncio.run_coroutine_threadsafe(
                    self.delayed_reload(), self.loop
                )

    async def delayed_reload(self):
        await asyncio.sleep(1.5)
        print("Triggering reload of slash commands due to file change...")
        try:
            await reload_slash_commands(self.bot)
        except Exception:
            traceback.print_exc()

def start_watching(loop, bot):
    event_handler = CommandsReloadHandler(loop, bot)
    observer = Observer()
    observer.schedule(event_handler, path="Commands/slash", recursive=False)
    observer.start()

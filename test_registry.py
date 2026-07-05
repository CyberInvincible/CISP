from core.plugin_loader import PluginLoader
from core.registry import PluginRegistry

loader = PluginLoader()
registry = PluginRegistry()

for plugin in loader.discover():
    registry.register(plugin)

print(f"Registered Plugins: {registry.count()}")

for plugin in registry.all():
    print(f"{plugin.name} ({plugin.category})")
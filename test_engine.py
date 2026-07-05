from core.engine import Engine
from core.plugin_loader import PluginLoader
from core.registry import PluginRegistry

loader = PluginLoader()
registry = PluginRegistry()

for plugin in loader.discover():
    registry.register(plugin)

engine = Engine(registry)

result = engine.execute("Test Plugin")

print(result)
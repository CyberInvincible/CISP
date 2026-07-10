from cisp.core.plugin_loader import PluginLoader
from cisp.core.registry import PluginRegistry
from cisp.core.engine import Engine

loader = PluginLoader()
plugins = loader.discover()

registry = PluginRegistry()

for plugin in plugins:
    registry.register(plugin)

engine = Engine(registry)

result = engine.execute(
    "SSL Scanner",
    "openai.com"
)

print(result)
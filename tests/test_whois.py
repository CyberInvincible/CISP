from cisp.core.engine import Engine
from cisp.core.plugin_loader import PluginLoader
from cisp.core.registry import PluginRegistry

loader = PluginLoader()
registry = PluginRegistry()

for plugin in loader.discover():
    registry.register(plugin)

engine = Engine(registry)

result = engine.execute("WHOIS Lookup", "openai.com")

print(result)
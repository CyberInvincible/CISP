from core.plugin_loader import PluginLoader

loader = PluginLoader()

plugins = loader.discover()

loader.list_plugins()
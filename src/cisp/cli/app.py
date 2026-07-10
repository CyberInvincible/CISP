"""
Main CLI application.

This class coordinates the startup of the CISP platform.
The CLI is only responsible for interacting with the user.
Business logic remains inside the Engine and Plugins.
"""

from cisp.cli.banner import show_banner
from cisp.cli.menu import MainMenu
from cisp.core.engine import Engine
from cisp.core.logger import Logger
from cisp.core.plugin_loader import PluginLoader
from cisp.core.registry import PluginRegistry


class CLIApplication:
    """
    Main CLI application.

    This class controls the complete lifecycle of the
    command-line interface.
    """

    def __init__(self) -> None:
        """Prepare all core platform components."""

        self.logger = Logger.get_logger()

        self.registry = PluginRegistry()

        self.loader = PluginLoader()

        # Create a single execution engine.
        self.engine = Engine(self.registry)

    def run(self) -> None:
        """
        Start the application.
        """

        self.logger.info("Starting CyberInvincible Security Platform...")

        # Discover every available plugin.
        plugins = self.loader.discover()

        print(f"\nDiscovered {len(plugins)} plugins\n")
        
        # Register every discovered plugin.
        for plugin in plugins:
            print(f"Registering: {plugin.name}")
            self.registry.register(plugin)

        print(f"\nRegistry contains {self.registry.count()} plugins\n")
        
        show_banner()

        menu = MainMenu(
            self.registry,
            self.engine,
        )

        menu.run()
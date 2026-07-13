"""
Main CLI application.

This class coordinates the startup of the CISP platform.
The CLI is only responsible for interacting with the user.
Business logic remains inside the Engine and Plugins.
"""

from cisp.cli.wizard import ScanWizard
from cisp.cli.profile_mapper import ProfileMapper

from cisp.pipelines.web import WebPipeline
from cisp.pipelines.infrastructure import InfrastructurePipeline
from cisp.pipelines.full import FullPipeline
from cisp.pipelines.recon import ReconPipeline
from cisp.pipelines.runner import PipelineRunner

from cisp.reporting.aggregator import ResultAggregator
from cisp.reporting.html_report import HTMLReport

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

        wizard = ScanWizard()

        selection = wizard.start()

        if selection is None:
            print("\nThank you for using CISP.")
            return

        profile = ProfileMapper.get_profile(
            selection["profile"]
        )

        target = selection["target"]

        if profile == "quick":
            pipeline = ReconPipeline(self.engine)

        elif profile == "web":
            pipeline = WebPipeline(self.engine)

        elif profile == "infrastructure":
            pipeline = InfrastructurePipeline(self.engine)

        elif profile == "full":
            pipeline = FullPipeline(self.engine)

        else:
            menu = MainMenu(
                self.registry,
                self.engine,
            )
            menu.run()
            return

        runner = PipelineRunner(pipeline)

        results = runner.run(target)

        aggregator = ResultAggregator()

        report = aggregator.aggregate(results)

        print("\nModules being sent to HTML Report:")

        for module in results:
            print("-", module)

        HTMLReport().generate(results)

        print("\nHTML report generated successfully.")
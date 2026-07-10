"""
===============================================================================
CISP (CyberInvincible Security Platform)

File:
    cli/menu.py

Purpose:
    Display the interactive command-line menu.

Why this file exists:
    The menu is the user's entry point into the platform.

The menu never executes plugins directly.
It only collects user input.

Execution is delegated to the Engine.
===============================================================================
"""

from __future__ import annotations

from cisp.core.registry import PluginRegistry

from cisp.core.engine import Engine


class MainMenu:
    """
    Interactive CLI menu.

    Displays every registered plugin and allows
    the user to choose one.
    """

    def __init__(self, registry: PluginRegistry, engine: Engine,) -> None:
        """
        Store the plugin registry.

        Parameters
        ----------
        registry:
            The central registry containing all plugins.
        """
        self.registry = registry
        self.engine = engine

    def run(self) -> None:
        """
        Display the menu until the user exits.
        """

        plugins = self.registry.list_plugins()

        if not plugins:
            print("\nNo plugins registered.\n")
            return

        while True:

            print("\n==============================")
            print(" Available Plugins")
            print("==============================\n")

            for index, plugin in enumerate(plugins, start=1):
                print(f"{index}. {plugin.name} ({plugin.category})")

            print("0. Exit")

            choice = input("\nSelect a plugin: ").strip()

            if choice == "0":
                print("\nThank you for using CISP.")
                break

            if not choice.isdigit():
                print("\nInvalid selection.")
                continue

            index = int(choice)

            if index < 1 or index > len(plugins):
                print("\nInvalid selection.")
                continue

            selected_plugin = plugins[index - 1]

            print(f"\nExecuting '{selected_plugin.name}'...\n")

            url = input("Target URL: ").strip()
            
            try:
                result = self.engine.execute(
                    selected_plugin.name,
                    url=url,
                )

                print("\nExecution Result")
                print("----------------")
                print(result)

            except Exception as error:
                print(f"\nExecution failed: {error}")

            # Engine execution will be added in the next sprint.
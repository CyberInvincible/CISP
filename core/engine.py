"""
===============================================================================
CISP (CyberInvincible Security Platform)

File:
    core/engine.py

Purpose:
    Executes CISP plugins.

Why this file exists:
    The Engine is responsible for running plugins.

    It does NOT discover plugins.
    It does NOT display results.

    It only executes plugins and returns their results.

Architecture:

    CLI / GUI / API
           │
           ▼
    Execution Engine
           │
           ▼
    Plugin Registry
           │
           ▼
         Plugin

Benefits:
    ✔ Single execution point
    ✔ Easy testing
    ✔ GUI ready
    ✔ API ready
    ✔ Future AI ready
===============================================================================
"""

from __future__ import annotations

from typing import Any

from core.registry import PluginRegistry


class Engine:
    """
    Central execution engine for CISP.

    The Engine retrieves plugins from the registry,
    creates an instance, executes it, and returns
    the result to the caller.
    """

    def __init__(self, registry: PluginRegistry):
        """
        Initialize the engine.

        Args:
            registry:
                Plugin registry containing all available plugins.
        """
        self.registry = registry

    def execute(self, plugin_name: str, *args: Any, **kwargs: Any) -> Any:
        """
        Execute a plugin by its registered name.

        Args:
            plugin_name:
                Human-readable plugin name.

            *args:
                Positional arguments forwarded to the plugin.

            **kwargs:
                Keyword arguments forwarded to the plugin.

        Returns:
            Whatever the plugin's run() method returns.

        Raises:
            ValueError:
                If the requested plugin does not exist.
        """

        plugin_class = self.registry.get(plugin_name)

        if plugin_class is None:
            raise ValueError(f"Plugin '{plugin_name}' was not found.")

        # Create a new plugin instance.
        plugin = plugin_class()

        # Execute the plugin.
        return plugin.run(*args, **kwargs)
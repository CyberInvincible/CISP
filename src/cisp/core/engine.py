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

from cisp.core.registry import PluginRegistry

from cisp.models import ModuleResult

from cisp.core.context import Context

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
        self.context = Context()

    def execute(self, plugin_name: str, *args: Any, **kwargs) -> ModuleResult:
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
            return ModuleResult(
                success=False,
                data={
                    "plugin": plugin_name,
                    "exception": "PluginNotFound",
                },
                message=f"Plugin '{plugin_name}' was not found.",
                warnings=[],
                errors=[f"Plugin '{plugin_name}' does not exist."],
            )

        plugin = plugin_class()

        try:
            return plugin.run(
                self.context,
                *args,
                **kwargs
            )

            # If the plugin already returned a ModuleResult,
            # pass it through unchanged.
            if isinstance(result, ModuleResult):
                return result

        except Exception as error:
            return ModuleResult(
                success=False,
                data={
                    "plugin": plugin_name,
                    "exception": type(error).__name__,
                },
                message="Plugin execution failed.",
                warnings=[],
                errors=[str(error)],
            )
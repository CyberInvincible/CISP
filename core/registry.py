"""
===============================================================================
CISP (CyberInvincible Security Platform)

File:
    core/registry.py

Purpose:
    Stores and manages all discovered CISP plugins.

Why this file exists:
    The Plugin Loader is responsible for DISCOVERING plugins.

    The Registry is responsible for STORING plugins.

Architecture:

        Plugin Loader
              │
              ▼
        Plugin Registry
              │
              ▼
        Execution Engine

Benefits:
    ✔ Single source of truth
    ✔ Fast plugin lookup
    ✔ Cleaner architecture
    ✔ Easy filtering by category
===============================================================================
"""

from __future__ import annotations

from typing import Type

from core.base_module import BaseModule


class PluginRegistry:
    """
    Stores every discovered plugin.

    Other parts of CISP (CLI, Engine, GUI)
    should interact with this registry instead
    of directly using the Plugin Loader.
    """

    def __init__(self):
        """Create an empty plugin registry."""
        self._plugins: dict[str, Type[BaseModule]] = {}

    def register(self, plugin: Type[BaseModule]) -> None:
        """
        Register a plugin class.

        Parameters
        ----------
        plugin:
            A class that inherits from BaseModule.
        """
        self._plugins[plugin.name] = plugin

    def get(self, name: str) -> Type[BaseModule] | None:
        """
        Retrieve a plugin by its name.

        Returns
        -------
        BaseModule class or None
        """
        return self._plugins.get(name)

    def all(self) -> list[Type[BaseModule]]:
        """
        Return all registered plugins.
        """
        return list(self._plugins.values())

    def categories(self) -> list[str]:
        """
        Return a sorted list of available categories.
        """
        return sorted({plugin.category for plugin in self._plugins.values()})

    def plugins_by_category(self, category: str) -> list[Type[BaseModule]]:
        """
        Return every plugin that belongs to a category.
        """
        return [
            plugin
            for plugin in self._plugins.values()
            if plugin.category.lower() == category.lower()
        ]

    def count(self) -> int:
        """
        Return the number of registered plugins.
        """
        return len(self._plugins)
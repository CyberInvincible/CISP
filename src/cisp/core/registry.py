"""
===============================================================================
CISP (CyberInvincible Security Platform)

Plugin Registry

Responsible for storing every discovered plugin.

The registry acts as the single source of truth for every loaded plugin.
===============================================================================
"""

from __future__ import annotations

from typing import Type

from cisp.core.base_module import BaseModule


class PluginRegistry:
    """
    Stores every discovered plugin.

    Other parts of CISP should interact with the registry instead
    of directly using the Plugin Loader.
    """

    def __init__(self) -> None:
        """Create an empty registry."""
        self._plugins: dict[str, Type[BaseModule]] = {}

    def register(self, plugin: Type[BaseModule]) -> None:
        """
        Register a plugin.

        If another plugin with the same name exists,
        it will be replaced.
        """
        self._plugins[plugin.name] = plugin

    def unregister(self, name: str) -> None:
        """Remove a plugin if it exists."""
        self._plugins.pop(name, None)

    def get(self, name: str) -> Type[BaseModule] | None:
        """Return a plugin by name."""
        return self._plugins.get(name)

    def get_plugin(self, name: str) -> Type[BaseModule] | None:
        """
        Alias for get().

        This name is easier to understand when reading
        application code.
        """
        return self.get(name)

    def all(self) -> list[Type[BaseModule]]:
        """Return every registered plugin."""
        return list(self._plugins.values())

    def list_plugins(self) -> list[Type[BaseModule]]:
        """
        Alias for all().

        Used by the CLI and future GUI.
        """
        return self.all()

    def has_plugin(self, name: str) -> bool:
        """Return True if a plugin exists."""
        return name in self._plugins

    def clear(self) -> None:
        """Remove every registered plugin."""
        self._plugins.clear()

    def count(self) -> int:
        """Return the number of registered plugins."""
        return len(self._plugins)

    def categories(self) -> list[str]:
        """Return all available categories."""
        return sorted(
            {
                plugin.category
                for plugin in self._plugins.values()
            }
        )

    def plugins_by_category(
        self,
        category: str
    ) -> list[Type[BaseModule]]:
        """Return plugins belonging to a category."""
        return [
            plugin
            for plugin in self._plugins.values()
            if plugin.category.lower() == category.lower()
        ]
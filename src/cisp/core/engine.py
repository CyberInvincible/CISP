from __future__ import annotations

from typing import Any

from cisp.core.context import Context
from cisp.core.registry import PluginRegistry
from cisp.models import ModuleResult


class Engine:
    """
    Central execution engine for CISP.
    """

    def __init__(self, registry: PluginRegistry):
        self.registry = registry
        self.context = Context()

    def execute(
        self,
        plugin_name: str,
        *args: Any,
        **kwargs: Any,
    ) -> ModuleResult:

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
                errors=[
                    f"Plugin '{plugin_name}' does not exist."
                ],
            )

        plugin = plugin_class()

        try:
            return plugin.run(
                self.context,
                *args,
                **kwargs,
            )

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
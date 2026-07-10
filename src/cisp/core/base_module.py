"""
===============================================================================
CISP (CyberInvincible Security Platform)

File:
    core/base_module.py

Purpose:
    Defines the abstract base class for every CISP plugin.

Architecture:
    Every plugin follows the same lifecycle.

        run()
          │
          ├── validate()
          ├── execute()
          ├── measure execution time
          ├── handle exceptions
          └── return ModuleResult

Benefits:
    ✔ Less duplicate code
    ✔ Consistent behaviour
    ✔ Easier testing
    ✔ Production ready
===============================================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from time import perf_counter
from typing import Any

from cisp.models import ModuleResult

from cisp.core.context import Context


class BaseModule(ABC):
    """
    Base class for every CISP plugin.

    Plugin developers should ONLY implement:

        validate()
        execute()

    The framework takes care of everything else.
    """

    # -------------------------------------------------------------------------
    # Module Metadata
    #
    # Child classes should override these values.
    #
    # These fields are used by:
    #
    # • CLI
    # • Reporting
    # • Dashboard
    # • Scheduler
    # • REST API
    # • Module Registry
    # -------------------------------------------------------------------------

    name: str = "Unnamed Plugin"
    slug: str = "unnamed"
    description: str = ""
    category: str = "General"
    version: str = "0.1.0"
    author: str = "CISP"

    tags: list[str] = []

    dependencies: list[str] = []

    default_config: dict[str, Any] = {}

    # -------------------------------------------------------------------------

    def validate(
        self,
        context: Context,
        *args: Any,
        **kwargs: Any
    ) -> None:
        """
        Validate user input.

        Override this if your plugin needs validation.

        Raise:
            ValueError
            TypeError
            etc.
        """
        return

    # -------------------------------------------------------------------------

    @abstractmethod
    def execute(
        self,
        context: Context,
        *args: Any,
        **kwargs: Any
    ) -> Any:
        """
        Plugin-specific business logic.

        Every plugin MUST implement this method.
        """
        raise NotImplementedError

    # -------------------------------------------------------------------------

    def run(
        self,
        context: Context,
        *args: Any,
        **kwargs: Any
    ) -> ModuleResult:
        """
        Standard execution lifecycle.

        This method should NEVER be overridden by plugins.
        """

        start = perf_counter()

        try:
            # Step 1: Validate input
            self.validate(
                context,
                *args,
                **kwargs
            )

            # Step 2: Execute plugin logic
            data = self.execute(
                context,
                *args,
                **kwargs
            )

            end = perf_counter()

            # If plugin already returned ModuleResult, just update timing.
            if isinstance(data, ModuleResult):
                data.execution_time = end - start
                return data

            # Wrap legacy return values.
            return ModuleResult(
                success=True,
                data=data,
                message=f"{self.name} completed successfully.",
                execution_time=end - start,
            )

        except Exception as error:
            end = perf_counter()

            return ModuleResult(
                success=False,
                message=f"{self.name} failed.",
                errors=[str(error)],
                execution_time=end - start,
            )
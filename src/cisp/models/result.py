"""
===============================================================================
CISP (CyberInvincible Security Platform)

File:
    models/result.py

Purpose:
    Defines the standard result returned by every CISP plugin.

Why this file exists:
    Every plugin should return the same result structure.

Benefits:
    ✔ Consistent output
    ✔ Easier reporting
    ✔ GUI ready
    ✔ REST API ready
    ✔ AI ready
===============================================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, UTC
from typing import Any


@dataclass(slots=True)
class ModuleResult:
    """
    Standard result returned by every CISP plugin.
    """

    # Whether the plugin completed successfully.
    success: bool

    # Stable module identifier.
    module: str = ""

    # Human-readable module name.
    module_name: str = ""

    # Main data produced by the plugin.
    data: Any = None

    # Human-readable message.
    message: str = ""

    # Non-fatal issues encountered during execution.
    warnings: list[str] = field(default_factory=list)

    # Fatal errors encountered during execution.
    errors: list[str] = field(default_factory=list)

    # Time taken to execute the plugin (seconds).
    execution_time: float = 0.0

    # Time when the result was created.
    timestamp: datetime = field(default_factory=lambda: datetime.now(UTC))

    # Additional module-specific metadata.
    metadata: dict[str, Any] = field(default_factory=dict)

    def has_warnings(self) -> bool:
        """Return True if warnings are present."""
        return bool(self.warnings)

    def has_errors(self) -> bool:
        """Return True if errors are present."""
        return bool(self.errors)

    @property
    def failed(self) -> bool:
        """Return True if the module execution failed."""
        return not self.success
"""
===============================================================================
CISP Core Models
===============================================================================
"""

from dataclasses import dataclass, field
from typing import Any

from cisp.core.finding import Finding


@dataclass
class ModuleResult:
    """
    Standard result returned by every CISP plugin.
    """

    success: bool

    data: Any = None

    findings: list[Finding] = field(default_factory=list)

    message: str = ""

    warnings: list[str] = field(default_factory=list)

    errors: list[str] = field(default_factory=list)

    execution_time: float = 0.0
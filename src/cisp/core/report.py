from dataclasses import dataclass, field
from typing import Any


@dataclass
class ScanReport:
    """
    Represents a complete CISP scan.
    """

    target: str

    success: bool = True

    modules: dict[str, Any] = field(default_factory=dict)

    summary: dict[str, Any] = field(default_factory=dict)

    findings: list[dict] = field(default_factory=list)

    metadata: dict[str, Any] = field(default_factory=dict)
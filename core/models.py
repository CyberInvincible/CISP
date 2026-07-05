"""
===============================================================================
CISP (CyberInvincible Security Platform)

File: core/models.py

Purpose:
    Defines the core data models used across CISP.

Why this file exists:
    Security modules should NOT print results directly.

    Instead, they should return structured objects.

    These objects can later be displayed in:

        • CLI
        • Desktop GUI
        • Web Dashboard
        • REST API
        • PDF Reports
        • JSON Export
        • AI Analysis

Benefits:
    ✔ Consistent data
    ✔ Easier testing
    ✔ Better scalability
    ✔ Cleaner architecture
===============================================================================
"""

from dataclasses import dataclass, field
from typing import List


# =============================================================================
# FINDING
# =============================================================================

@dataclass
class Finding:
    """
    Represents a single security finding.

    Example:

        Open Port
        Missing Security Header
        Weak TLS Version
        Exposed Directory
    """

    title: str
    severity: str
    description: str
    evidence: str


# =============================================================================
# SCAN RESULT
# =============================================================================

@dataclass
class ScanResult:
    """
    Represents the complete output of a module.

    Every module should return ONE ScanResult object.
    """

    target: str
    module: str
    success: bool

    findings: List[Finding] = field(default_factory=list)

    execution_time: float = 0.0
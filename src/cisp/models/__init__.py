"""
Data models used throughout CISP.

Models define the common data structures shared between
the CLI, Engine, Plugins, Reporting, GUI and future APIs.
"""

from .result import ModuleResult

__all__ = ["ModuleResult"]
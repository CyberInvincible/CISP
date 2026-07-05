"""
===============================================================================
CISP (CyberInvincible Security Platform)

File: core/base_module.py

Purpose:
    Defines the BaseModule abstract class that every CISP module must inherit.

Why this file exists:
    The CISP Engine should not know how individual modules work.

    Whether it is:

        • WHOIS Lookup
        • DNS Lookup
        • Port Scanner
        • Banner Grabber
        • Future AI Scanner

    every module should expose the SAME interface.

    This allows the engine to execute any module without writing
    module-specific code.

Benefits:
    ✔ Standardized architecture
    ✔ Plugin-based design
    ✔ Easier testing
    ✔ Automatic module discovery
    ✔ Future GUI compatibility
    ✔ Future REST API compatibility
    ✔ Better scalability
    ✔ Easier community contributions

Author:
    CISP Team

Version:
    0.1.0
===============================================================================
"""

# =============================================================================
# IMPORTS
# =============================================================================

# ABC (Abstract Base Class)
#
# Think of an abstract class as a blueprint.
#
# It defines what every CISP module MUST contain,
# but it is never executed directly.
from abc import ABC, abstractmethod

# "Any" allows a function to accept or return any Python object.
#
# Later in the project, most return types will become strongly typed
# using ScanResult and other models.
from typing import Any


# =============================================================================
# BASE MODULE
# =============================================================================

class BaseModule(ABC):
    """
    Base class for every CISP module.

    Every module in CISP MUST inherit from this class.

    Responsibilities
    ----------------
    • Store module metadata
    • Define a common execution interface
    • Ensure consistency across all plugins
    • Make automatic plugin discovery possible

    Example
    -------
        class WhoisModule(BaseModule):

            name = "WHOIS Lookup"

            def run(self, target):
                ...

    Why use inheritance?
    --------------------
    Without a common base class:

        WHOIS.execute()

        DNS.lookup()

        PortScanner.start()

    Every module would have different method names.

    The engine would become difficult to maintain.

    With BaseModule:

        module.run(...)

    The engine can execute every module the same way.
    """

    # =========================================================================
    # REQUIRED MODULE METADATA
    # =========================================================================
    #
    # These fields describe the module.
    #
    # They are displayed in:
    #
    #   • CLI
    #   • Desktop GUI
    #   • Reports
    #   • Plugin Loader
    #   • Future Marketplace
    #

    # Human-readable module name.
    name: str = "Unnamed Module"

    # Short explanation of what the module does.
    description: str = "No description provided."

    # Module developer.
    author: str = "CISP Team"

    # Module version.
    version: str = "0.1.0"

    # Module category.
    #
    # Examples:
    #   Recon
    #   Network
    #   Web
    #   Cloud
    #   Active Directory
    category: str = "General"

    # =========================================================================
    # OPTIONAL MODULE METADATA
    # =========================================================================

    # Search keywords used by the plugin loader and future GUI.
    #
    # Example:
    #
    # tags = ["dns", "recon", "network"]
    tags: list[str] = []

    # Operating systems officially supported by the module.
    supported_platforms: list[str] = [
        "Windows",
        "Linux",
        "macOS"
    ]

    # Does the module require Internet or network connectivity?
    requires_network: bool = False

    # Can this module currently be executed?
    #
    # Future Community / Pro editions may disable certain modules.
    enabled: bool = True

    # Minimum supported Python version.
    min_python: tuple[int, int] = (3, 12)

    # Module license.
    license: str = "MIT"

    # Documentation or project page.
    homepage: str = ""

    # =========================================================================
    # MODULE EXECUTION
    # =========================================================================

    @abstractmethod
    def run(self, *args: Any, **kwargs: Any) -> Any:
        """
        Execute the module.

        Parameters
        ----------
        *args
            Positional arguments required by the module.

        **kwargs
            Optional keyword arguments.

        Returns
        -------
        Any

            Current Version:
                Any Python object.

            Future Version:
                ScanResult

        Notes
        -----
        Every child class MUST implement this method.

        The CISP Engine simply calls:

            module.run(...)

        without knowing anything about the module's internal logic.

        This principle is called abstraction and is one of the key
        reasons CISP can support hundreds of modules without changing
        the engine.
        """

        raise NotImplementedError(
            "Every CISP module must implement the 'run()' method."
        )
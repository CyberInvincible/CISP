"""
===============================================================================
CISP (CyberInvincible Security Platform)

File:
    core/plugin_loader.py

Purpose:
    Automatically discover and load CISP modules.

Why this file exists:
    Imagine CISP has 500 security modules.

    We DO NOT want to manually import every module.

    Instead, this loader automatically discovers modules
    that inherit from BaseModule.

How it works:

        modules/
            recon/
                whois/
                    module.py

↓

        Plugin Loader

↓

        Imports module automatically

↓

        Checks if it inherits BaseModule

↓

        Registers it

↓

        Engine can execute it

Benefits:

    ✔ No manual imports
    ✔ Easy plugin development
    ✔ Community plugins
    ✔ Future marketplace support
    ✔ Scalable architecture
===============================================================================
"""

from __future__ import annotations

# =============================================================================
# IMPORTS
# =============================================================================

import importlib
import inspect
import pkgutil
from pathlib import Path

from cisp.core.base_module import BaseModule


# =============================================================================
# PLUGIN LOADER
# =============================================================================

class PluginLoader:
    """ 
    Responsible for discovering CISP plugins.

    The loader searches inside the "modules" package,
    imports every module automatically,
    and returns every valid BaseModule class.
    """

    def __init__(self, package_name: str = "cisp.modules"):
        """
        Parameters
        ----------
        package_name:
            Root package that contains all CISP plugins.
        """
        self.package_name = package_name
        self.plugins = []

    # -------------------------------------------------------------------------
    # Discover Plugins
    # -------------------------------------------------------------------------

    def discover(self):
        """
        Search the modules package recursively.

        Returns
        -------
        list
            List of discovered plugin classes.
        """

        self.plugins.clear()

        package = importlib.import_module(self.package_name)

        IGNORE_PACKAGES = {
            "__pycache__",
            "whois_old",
            "old",
            "backup",
            "archive",
        }

        for _, module_name, _ in pkgutil.walk_packages(
            package.__path__,
            package.__name__ + "."
        ):

            # Ignore backup/archive folders.
            if any(
                part in IGNORE_PACKAGES
                for part in module_name.split(".")
            ):
                continue

            try:
                module = importlib.import_module(module_name)

            except Exception as e:
                import traceback

                print(f"[ERROR] Failed to import {module_name}")
                traceback.print_exc()

                continue

            for _, obj in inspect.getmembers(module, inspect.isclass):

                # Only consider classes defined in THIS module.
                if obj.__module__ != module.__name__:
                    continue

                # Must inherit from BaseModule.
                if not issubclass(obj, BaseModule):
                    continue

                # Ignore BaseModule itself.
                if obj is BaseModule:
                    continue

                # Prevent duplicate plugins.
                if obj in self.plugins:
                    continue

                print(
                    f"Loaded: {obj.__name__} | "
                    f"Abstract: {obj.__abstractmethods__}"
                )

                self.plugins.append(obj)

        return self.plugins
    # -------------------------------------------------------------------------
    # Display Plugins
    # -------------------------------------------------------------------------

    def list_plugins(self):
        """
        Print all discovered plugins.
        """

        if not self.plugins:

            print("No plugins loaded.")

            return

        print("\nLoaded Plugins\n")

        for plugin in self.plugins:

            print(
                f"- {plugin.name} "
                f"({plugin.category}) "
                f"v{plugin.version}"
            )
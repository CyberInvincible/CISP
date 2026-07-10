"""
===============================================================================
CISP (CyberInvincible Security Platform)

File:
    config/profile_manager.py

Purpose:
    Load and manage scan profiles.
===============================================================================
"""

from __future__ import annotations

from pathlib import Path

import yaml


class ProfileManager:
    """
    Loads scan profiles from YAML.
    """

    def __init__(self):

        config_file = (
            Path(__file__).parent
            / "scan_profiles.yaml"
        )

        with config_file.open(
            "r",
            encoding="utf-8"
        ) as file:

            self.profiles = yaml.safe_load(file)

    def names(self):

        return list(self.profiles.keys())

    def exists(self, profile: str):

        return profile in self.profiles

    def modules(self, profile: str):

        return self.profiles[profile]["modules"]

    def description(self, profile: str):

        return self.profiles[profile]["description"]
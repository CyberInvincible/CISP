"""
===============================================================================
CISP (CyberInvincible Security Platform)

File:
    core/context.py

Purpose:
    Shared runtime context passed to every plugin.

Why?

Instead of every plugin creating its own logger,
loading config, creating folders, etc.,
the framework provides one shared Context.

Benefits:
    ✔ Single source of truth
    ✔ Easier testing
    ✔ GUI/API ready
    ✔ Future AI ready
===============================================================================
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from cisp.core.logger import Logger


class Context:
    """
    Shared runtime context for every plugin.
    """

    def __init__(self):

        self.data = {}

    def set(self, key, value):

        self.data[key] = value

    def get(self, key, default=None):

        return self.data.get(key, default)

    def has(self, key):

        return key in self.data

    def remove(self, key):

        self.data.pop(key, None)

    def clear(self):

        self.data.clear()

    def all(self):

        return self.data
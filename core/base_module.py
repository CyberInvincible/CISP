from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class BaseModule(ABC):
    """
    Base class for every CISP module.

    Every security module must inherit from this class.
    """

    # Metadata
    name: str = "Unnamed Module"
    description: str = ""
    author: str = "CISP Team"
    version: str = "0.1.0"
    category: str = "General"

    @abstractmethod
    def run(self, *args: Any, **kwargs: Any) -> Any:
        """
        Execute the module.

        Returns:
            Structured result object.
        """
        raise NotImplementedError
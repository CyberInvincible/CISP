"""
===============================================================================
CISP (CyberInvincible Security Platform)

File:
    core/logger.py

Purpose:
    Centralized logging for the entire CISP platform.

Why this file exists:
    Every part of CISP should use the SAME logger.

Benefits:
    ✔ Consistent logging
    ✔ Console + file logging
    ✔ Easier debugging
    ✔ Future SIEM integration
===============================================================================
"""

from __future__ import annotations

import logging
from pathlib import Path


class Logger:
    """
    Creates and manages the CISP logger.

    This class ensures the logger is configured only once.
    """

    _logger = None

    @classmethod
    def get_logger(cls) -> logging.Logger:
        """
        Return the shared CISP logger.

        If it doesn't exist yet, create and configure it.
        """

        if cls._logger is not None:
            return cls._logger

        # ---------------------------------------------------------------------
        # Create logs directory if it doesn't already exist.
        # ---------------------------------------------------------------------
        log_directory = Path("logs")
        log_directory.mkdir(exist_ok=True)

        log_file = log_directory / "cisp.log"

        # ---------------------------------------------------------------------
        # Create the logger.
        # ---------------------------------------------------------------------
        logger = logging.getLogger("CISP")

        logger.setLevel(logging.INFO)

        # Prevent duplicate handlers if called multiple times.
        if logger.handlers:
            cls._logger = logger
            return logger

        # ---------------------------------------------------------------------
        # Log message format.
        # ---------------------------------------------------------------------
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        # Console output.
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        # File output.
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

        cls._logger = logger

        return logger
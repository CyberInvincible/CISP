"""
===============================================================================
CISP (CyberInvincible Security Platform)

File:
    pipelines/web.py

Purpose:
    Execute the complete Web Security Scan profile.
===============================================================================
"""

from __future__ import annotations

from cisp.core.target import Target

from cisp.core.engine import Engine
from cisp.core.execution_manager import ExecutionManager


class WebPipeline:
    """
    Executes every module included in the Web Security Scan profile.
    """

    def __init__(self, engine: Engine):
        self.execution_manager = ExecutionManager(engine)

    def execute(self, url: str):

        tasks = [

            ("WHOIS Lookup", (url,)),

            ("DNS Lookup", (url,)),

            ("SSL Scanner", (url,)),

            ("HTTP Methods Scanner", (url,)),

            ("Security Headers Analyzer", (url,)),

            ("Technology Detection", (url,)),

            ("Directory Bruteforcer", (url,)),

            ("Robots Analyzer", (url,)),

            ("Vulnerability Analyzer", (url,)),

        ]

        return self.execution_manager.execute(tasks)
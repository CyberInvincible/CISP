"""
===============================================================================
CISP (CyberInvincible Security Platform)

File:
    pipelines/recon.py

Purpose:
    Executes the standard reconnaissance workflow.

Version:
    1.0.0
===============================================================================
"""

from __future__ import annotations

from cisp.core.engine import Engine


class ReconPipeline:
    """
    Standard reconnaissance pipeline.
    """

    PIPELINE = [
        ("WHOIS Lookup", {"domain": True}),
        ("DNS Lookup", {"domain": True}),
        ("SSL Scanner", {"url": True}),
        ("HTTP Methods Scanner", {"url": True}),
        ("Security Headers Analyzer", {"url": True}),
        ("Technology Detection", {"url": True}),
        ("Robots Analyzer", {"url": True}),
        ("Directory Bruteforcer", {"url": True}),
    ]

    def __init__(self, engine: Engine):
        self.engine = engine

    def execute(self, target: str):

        results = {}

        for plugin_name, options in self.PIPELINE:

            try:

                if options.get("url"):

                    result = self.engine.execute(
                        plugin_name,
                        url=target,
                    )

                elif options.get("domain"):

                    result = self.engine.execute(
                        plugin_name,
                        target,
                    )

                else:

                    result = self.engine.execute(
                        plugin_name,
                    )

            except Exception as error:

                result = {
                    "success": False,
                    "error": str(error),
                }

            results[plugin_name] = result

        return results
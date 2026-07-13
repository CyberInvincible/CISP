"""
Infrastructure Scan Pipeline
"""

from __future__ import annotations

from cisp.core.engine import Engine


class InfrastructurePipeline:

    def __init__(self, engine: Engine):
        self.engine = engine

    def execute(self, target: str):

        results = {}

        results["Port Scanner"] = self.engine.execute(
            "Port Scanner",
            target,
            1,
            1000,
        )

        results["Banner Grabber"] = self.engine.execute(
            "Banner Grabber",
            target,
        )

        results["SSL Scanner"] = self.engine.execute(
            "SSL Scanner",
            target,
        )

        return results
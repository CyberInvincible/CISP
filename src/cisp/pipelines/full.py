"""
Full Scan Pipeline
"""

from __future__ import annotations

from cisp.pipelines.web import WebPipeline
from cisp.pipelines.infrastructure import InfrastructurePipeline


class FullPipeline:

    def __init__(self, engine):
        self.web = WebPipeline(engine)
        self.infrastructure = InfrastructurePipeline(engine)

    def execute(self, target):

        results = {}

        results.update(
            self.web.execute(target)
        )

        results.update(
            self.infrastructure.execute(target)
        )

        return results
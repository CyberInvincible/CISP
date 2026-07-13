"""
===============================================================================
CISP (CyberInvincible Security Platform)

File:
    pipelines/runner.py

Purpose:
    Execute complete scan pipelines and provide a unified
    execution interface for the CLI, GUI and REST API.
===============================================================================
"""

from __future__ import annotations

from time import perf_counter


class PipelineRunner:
    """
    Executes a complete scan pipeline.
    """

    def __init__(self, pipeline):
        self.pipeline = pipeline

    def run(self, target: str):

        print("\n===================================")
        print(" Starting Scan")
        print("===================================\n")

        start = perf_counter()

        results = self.pipeline.execute(target)

        end = perf_counter()

        successful = sum(
            1 for result in results.values()
            if result.success
        )

        failed = len(results) - successful

        print("\n===================================")
        print(" Scan Completed")
        print("===================================")

        print(f"Modules Executed : {len(results)}")
        print(f"Successful       : {successful}")
        print(f"Failed           : {failed}")
        print(f"Execution Time   : {end-start:.2f} sec")

        return results
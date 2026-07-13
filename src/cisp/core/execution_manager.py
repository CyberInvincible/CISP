"""
===============================================================================
CISP (CyberInvincible Security Platform)

File:
    core/execution_manager.py

Purpose:
    Execute multiple CISP plugins in a consistent way.

Why this file exists:

Instead of every pipeline manually calling:

    engine.execute(...)
    engine.execute(...)
    engine.execute(...)

the Execution Manager handles all execution.

Future capabilities:

    ✓ Progress tracking
    ✓ Parallel execution
    ✓ Retry failed modules
    ✓ Timeouts
    ✓ Scan cancellation
    ✓ Metrics
===============================================================================
"""

from __future__ import annotations

from time import perf_counter

from cisp.core.engine import Engine


class ExecutionManager:
    """
    Executes a collection of scan tasks.
    """

    def __init__(self, engine: Engine):
        self.engine = engine

    def execute(self, tasks: list[tuple[str, tuple]]) -> dict:
        """
        Execute every task sequentially.

        Parameters
        ----------
        tasks

            Example:

            [
                ("WHOIS Lookup", ("google.com",)),
                ("DNS Lookup", ("google.com",)),
            ]

        Returns
        -------
        dict
            Dictionary of ModuleResult objects.
        """

        results = {}

        total = len(tasks)

        print()

        for index, (plugin_name, arguments) in enumerate(tasks, start=1):

            print(f"[{index}/{total}] Running {plugin_name:<32}", end="")

            start = perf_counter()

            result = self.engine.execute(
                plugin_name,
                *arguments
            )

            if result is None:
                print(f"\n[DEBUG] Engine returned None for plugin: {plugin_name}")
                continue

            end = perf_counter()

            result.execution_time = end - start

            if result.success:
                print(f"✓ {result.execution_time:.2f} sec")
            else:
                print(f"✗ {result.execution_time:.2f} sec")

                if result.errors:
                    print(f"      Reason: {result.errors[0]}")

            results[plugin_name] = result

        return results
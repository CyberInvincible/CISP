"""
===============================================================================
CISP (CyberInvincible Security Platform)

File:
    reporting/aggregator.py

Purpose:
    Combine multiple ModuleResult objects into a single report.
===============================================================================
"""

from __future__ import annotations

from cisp.models import ModuleResult


class ResultAggregator:
    """
    Aggregates multiple ModuleResult objects into a
    single dictionary that can be consumed by HTML,
    JSON, PDF, REST API and future dashboards.
    """

    def aggregate(
        self,
        results: dict[str, ModuleResult]
    ) -> dict:

        report = {
            "success": True,
            "modules": {},
            "summary": {
                "total_modules": 0,
                "successful": 0,
                "failed": 0,
                "execution_time": 0.0,
            },
        }

        for module_name, result in results.items():

            report["modules"][module_name] = {
                "success": result.success,
                "message": result.message,
                "data": result.data,
                "warnings": result.warnings,
                "errors": result.errors,
                "execution_time": result.execution_time,
                "timestamp": result.timestamp.isoformat(),
            }

            report["summary"]["total_modules"] += 1
            report["summary"]["execution_time"] += (
                result.execution_time
            )

            if result.success:
                report["summary"]["successful"] += 1
            else:
                report["summary"]["failed"] += 1
                report["success"] = False

        return report
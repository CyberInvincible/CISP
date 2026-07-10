import json
from pathlib import Path


class JSONReportGenerator:
    """
    Export scan reports as JSON.
    """

    def generate(self, report: dict, filename: str = "report.json"):

        output = Path(filename)

        with output.open("w", encoding="utf-8") as file:
            json.dump(report, file, indent=4)

        return output
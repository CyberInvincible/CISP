from dataclasses import dataclass

from cisp.core.severity import Severity


@dataclass
class Risk:
    """
    Risk information for a finding.
    """

    severity: Severity
    cvss: float = 0.0
    exploitability: str = "Unknown"
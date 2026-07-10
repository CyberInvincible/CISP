from dataclasses import dataclass


@dataclass
class Evidence:
    """
    Evidence supporting a finding.
    """

    description: str
    value: str = ""
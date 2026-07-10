from dataclasses import dataclass, field

from cisp.core.evidence import Evidence
from cisp.core.risk import Risk


@dataclass
class Finding:
    """
    Standard finding object used by every CISP plugin.
    """

    id: str

    title: str

    description: str

    asset: str

    risk: Risk

    evidence: list[Evidence] = field(default_factory=list)

    remediation: str = ""

    references: list[str] = field(default_factory=list)

    cwe: str = ""

    owasp: str = ""

    mitre: str = ""
from __future__ import annotations

import dns.resolver

from cisp.core.base_module import BaseModule


class DNSLookupPlugin(BaseModule):
    """
    Perform DNS reconnaissance.
    """

    name = "DNS Lookup"
    description = "Retrieve DNS records for a domain."
    category = "Reconnaissance"
    version = "1.0.0"
    author = "CISP"

    def validate(self, context, domain: str) -> None:
        if not domain:
            raise ValueError("Domain cannot be empty.")

        if "." not in domain:
            raise ValueError("Invalid domain.")

    def execute(self, context, domain: str):
        return {
            "A": self.lookup(domain, "A"),
            "AAAA": self.lookup(domain, "AAAA"),
            "MX": self.lookup(domain, "MX"),
            "NS": self.lookup(domain, "NS"),
            "TXT": self.lookup(domain, "TXT"),
            "CNAME": self.lookup(domain, "CNAME"),
            "SOA": self.lookup(domain, "SOA"),
        }

    @staticmethod
    def lookup(domain: str, record_type: str):
        try:
            answers = dns.resolver.resolve(domain, record_type)
            return [str(answer) for answer in answers]
        except Exception:
            return []
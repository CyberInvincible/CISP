"""
===============================================================================
CISP (CyberInvincible Security Platform)

WHOIS Plugin

Purpose:
    Retrieve WHOIS information for a domain.

This plugin demonstrates the standard CISP plugin lifecycle.
===============================================================================
"""

from __future__ import annotations

import whois

from cisp.core.base_module import BaseModule


class WhoisPlugin(BaseModule):
    """
    Production WHOIS plugin.
    """

    name = "WHOIS Lookup"
    description = "Retrieve WHOIS information for a domain."
    category = "Reconnaissance"
    version = "1.0.0"
    author = "CISP"

    def validate(self, context, domain: str) -> None:
        """
        Validate user input.
        """

        if not domain:
            raise ValueError("Domain cannot be empty.")

        if "." not in domain:
            raise ValueError("Invalid domain.")

    def execute(self, context, domain: str):
        """
        Execute WHOIS lookup.
        """

        result = whois.whois(domain)

        return {
            "domain": result.domain_name,
            "registrar": result.registrar,
            "creation_date": str(result.creation_date),
            "expiration_date": str(result.expiration_date),
            "updated_date": str(result.updated_date),
            "name_servers": result.name_servers,
            "emails": result.emails,
        }
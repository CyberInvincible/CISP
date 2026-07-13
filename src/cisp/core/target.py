"""
===============================================================================
CISP (CyberInvincible Security Platform)

File:
    core/target.py

Purpose:
    Normalize and represent scan targets.

Supported inputs:

    google.com
    https://google.com
    http://google.com
    192.168.1.10

===============================================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from ipaddress import ip_address
from urllib.parse import urlparse


@dataclass(slots=True)
class Target:

    original: str

    hostname: str

    url: str

    scheme: str

    port: int

    is_ip: bool

    is_domain: bool

    @classmethod
    def parse(cls, target: str):

        target = target.strip()

        if not target:
            raise ValueError("Target cannot be empty.")

        # Automatically assume HTTPS
        if not target.startswith(("http://", "https://")):
            url = "https://" + target
        else:
            url = target

        parsed = urlparse(url)

        hostname = parsed.hostname

        if hostname is None:
            raise ValueError("Invalid target.")

        try:
            ip_address(hostname)
            is_ip = True
        except ValueError:
            is_ip = False

        return cls(
            original=target,
            hostname=hostname,
            url=url,
            scheme=parsed.scheme,
            port=parsed.port or (
                443 if parsed.scheme == "https" else 80
            ),
            is_ip=is_ip,
            is_domain=not is_ip,
        )
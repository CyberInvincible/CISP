from __future__ import annotations

import socket
import ssl
from datetime import datetime, UTC

from cisp.core.base_module import BaseModule


class SSLScannerPlugin(BaseModule):

    name = "SSL Scanner"
    description = "Collect SSL/TLS certificate information."
    category = "Network Security"
    version = "1.0.0"
    author = "CISP"

    def validate(self, context, host):

        if not host:
            raise ValueError("Host cannot be empty.")

    def execute(self, context, host: str):

        port = 443

        ssl_context = ssl.create_default_context()

        with socket.create_connection((host, port), timeout=5) as sock:

            with ssl_context.wrap_socket(
                sock,
                server_hostname=host
            ) as secure_sock:

                cert = secure_sock.getpeercert()

                subject = dict(x[0] for x in cert["subject"])
                issuer = dict(x[0] for x in cert["issuer"])

                not_before = cert["notBefore"]
                not_after = cert["notAfter"]

                start = datetime.strptime(
                    not_before,
                    "%b %d %H:%M:%S %Y %Z"
                )

                end = datetime.strptime(
                    not_after,
                    "%b %d %H:%M:%S %Y %Z"
                )

                now = datetime.now(UTC)

                # If the certificate date is timezone-naive, make it UTC-aware.
                if end.tzinfo is None:
                    end = end.replace(tzinfo=UTC)

                days_remaining = (end - now).days

                return {

                    "host": host,

                    "tls_version": secure_sock.version(),

                    "cipher": secure_sock.cipher(),

                    "subject": subject,

                    "issuer": issuer,

                    "valid_from": start.isoformat(),

                    "valid_until": end.isoformat(),

                    "days_remaining": days_remaining,
                }
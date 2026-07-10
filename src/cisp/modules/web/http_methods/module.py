"""
===============================================================================
CISP (CyberInvincible Security Platform)

File:
    modules/web/http_methods/module.py

Purpose:
    Detect supported HTTP methods exposed by a web server.

Why this module exists:
    Enumerates HTTP methods and identifies potentially dangerous methods
    that may increase the attack surface.

Benefits:
    ✔ Detects supported HTTP methods
    ✔ Identifies risky methods
    ✔ Detects possible WebDAV support
    ✔ Returns structured scan results
===============================================================================
"""

from __future__ import annotations

from cisp.core.base_module import BaseModule
from cisp.utils.http import HTTPClient


class HTTPMethodsModule(BaseModule):
    """
    HTTP Methods Scanner.
    """

    name = "HTTP Methods Scanner"
    slug = "http_methods"
    description = "Detect supported HTTP methods."
    category = "Web"
    version = "1.0.0"
    author = "CISP"

    tags = [
        "http",
        "web",
        "methods",
        "enumeration",
    ]

    dependencies = []

    default_config = {
        "timeout": 10,
        "verify_ssl": True,
    }

    DANGEROUS_METHODS = {
        "PUT": "Allows uploading or replacing resources.",
        "DELETE": "Allows deleting resources.",
        "TRACE": "May enable Cross-Site Tracing (XST).",
        "CONNECT": "May allow proxy tunneling.",
        "PROPFIND": "WebDAV method detected.",
        "MKCOL": "WebDAV method detected.",
        "MOVE": "WebDAV method detected.",
        "COPY": "WebDAV method detected.",
        "LOCK": "WebDAV method detected.",
        "UNLOCK": "WebDAV method detected.",
    }

    def validate(self, context, url: str):

        if not url:
            raise ValueError("URL cannot be empty.")

        if not url.startswith(("http://", "https://")):
            raise ValueError(
                "URL must start with http:// or https://"
            )

    def execute(self, context, url: str):

        client = HTTPClient(
            timeout=self.default_config["timeout"],
            verify_ssl=self.default_config["verify_ssl"],
        )

        response = client.options(url)

        methods = self._collect_methods(response.headers)

        findings = self._analyze_methods(methods)

        return {
            "url": response.url,
            "status_code": response.status_code,
            "supported_methods": methods,
            "findings": findings,
            "headers": dict(response.headers),
        }

    def _collect_methods(self, headers):

        methods = set()

        allow = headers.get("Allow", "")

        public = headers.get("Public", "")

        for value in (allow, public):

            if value:

                methods.update(
                    method.strip().upper()
                    for method in value.split(",")
                )

        return sorted(methods)

    def _analyze_methods(self, methods):

        findings = []

        for method in methods:

            if method in self.DANGEROUS_METHODS:

                findings.append(
                    {
                        "method": method,
                        "severity": "Medium",
                        "description": self.DANGEROUS_METHODS[method],
                    }
                )

        return findings
from __future__ import annotations

import requests

from cisp.core.base_module import BaseModule


class SecurityHeadersPlugin(BaseModule):

    name = "Security Headers Analyzer"
    description = "Analyze HTTP security headers."
    category = "Web"
    version = "1.0.0"
    author = "CISP"

    REQUIRED_HEADERS = {
        "Content-Security-Policy": "Missing CSP header.",
        "Strict-Transport-Security": "Missing HSTS header.",
        "X-Frame-Options": "Missing clickjacking protection.",
        "X-Content-Type-Options": "Missing MIME sniffing protection.",
        "Referrer-Policy": "Missing Referrer-Policy.",
        "Permissions-Policy": "Missing Permissions-Policy.",
    }

    def validate(self, context, url: str):

        if not url:
            raise ValueError("URL cannot be empty.")

        if not url.startswith(("http://", "https://")):
            raise ValueError(
                "URL must start with http:// or https://"
            )

    def execute(self, context, url: str):

        response = requests.get(
            url,
            timeout=10,
            allow_redirects=True,
        )

        headers = response.headers

        findings = []

        for header, message in self.REQUIRED_HEADERS.items():

            if header not in headers:
                findings.append({
                    "header": header,
                    "status": "Missing",
                    "severity": "Medium",
                    "description": message,
                })
            else:
                findings.append({
                    "header": header,
                    "status": "Present",
                    "severity": "Info",
                    "value": headers.get(header),
                })

        return {
            "url": response.url,
            "status_code": response.status_code,
            "findings": findings,
        }
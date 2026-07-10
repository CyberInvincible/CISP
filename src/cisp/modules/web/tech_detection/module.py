from __future__ import annotations

import requests

from cisp.core.base_module import BaseModule


class TechDetectionPlugin(BaseModule):

    name = "Technology Detection"
    description = "Detect web technologies from HTTP headers."
    category = "Web"
    version = "1.0.0"
    author = "CISP"

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

        return {
            "url": response.url,
            "status_code": response.status_code,
            "server": headers.get("Server"),
            "powered_by": headers.get("X-Powered-By"),
            "content_type": headers.get("Content-Type"),
            "headers": dict(headers),
        }
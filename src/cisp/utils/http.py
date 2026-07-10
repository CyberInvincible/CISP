"""
===============================================================================
CISP (CyberInvincible Security Platform)

File:
    utils/http.py

Purpose:
    Provides a reusable HTTP client for all web-based CISP modules.

Why this file exists:
    Instead of every module creating its own HTTP requests, all networking
    goes through a shared HTTP client.

Benefits:
    ✔ Shared HTTP session
    ✔ Consistent timeout handling
    ✔ Consistent SSL verification
    ✔ Consistent User-Agent
    ✔ Easy future support for retries, proxies and authentication
===============================================================================
"""

from __future__ import annotations

from typing import Any

import requests
from requests import Response


class HTTPClient:
    """
    Shared HTTP client used by all CISP web modules.
    """

    def __init__(
        self,
        timeout: int = 10,
        verify_ssl: bool = True,
    ) -> None:

        self.timeout = timeout
        self.verify_ssl = verify_ssl

        self.session = requests.Session()

        self.session.headers.update(
            {
                "User-Agent": "CISP/1.0"
            }
        )

    def request(
        self,
        method: str,
        url: str,
        **kwargs: Any,
    ) -> Response:
        """
        Send an HTTP request.

        Parameters
        ----------
        method : str
            HTTP method (GET, POST, OPTIONS, etc.)

        url : str
            Target URL.

        Returns
        -------
        requests.Response
        """

        kwargs.setdefault("timeout", self.timeout)
        kwargs.setdefault("verify", self.verify_ssl)
        kwargs.setdefault("allow_redirects", True)

        response = self.session.request(
            method=method.upper(),
            url=url,
            **kwargs,
        )

        return response

    def get(self, url: str, **kwargs: Any) -> Response:
        """Send a GET request."""
        return self.request("GET", url, **kwargs)

    def post(self, url: str, **kwargs: Any) -> Response:
        """Send a POST request."""
        return self.request("POST", url, **kwargs)

    def head(self, url: str, **kwargs: Any) -> Response:
        """Send a HEAD request."""
        return self.request("HEAD", url, **kwargs)

    def options(self, url: str, **kwargs: Any) -> Response:
        """Send an OPTIONS request."""
        return self.request("OPTIONS", url, **kwargs)
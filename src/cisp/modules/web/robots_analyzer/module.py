"""
===============================================================================
CISP (CyberInvincible Security Platform)

File:
    modules/web/robots_analyzer/module.py

Purpose:
    Analyze robots.txt and sitemap.xml for reconnaissance information.

Version:
    1.0.0
===============================================================================
"""

from __future__ import annotations

from cisp.core.base_module import BaseModule
from cisp.utils.http import HTTPClient


class RobotsAnalyzerPlugin(BaseModule):

    name = "Robots Analyzer"
    description = "Analyze robots.txt and sitemap.xml."
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

        client = HTTPClient()

        base = url.rstrip("/")

        robots_url = f"{base}/robots.txt"
        sitemap_url = f"{base}/sitemap.xml"

        robots = self._fetch(client, robots_url)
        sitemap = self._fetch(client, sitemap_url)

        findings = []

        if robots["exists"]:
            findings.extend(
                self._parse_robots(robots["content"])
            )

        return {
            "target": url,
            "robots": robots,
            "sitemap": sitemap,
            "findings": findings,
        }

    def _fetch(self, client: HTTPClient, url: str):

        try:

            response = client.get(url)

            return {
                "url": url,
                "exists": response.status_code == 200,
                "status_code": response.status_code,
                "content": response.text,
            }

        except Exception:

            return {
                "url": url,
                "exists": False,
                "status_code": None,
                "content": "",
            }

    def _parse_robots(self, content: str):

        findings = []

        for line in content.splitlines():

            line = line.strip()

            if not line or line.startswith("#"):
                continue

            if ":" not in line:
                continue

            key, value = line.split(":", 1)

            findings.append(
                {
                    "directive": key.strip(),
                    "value": value.strip(),
                }
            )

        return findings
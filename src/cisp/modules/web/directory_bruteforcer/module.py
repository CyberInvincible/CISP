"""
===============================================================================
CISP (CyberInvincible Security Platform)

File:
    modules/web/directory_bruteforcer/module.py

Purpose:
    Discover common directories and files exposed by a web server.

Version:
    1.0.0 (Foundation)

Features:
    ✔ Uses shared HTTPClient
    ✔ Reads a wordlist
    ✔ Detects accessible paths
    ✔ Returns structured results
===============================================================================
"""

from __future__ import annotations

from pathlib import Path

from cisp.core.base_module import BaseModule
from cisp.utils.http import HTTPClient


class DirectoryBruteforcerPlugin(BaseModule):

    name = "Directory Bruteforcer"
    description = "Discover common directories and files."
    category = "Web"
    version = "1.0.0"
    author = "CISP"

    INTERESTING_STATUS_CODES = {
        200,
        204,
        301,
        302,
        307,
        308,
        401,
        403,
    }

    def validate(self, context, url: str):

        if not url:
            raise ValueError("URL cannot be empty.")

        if not url.startswith(("http://", "https://")):
            raise ValueError(
                "URL must start with http:// or https://"
            )

    def execute(self, context, url: str):

        client = HTTPClient()

        wordlist = self._load_wordlist()

        findings = []

        base = url.rstrip("/")

        for entry in wordlist:

            target = f"{base}/{entry}"

            try:

                response = client.get(target)

                if response.status_code in self.INTERESTING_STATUS_CODES:

                    findings.append(
                        {
                            "path": entry,
                            "url": target,
                            "status": response.status_code,
                            "content_length": len(response.content),
                        }
                    )

            except Exception:
                continue

        return {
            "url": url,
            "tested_paths": len(wordlist),
            "findings": findings,
        }

    def _load_wordlist(self) -> list[str]:

        wordlist_path = (
            Path(__file__).parent
            / "wordlists"
            / "common.txt"
        )

        with wordlist_path.open(
            "r",
            encoding="utf-8",
        ) as file:

            return [
                line.strip()
                for line in file
                if line.strip()
            ]
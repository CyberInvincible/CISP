"""
===============================================================================
CISP (CyberInvincible Security Platform)

Banner Grabber Plugin

Purpose:
    Connect to an open TCP port and retrieve the service banner.
===============================================================================
"""

from __future__ import annotations

import socket

from cisp.core.base_module import BaseModule


class BannerGrabberPlugin(BaseModule):
    """
    Grab banners from open TCP services.
    """

    name = "Banner Grabber"
    description = "Grab banners from open TCP services."
    category = "Network"
    version = "1.0.0"
    author = "CISP"

    def validate(self, context, host: str, port: int):

        if not host:
            raise ValueError("Host cannot be empty.")

        if port < 1 or port > 65535:
            raise ValueError("Port must be between 1 and 65535.")

    def execute(self, context, host: str, port: int):

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)

        try:

            sock.connect((host, port))

            try:
                sock.send(b"\r\n")
            except Exception:
                pass

            try:
                banner = sock.recv(4096).decode(
                    errors="ignore"
                ).strip()
            except Exception:
                banner = ""

            result = {
                "target": host,
                "port": port,
                "banner": banner,
            }

            context.set("banner", result)

            return result

        finally:
            sock.close()
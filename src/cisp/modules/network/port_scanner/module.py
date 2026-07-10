"""
===============================================================================
CISP (CyberInvincible Security Platform)

Port Scanner Plugin

Purpose:
    Scan TCP ports on a target host.

Version:
    1.0.0
===============================================================================
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

import socket

from cisp.core.base_module import BaseModule


class PortScannerPlugin(BaseModule):
    """
    TCP Port Scanner.
    """

    name = "Port Scanner"
    description = "Scan TCP ports on a target."
    category = "Network"
    version = "1.0.0"
    author = "CISP"

    # ------------------------------------------------------------------

    def validate(
        self,
        context,
        host: str,
        start_port: int = 1,
        end_port: int = 1024,
    ) -> None:

        if not host:
            raise ValueError("Target host cannot be empty.")

        if start_port < 1 or end_port > 65535:
            raise ValueError("Port range must be between 1 and 65535.")

        if start_port > end_port:
            raise ValueError("Start port cannot be greater than end port.")

    # ------------------------------------------------------------------

    def scan_port(self, host: str, port: int):

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.3)

        try:

            if sock.connect_ex((host, port)) == 0:

                try:
                    service = socket.getservbyport(port)
                except OSError:
                    service = "unknown"

                return {
                    "port": port,
                    "service": service,
                }

        finally:
            sock.close()

        return None

    # ------------------------------------------------------------------

    def execute(
        self,
        context,
        host: str,
        start_port: int = 1,
        end_port: int = 1024,
    ):

        open_ports = []

        with ThreadPoolExecutor(max_workers=100) as executor:

            futures = [
                executor.submit(self.scan_port, host, port)
                for port in range(start_port, end_port + 1)
            ]

            for future in futures:

                result = future.result()

                if result:
                    open_ports.append(result)

        open_ports.sort(key=lambda x: x["port"])

        result = {
            "target": host,
            "start_port": start_port,
            "end_port": end_port,
            "total_open": len(open_ports),
            "open_ports": open_ports,
        }

        context.set("open_ports", open_ports)

        return result
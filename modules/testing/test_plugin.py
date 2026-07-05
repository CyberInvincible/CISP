"""
Simple test plugin for CISP.
"""

from core.base_module import BaseModule


class TestPlugin(BaseModule):

    name = "Test Plugin"

    description = "Used to test plugin loading."

    author = "Rudra"

    version = "0.1.0"

    category = "Testing"

    tags = ["test"]

    def run(self):

        return {
            "status": "success"
        }
"""
===============================================================================
CISP (CyberInvincible Security Platform)

File:
    cli/wizard.py

Purpose:
    Interactive Scan Wizard.

The wizard collects user input and returns the selected
scan profile along with the target.
===============================================================================
"""

from __future__ import annotations


class ScanWizard:

    def start(self):

        print("\n======================================")
        print("        Scan Wizard")
        print("======================================")

        print("1. Quick Scan")
        print("2. Web Security Scan")
        print("3. Infrastructure Scan")
        print("4. Full Security Assessment")
        print("5. Manual Plugin Mode")
        print("0. Exit")

        while True:

            choice = input("\nSelect profile: ").strip()

            if choice in ("0", "1", "2", "3", "4", "5"):
                break

            print("Invalid selection.")

        if choice == "0":
            return None

        target = input("\nEnter target (URL/IP/Domain): ").strip()

        return {
            "profile": choice,
            "target": target,
        }
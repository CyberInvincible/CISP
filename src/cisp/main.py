"""
Application entry point.

Running:

    cisp

or

    python -m cisp.main

will start the application.
"""

from cisp.cli.app import CLIApplication


def main() -> None:
    """Launch CISP."""

    app = CLIApplication()
    app.run()


if __name__ == "__main__":
    main()
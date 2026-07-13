"""
Maps menu selections to scan profiles.
"""


class ProfileMapper:

    MAP = {
        "1": "quick",
        "2": "web",
        "3": "infrastructure",
        "4": "full",
        "5": "manual",
    }

    @classmethod
    def get_profile(cls, choice: str):

        return cls.MAP.get(choice)
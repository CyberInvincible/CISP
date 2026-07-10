from cisp.config.profile_manager import ProfileManager


def test_profile_manager_loads():

    manager = ProfileManager()

    assert manager.exists("quick")
    assert manager.exists("web")
    assert manager.exists("full")


def test_web_profile_contains_modules():

    manager = ProfileManager()

    modules = manager.modules("web")

    assert "HTTP Methods Scanner" in modules
    assert "Technology Detection" in modules
from cisp.core.base_module import BaseModule


class TestPlugin(BaseModule):
    """
    Simple plugin used to verify the CISP framework.
    """

    name = "Test Plugin"
    description = "Framework test plugin"
    category = "Testing"
    version = "0.1.0"
    author = "CISP"

    def execute(self, context):
        """
        Plugin logic.

        BaseModule.run() handles timing, errors,
        and ModuleResult creation automatically.
        """

        return {
            "status": "success",
            "message": "Framework is working correctly."
        }
from cisp.core.base_module import BaseModule
from cisp.core.context import Context


class TestModule(BaseModule):
    name = "Test Module"
    description = "Simple test module"
    author = "Rudra"
    version = "0.1.0"
    category = "Testing"

    def execute(self, context: Context):
        return {
            "status": "success"
        }


def test_base_module_execution():

    module = TestModule()

    result = module.run(Context())

    assert result.success is True
    assert result.data["status"] == "success"
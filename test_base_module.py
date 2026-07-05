from core.base_module import BaseModule


class TestModule(BaseModule):
    name = "Test Module"
    description = "Simple test module"
    author = "Rudra"
    version = "0.1.0"
    category = "Testing"

    def run(self):
        return {"status": "success"}


module = TestModule()

print(module.name)
print(module.run())
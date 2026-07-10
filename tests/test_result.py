from cisp.models import ModuleResult

result = ModuleResult(
    success=True,
    data={"status": "ok"},
    message="Test completed successfully."
)

print(result)
print(result.success)
print(result.data)
print(result.has_errors())
print(result.has_warnings())
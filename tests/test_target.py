from cisp.core.target import Target


target = Target.parse("google.com")

print(target)

print(target.hostname)
print(target.url)
print(target.scheme)
print(target.port)
print(target.is_domain)
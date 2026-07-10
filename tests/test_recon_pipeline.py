from cisp.core.plugin_loader import PluginLoader
from cisp.core.registry import PluginRegistry
from cisp.core.engine import Engine

loader = PluginLoader()
plugins = loader.discover()

registry = PluginRegistry()

for plugin in plugins:
    registry.register(plugin)

engine = Engine(registry)

# ---------------------------
# Execute Recon Modules
# ---------------------------

whois = engine.execute(
    "WHOIS Lookup",
    "openai.com"
)

dns = engine.execute(
    "DNS Lookup",
    "openai.com"
)

ports = engine.execute(
    "Port Scanner",
    "openai.com",
    1,
    100
)

banner = engine.execute(
    "Banner Grabber",
    "openai.com",
    80
)

technology = engine.execute(
    "Technology Detection",
    "https://openai.com"
)

headers = engine.execute(
    "Security Headers Analyzer",
    "https://openai.com"
)

vulnerabilities = engine.execute(
    "Vulnerability Analyzer",
    "https://openai.com"
)

# ---------------------------
# Collect Results
# ---------------------------

results = {
    "whois": whois,
    "dns": dns,
    "ports": ports,
    "banner": banner,
    "technology": technology,
    "headers": headers,
    "vulnerabilities": vulnerabilities,
}

print(results)

from cisp.reporting.html_report import HTMLReport

HTMLReport().generate(results)
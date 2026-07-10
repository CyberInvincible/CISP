from cisp.core.engine import Engine
from cisp.core.plugin_loader import PluginLoader
from cisp.core.registry import PluginRegistry

from cisp.pipelines.recon import ReconPipeline
from cisp.reporting.aggregator import ResultAggregator
from cisp.reporting.json_report import JSONReportGenerator

loader = PluginLoader()
registry = PluginRegistry()

for plugin in loader.discover():
    registry.register(plugin)

engine = Engine(registry)

pipeline = ReconPipeline(engine)

results = pipeline.execute("openai.com")

report = ResultAggregator().aggregate(results)

output = JSONReportGenerator().generate(report)

print(output)
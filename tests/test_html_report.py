from pathlib import Path

from cisp.core.engine import Engine
from cisp.core.plugin_loader import PluginLoader
from cisp.core.registry import PluginRegistry

from cisp.pipelines.recon import ReconPipeline
from cisp.reporting.html_report import HTMLReport


def test_html_report_generation():

    loader = PluginLoader()
    registry = PluginRegistry()

    for plugin in loader.discover():
        registry.register(plugin)

    engine = Engine(registry)

    pipeline = ReconPipeline(engine)

    results = pipeline.execute("openai.com")

    HTMLReport().generate(results)

    assert Path("report.html").exists()
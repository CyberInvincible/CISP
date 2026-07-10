from pathlib import Path


class HTMLReport:

    def __init__(self):

        self.template = Path(
            __file__
        ).parent / "templates" / "report.html"

    def generate(self, results):

        html = self.template.read_text(
            encoding="utf-8"
        )

        cards = ""
        table = ""

        total = len(results)
        success = 0
        failed = 0

        for name, result in results.items():

            if result.success:
                success += 1
                status = "SUCCESS"
                css = "success"
            else:
                failed += 1
                status = "FAILED"
                css = "failed"

            table += f"""
<tr>
<td>{name}</td>
<td class="{css}">{status}</td>
<td>{result.execution_time:.3f}s</td>
<td>{result.message}</td>
</tr>
"""

        cards = f"""
<div class="cards">

<div class="card">
<h2>{total}</h2>
<p>Total Modules</p>
</div>

<div class="card green">
<h2>{success}</h2>
<p>Successful</p>
</div>

<div class="card red">
<h2>{failed}</h2>
<p>Failed</p>
</div>

</div>
"""

        html = html.replace(
            "{{SUMMARY}}",
            cards
        )

        html = html.replace(
            "{{TABLE}}",
            table
        )

        Path("report.html").write_text(
            html,
            encoding="utf-8"
        )

        print("Report generated -> report.html")
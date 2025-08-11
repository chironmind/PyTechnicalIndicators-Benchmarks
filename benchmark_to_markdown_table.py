import json

def load_benchmarks(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data.get("benchmarks", [])

def format_us(x):
    """Format number as microseconds with 2 decimals, or empty if missing."""
    if isinstance(x, (float, int)):
        return f"{x * 1e6:.2f}"
    return ""

def format_number(x):
    """Format numbers for compact scientific notation."""
    if isinstance(x, float):
        return f"{x:.2e}"
    return str(x)

def make_table(benchmarks):
    headers = [
        "Run Name", "Rounds", "Min (µs)", "Max (µs)", "Mean (µs)", "Median (µs)",
        "Stddev (µs)", "Ops/sec"
    ]
    lines = ["| " + " | ".join(headers) + " |", "|" + "----|" * len(headers)]
    for bm in benchmarks:
        stats = bm["stats"]
        params = bm.get("params", {})
        row = [
            "`" + bm.get("name", "") + "`",
            str(stats.get("rounds", "")),
            format_us(stats.get("min", "")),
            format_us(stats.get("max", "")),
            format_us(stats.get("mean", "")),
            format_us(stats.get("median", "")),
            format_us(stats.get("stddev", "")),
            format_number(stats.get("ops", "")),
        ]
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <benchmark_results.json>")
        exit(1)
    benchmarks = load_benchmarks(sys.argv[1])
    table = make_table(benchmarks)
    print(table)

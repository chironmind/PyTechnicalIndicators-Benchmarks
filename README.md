# PyTechnicalIndicators Benchmarks

Performance benchmarks for PyTechnicalIndicators library using pytest-benchmark.

## Setup

```bash
pip install -r requirements.txt
```

## Running Benchmarks

### Basic benchmark run
```bash
pytest
```

### Run specific indicator groups
```bash
pytest -k "rsi_single"      # Only Single RSI benchmarks
pytest -k "rsi_bulk"        # Only Bulk RSI benchmarks  
pytest -k "small"           # Only small dataset benchmarks
pytest -k "trend"           # Only trend indicators
```

### Run with different output formats
```bash
# Table output (default)
pytest --benchmark-columns=min,max,mean,stddev,rounds

# JSON output for CI/analysis
pytest --benchmark-json=results/benchmark_results.json

# HTML report
pytest --benchmark-json=results/results.json
python -m pytest_benchmark compare results/results.json --csv=results/benchmark.csv

# Histogram
pytest --benchmark-histogram=results/histogram.svg
```

### Compare benchmark results
```bash
# Run baseline
pytest --benchmark-json=results/baseline.json

# Run after changes  
pytest --benchmark-json=results/current.json

# Compare
pytest-benchmark compare results/baseline.json results/current.json
```

### Performance analysis
```bash
# Sort by different metrics
pytest --benchmark-sort=min
pytest --benchmark-sort=max  
pytest --benchmark-sort=mean
pytest --benchmark-sort=stddev

# Skip slow tests
pytest -k "not large"

# Only run large dataset tests
pytest -k "large"
```

## About the benchmark tests

### Before you start

Each indicator is benchmarked according to the PyTechnicalIndicators code file they live in.

For example, `relative_strength_index` lives in the `momentum_indicators` file, its benchmark
file will be `test_momentum_indicators_bench.py`.

Each different flavor of the indicator is tested, this means all different constant model types, 
and deviation models are tested, and in different combinations. This leads to a lot of different benches
of the same function, but gives us a good idea of how the different deviation and constant models interact.

All benchmarks were run on a **Raspberry Pi 5 (8GB RAM)** split over different data sizes.
Why a Raspberry Pi? It’s a familiar, modest baseline, your machine is probably much faster!
For more details, see the [Raspberry Pi 5 benchmarks](https://www.raspberrypi.com/news/benchmarking-raspberry-pi-5/).

All benchmarks were saved under `results/` so that they can be used as comparaisons. The results are split by 
data size as there a lot of benchmarks run.

### Data Sizes

The full data set is daily data over the course of 10 years

- **Small**: 255 data points (1 year of daily data)
- **Medium**: 1276 data points (5 years of daily data)
- **Large**: 2552 data points (10 years of daily data)

If you want to know how quickly the code will run for you dataset, you'll need to study your data to see in which
size it falls under, then narrow it down to which indicators you're interested in and run those. This will give you
a complete picutre of what to expect.

### Results

These result will summarize the results from the benches on a RPI5, a full human friendly run can be found [here](https://github.com/ChironMind/PyTechnicalIndicators_Benchmarks/results/markdown).

The results are split by indicator category, then data size. For indicators that have multiple possible combinations (constant model
type, deviation model...) only the fastest and the slowest combination will be provided here. More details can
be found in the `results/markdown` directory.

#### Candle Indicators

##### Small

TBD

##### Medium

| Run Name | Rounds | Min (µs) | Max (µs) | Mean (µs) | Median (µs) | Stddev (µs) | Ops/sec |
|----|----|----|----|----|----|----|----|
| Single Moving Constant Env [simple ma] | 30287 | 17.94 | 36.87 | 18.17 | 18.13 | 0.26 | 5.50e+04 |
| Single Moving Constant Env [mode] | 11699 | 70.56 | 981.17 | 75.59 | 74.89 | 10.18 | 1.32e+04 |
| Bulk Moving Constant Env [simple ma] | 1225 | 139.13 | 565.80 | 142.80 | 140.09 | 15.91 | 7.00e+03 |
| Bulk Moving Constant Env [mode] | 561 | 1740.75 | 2524.77 | 1779.91 | 1763.66 | 49.48 | 5.62e+02 |



---

## 📚 About This Repo

This repository is part of a structured documentation suite:

- 📕 **Tutorials:** — [See here](https://github.com/ChironMind/PyTechnicalIndicators_Tutorials)
- 📘 **How-To Guides:** — [See here](https://github.com/ChironMind/PyTechnicalIndicators-How-To-guides)
- ⏱️ **Benchmarks:** This repo!
- 📙 **Explanations:** — Coming soon
- 📗 **Reference:** — [See here](https://github.com/ChironMind/PyTechnicalIndicators/wiki)

---


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
pytest -k "sma"           # Only SMA benchmarks
pytest -k "rsi"           # Only RSI benchmarks  
pytest -k "small"         # Only small dataset benchmarks
pytest -k "trend"         # Only trend indicators
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

## Benchmark Groups

!!! TODO !!!

- **Trend Indicators**: SMA, EMA, MACD
- **Momentum Indicators**: RSI, Stochastic, Williams %R  
- **Volatility Indicators**: Bollinger Bands, ATR
- **Volume Indicators**: OBV, Volume SMA
- **Overlap Indicators**: Moving averages

## Data Sizes

- **Small**: 100 data points
- **Medium**: 500 data points
- **Large**: 2552 data points (10 years of daily data)


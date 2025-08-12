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

These result will summarize the results from the benches on a RPI5, full human friendly runs can be found [here](https://github.com/ChironMind/PyTechnicalIndicators_Benchmarks/results/markdown).

The results are split by indicator category, then data size. For indicators that have multiple possible combinations (constant model
type, deviation model...) only the fastest and the slowest combination will be provided here. More details can
be found in the `results/markdown` directory.

Due to the size of the files produced Candles [small] and all momentum indicator runs aren't available in results for comparaisons.

#### Candle Indicators

##### Small

TBD

##### Medium

| Run Name | Rounds | Min (µs) | Max (µs) | Mean (µs) | Median (µs) | Stddev (µs) | Ops/sec |
|----|----|----|----|----|----|----|----|
| `test_single_mce[medium-simple]` | 30287 | 17.94 | 36.87 | 18.17 | 18.13 | 0.26 | 5.50e+04 |
| `test_single_mce[medium-mode]` | 11699 | 70.56 | 981.17 | 75.59 | 74.89 | 10.18 | 1.32e+04 |
| `test_bulk_mce[medium-simple]` | 1225 | 139.13 | 565.80 | 142.80 | 140.09 | 15.91 | 7.00e+03 |
| `test_bulk_mce[medium-mode]` | 561 | 1740.75 | 2524.77 | 1779.91 | 1763.66 | 49.48 | 5.62e+02 |
| `test_single_mcginley_env[medium]` | 30946 | 16.67 | 359.19 | 17.27 | 16.91 | 4.02 | 5.79e+04 |
| `test_bulk_mcginley_env[medium]` | 5846 | 133.52 | 470.28 | 140.53 | 135.39 | 18.69 | 7.12e+03 |
| `test_single_bands[medium-mean-simple]` | 40269 | 19.87 | 92.80 | 20.34 | 20.15 | 2.45 | 4.92e+04 |
| `test_single_bands[medium-ulcer-mode]` | 543 | 1752.67 | 2008.73 | 1789.22 | 1767.56 | 47.47 | 5.59e+02 |
| `test_bulk_bands[medium-mean-simple]` | 4884 | 187.41 | 804.74 | 192.65 | 189.19 | 19.60 | 5.19e+03 |
| `test_bulk_bands[medium-mode-mode]` | 283 | 3387.07 | 3914.07 | 3467.76 | 3449.13 | 62.49 | 2.88e+02 |
| `test_single_mcginley_bands[medium-mean]` | 43939 | 18.57 | 80.65 | 19.18 | 19.06 | 2.23 | 5.21e+04 |
| `test_single_mcginley_bands[medium-ulcer]` | 587 | 1696.64 | 1864.45 | 1709.24 | 1698.88 | 23.54 | 5.85e+02 |
| `test_bulk_mcginley_bands[medium-mean]` | 5391 | 172.22 | 324.26 | 175.96 | 174.28 | 9.18 | 5.68e+03 |
| `test_bulk_mcginley_bands[medium-mode]` | 533 | 1806.40 | 2353.66 | 1842.36 | 1820.67 | 51.06 | 5.43e+02 |
| `test_single_ichimoku[medium]` | 17476 | 49.98 | 96.70 | 50.71 | 50.50 | 1.14 | 1.97e+04 |
| `test_bulk_ichimoku[medium]` | 870 | 531.65 | 649.41 | 534.60 | 532.72 | 10.28 | 1.87e+03 |
| `test_single_donchian[medium]` | 22776 | 38.69 | 67.02 | 39.02 | 38.98 | 0.55 | 2.56e+04 |
| `test_bulk_donchian[medium]` | 3985 | 199.28 | 1303.17 | 203.70 | 202.96 | 18.97 | 4.91e+03 |
| `test_single_keltner[medium-simple-simple]` | 15250 | 56.04 | 1239.69 | 56.84 | 56.46 | 10.04 | 1.76e+04 |
| `test_single_keltner[medium-mode-mode]` | 6178 | 135.54 | 262.80 | 145.01 | 144.93 | 4.03 | 6.90e+03 |
| `test_bulk_keltner[medium-simple-simple]` | 366 | 361.43 | 472.24 | 365.80 | 362.82 | 12.57 | 2.73e+03 |
| `test_bulk_keltner[medium-mode-mode]` | 295 | 3307.79 | 3657.09 | 3365.07 | 3349.55 | 55.23 | 2.97e+02 |
| `test_single_supertrend[medium-simple]` | 14690 | 56.85 | 95.43 | 57.80 | 57.30 | 1.09 | 1.73e+04 |
| `test_single_supertrend[medium-mode]` | 9320 | 85.44 | 143.24 | 90.95 | 91.13 | 2.00 | 1.10e+04 |
| `test_bulk_supertrend[medium-simple]` | 3658 | 232.67 | 277.20 | 235.10 | 234.46 | 2.87 | 4.25e+03 |
| `test_bulk_supertrend[medium-mode]` | 603 | 1589.60 | 7154.47 | 1632.99 | 1622.51 | 225.84 | 6.12e+02 |

##### Large

| Run Name | Rounds | Min (µs) | Max (µs) | Mean (µs) | Median (µs) | Stddev (µs) | Ops/sec |
|----|----|----|----|----|----|----|----|
| `test_single_mce[large-simple]` | 16912 | 34.70 | 100.94 | 35.48 | 35.24 | 3.40 | 2.82e+04 |
| `test_single_mce[large-mode]` | 6075 | 142.78 | 398.39 | 150.90 | 149.72 | 8.57 | 6.63e+03 |
| `test_bulk_mce[large-simple]` | 1138 | 288.48 | 449.33 | 294.61 | 290.65 | 15.23 | 3.39e+03 |
| `test_bulk_mce[large-mode]` | 263 | 3658.81 | 4139.33 | 3710.86 | 3690.35 | 52.10 | 2.69e+02 |
| `test_single_mcginley_env[large]` | 25472 | 33.44 | 218.54 | 34.23 | 34.04 | 3.43 | 2.92e+04 |
| `test_bulk_mcginley_env[large]` | 2665 | 279.45 | 599.76 | 284.83 | 281.44 | 16.06 | 3.51e+03 |
| `test_single_bands[large-mean-simple]` | 21845 | 39.65 | 228.30 | 40.32 | 39.93 | 4.10 | 2.48e+04 |
| `test_single_bands[large-ulcer-mode]` | 145 | 6903.54 | 7040.79 | 6913.58 | 6909.32 | 15.99 | 1.45e+02 |
| `test_bulk_bands[large-mean-simple]` | 2454 | 384.39 | 595.15 | 389.18 | 387.63 | 12.53 | 2.57e+03 |
| `test_bulk_bands[large-mode-mode]` | 139 | 7087.03 | 7451.68 | 7132.68 | 7123.31 | 40.17 | 1.40e+02 |
| `test_single_mcginley_bands[large-mean]` | 23488 | 36.35 | 63.45 | 37.00 | 37.00 | 0.64 | 2.70e+04 |
| `test_single_mcginley_bands[large-ulcer]` | 147 | 6787.41 | 6890.86 | 6793.59 | 6790.34 | 11.68 | 1.47e+02 |
| `test_bulk_mcginley_bands[large-mean]` | 2612 | 356.63 | 628.30 | 360.35 | 358.69 | 14.55 | 2.78e+03 |
| `test_bulk_mcginley_bands[large-mode]` | 262 | 3756.16 | 4239.63 | 3772.07 | 3766.30 | 33.39 | 2.65e+02 |
| `test_single_ichimoku[large]` | 9052 | 103.02 | 158.87 | 104.11 | 103.91 | 1.92 | 9.60e+03 |
| `test_bulk_ichimoku[large]` | 192 | 1089.34 | 1541.80 | 1105.23 | 1092.71 | 56.55 | 9.05e+02 |
| `test_single_donchian[large]` | 11934 | 78.98 | 112.37 | 79.79 | 79.65 | 1.06 | 1.25e+04 |
| `test_bulk_donchian[large]` | 1808 | 414.35 | 715.54 | 418.40 | 416.45 | 15.84 | 2.39e+03 |
| `test_single_keltner[large-simple-simple]` | 7810 | 109.67 | 222.43 | 112.84 | 112.46 | 3.28 | 8.86e+03 |
| `test_single_keltner[large-mode-mode]` | 3264 | 275.56 | 446.06 | 290.56 | 290.46 | 6.65 | 3.44e+03 |
| `test_bulk_keltner[large-simple-simple]` | 1151 | 735.98 | 1044.25 | 742.41 | 739.86 | 19.29 | 1.35e+03 |
| `test_bulk_keltner[large-mode-mode]` | 138 | 7101.66 | 7807.01 | 7145.78 | 7128.74 | 82.83 | 1.40e+02 |
| `test_single_supertrend[large-simple]` | 7921 | 115.04 | 169.19 | 116.83 | 116.69 | 2.56 | 8.56e+03 |
| `test_single_supertrend[large-mode]` | 5216 | 168.54 | 245.02 | 179.49 | 179.58 | 3.51 | 5.57e+03 |
| `test_bulk_supertrend[large-simple]` | 1963 | 468.22 | 558.85 | 473.25 | 472.54 | 5.84 | 2.11e+03 |
| `test_bulk_supertrend[large-mode]` | 282 | 3491.31 | 3766.89 | 3531.67 | 3531.92 | 22.97 | 2.83e+02 |

---

#### Chart Trends

##### Small

| Run Name | Rounds | Min (µs) | Max (µs) | Mean (µs) | Median (µs) | Stddev (µs) | Ops/sec |
|----|----|----|----|----|----|----|----|
| `test_peaks[10-small]` | 28769 | 28.70 | 114.44 | 28.94 | 28.87 | 0.89 | 3.46e+04 |
| `test_peaks[1-small]` | 19875 | 29.13 | 76.41 | 29.33 | 29.24 | 1.25 | 3.41e+04 |
| `test_valleys[5-small]` | 26368 | 30.11 | 151.41 | 30.33 | 30.24 | 1.42 | 3.30e+04 |
| `test_valleys[1-small]` | 23716 | 30.39 | 56.09 | 30.56 | 30.52 | 0.45 | 3.27e+04 |
| `test_peak_trend[3-small]` | 45076 | 8.13 | 127.78 | 8.37 | 8.26 | 1.35 | 1.19e+05 |
| `test_peak_trend[20-small]` | 45571 | 14.39 | 35.82 | 14.55 | 14.52 | 0.29 | 6.87e+04 |
| `test_valley_trend[3-small]` | 54219 | 8.24 | 183.48 | 8.41 | 8.37 | 0.98 | 1.19e+05 |
| `test_valley_trend[20-small]` | 35880 | 15.04 | 36.26 | 15.18 | 15.15 | 0.36 | 6.59e+04 |
| `test_overall_trend[small]` | 102281 | 4.65 | 29.06 | 4.75 | 4.74 | 0.23 | 2.11e+05 |
| `test_break_down_trends[1.0-0.75-1-small]` | 13246 | 51.09 | 166.96 | 52.03 | 51.69 | 2.78 | 1.92e+04 |
| `test_break_down_trends[1.5-0.5-1-small]` | 10859 | 58.95 | 167.43 | 59.88 | 59.61 | 2.57 | 1.67e+04 |

##### Medium

| Run Name | Rounds | Min (µs) | Max (µs) | Mean (µs) | Median (µs) | Stddev (µs) | Ops/sec |
|----|----|----|----|----|----|----|----|
| `test_peaks[10-medium]` | 5871 | 157.65 | 284.93 | 159.20 | 158.08 | 4.52 | 6.28e+03 |
| `test_peaks[1-medium]` | 4721 | 167.78 | 1002.62 | 176.34 | 168.71 | 23.06 | 5.67e+03 |
| `test_valleys[10-medium]` | 5307 | 175.06 | 265.35 | 175.67 | 175.32 | 1.95 | 5.69e+03 |
| `test_valleys[1-medium]` | 4977 | 183.09 | 213.48 | 183.68 | 183.37 | 1.51 | 5.44e+03 |
| `test_peak_trend[10-medium]` | 11068 | 67.54 | 96.72 | 68.01 | 67.85 | 0.90 | 1.47e+04 |
| `test_peak_trend[3-medium]` | 10591 | 81.57 | 110.56 | 82.10 | 82.00 | 0.72 | 1.22e+04 |
| `test_valley_trend[10-medium]` | 11722 | 68.76 | 117.95 | 69.32 | 69.17 | 0.98 | 1.44e+04 |
| `test_valley_trend[3-medium]` | 10521 | 80.76 | 111.61 | 81.23 | 81.09 | 0.87 | 1.23e+04 |
| `test_overall_trend[medium]` | 21549 | 21.70 | 64.02 | 22.00 | 21.94 | 0.68 | 4.54e+04 |
| `test_break_down_trends[1.0-0.75-0-medium]` | 413 | 2370.29 | 2557.37 | 2392.66 | 2379.13 | 32.67 | 4.18e+02 |
| `test_break_down_trends[1.0-0.5-1-medium]` | 283 | 3474.84 | 3644.34 | 3503.35 | 3505.76 | 18.47 | 2.85e+02 |

##### Large

| Run Name | Rounds | Min (µs) | Max (µs) | Mean (µs) | Median (µs) | Stddev (µs) | Ops/sec |
|----|----|----|----|----|----|----|----|
| `test_peaks[10-large]` | 2946 | 320.08 | 548.11 | 322.69 | 320.67 | 9.22 | 3.10e+03 |
| `test_peaks[1-large]` | 2388 | 356.80 | 427.56 | 360.25 | 357.58 | 9.27 | 2.78e+03 |
| `test_valleys[10-large]` | 2676 | 358.15 | 468.00 | 360.66 | 358.60 | 7.87 | 2.77e+03 |
| `test_valleys[1-large]` | 2446 | 383.45 | 660.45 | 387.26 | 384.06 | 12.47 | 2.58e+03 |
| `test_peak_trend[10-large]` | 4938 | 184.39 | 381.43 | 186.55 | 185.20 | 6.97 | 5.36e+03 |
| `test_peak_trend[3-large]` | 3534 | 260.46 | 458.67 | 262.78 | 261.15 | 7.40 | 3.81e+03 |
| `test_valley_trend[10-large]` | 4769 | 183.59 | 785.30 | 186.54 | 184.21 | 20.32 | 5.36e+03 |
| `test_valley_trend[3-large]` | 3417 | 259.58 | 8505.53 | 285.03 | 261.34 | 211.46 | 3.51e+03 |
| `test_overall_trend[large]` | 8425 | 44.26 | 519.65 | 46.59 | 44.94 | 10.74 | 2.15e+04 |
| `test_break_down_trends[1.0-0.75-0-large]` | 68 | 14757.55 | 15754.47 | 15042.71 | 14979.53 | 251.33 | 6.65e+01 |
| `test_break_down_trends[1.5-0.5-1-large]` | 57 | 17440.31 | 18088.63 | 17667.48 | 17593.41 | 202.04 | 5.66e+01 |

---

#### Correlation Indicators

##### Small

| Run Name | Rounds | Min (µs) | Max (µs) | Mean (µs) | Median (µs) | Stddev (µs) | Ops/sec |
|----|----|----|----|----|----|----|----|
| `test_single_correlation_small[mean-simple]` | 73470 | 7.87 | 937.45 | 8.60 | 8.57 | 3.44 | 1.16e+05 |
| `test_single_correlation_small[ulcer-mode]` | 5536 | 158.56 | 200.52 | 160.62 | 160.44 | 1.37 | 6.23e+03 |
| `test_single_correlation_small[mode-simple]` | 24413 | 30.78 | 71.19 | 32.91 | 32.89 | 0.74 | 3.04e+04 |
| `test_single_correlation_small[mode-mode]` | 14934 | 53.78 | 180.37 | 58.87 | 57.70 | 5.62 | 1.70e+04 |
| `test_bulk_correlation_small[mean-simple]` | 16217 | 42.28 | 93.78 | 42.96 | 42.69 | 1.40 | 2.33e+04 |
| `test_bulk_correlation_small[mode-mode]` | 765 | 1269.60 | 1500.97 | 1284.95 | 1281.16 | 14.94 | 7.78e+02 |

##### Medium

| Run Name | Rounds | Min (µs) | Max (µs) | Mean (µs) | Median (µs) | Stddev (µs) | Ops/sec |
|----|----|----|----|----|----|----|----|
| `test_single_correlation_medium[mean-simple]` | 20256 | 41.22 | 96.63 | 41.81 | 41.80 | 0.79 | 2.39e+04 |
| `test_single_correlation_medium[ulcer-mode]` | 284 | 3506.58 | 3584.71 | 3513.89 | 3512.27 | 8.48 | 2.85e+02 |
| `test_single_correlation_medium[mode-simple]` | 6075 | 148.93 | 201.00 | 155.60 | 155.43 | 2.04 | 6.43e+03 |
| `test_single_correlation_medium[mode-mode]` | 3472 | 257.83 | 903.34 | 268.56 | 267.96 | 11.59 | 3.72e+03 |
| `test_bulk_correlation_medium[mean-simple]` | 4208 | 220.67 | 278.96 | 222.67 | 222.19 | 2.77 | 4.49e+03 |
| `test_bulk_correlation_medium[mode-mode]` | 149 | 6593.78 | 6792.52 | 6642.85 | 6640.10 | 23.93 | 1.51e+02 |

##### Large

| Run Name | Rounds | Min (µs) | Max (µs) | Mean (µs) | Median (µs) | Stddev (µs) | Ops/sec |
|----|----|----|----|----|----|----|----|
| `test_single_correlation_large[mean-simple]` | 10963 | 81.46 | 130.04 | 82.03 | 81.85 | 1.38 | 1.22e+04 |
| `test_single_correlation_large[ulcer-mode]` | 73 | 13810.40 | 13977.29 | 13824.72 | 13818.36 | 22.49 | 7.23e+01 |
| `test_single_correlation_large[mode-simple]` | 3081 | 302.84 | 368.60 | 312.39 | 312.02 | 3.64 | 3.20e+03 |
| `test_single_correlation_large[mode-mode]` | 1802 | 531.54 | 647.06 | 542.77 | 542.03 | 5.92 | 1.84e+03 |
| `test_bulk_correlation_large[mean-simple]` | 2190 | 442.34 | 555.39 | 445.89 | 444.91 | 5.45 | 2.24e+03 |
| `test_bulk_correlation_large[mode-mode]` | 72 | 13795.45 | 14098.01 | 13832.91 | 13823.53 | 42.28 | 7.23e+01 |
| `test_bulk_correlation_different_periods_large[5]` | 2730 | 343.00 | 528.17 | 345.76 | 344.65 | 7.79 | 2.89e+03 |
| `test_bulk_correlation_different_periods_large[50]` | 949 | 1014.77 | 1335.79 | 1021.13 | 1018.67 | 15.12 | 9.79e+02 |

---

#### Momentum Indicators

##### Small

TBD

##### Medium

TBD

##### Large

| Run Name | Rounds | Min (µs) | Max (µs) | Mean (µs) | Median (µs) | Stddev (µs) | Ops/sec |
|----|----|----|----|----|----|----|----|
| `test_single_rsi_large[simple]` | 13504 | 45.13 | 72.24 | 45.81 | 45.67 | 0.55 | 2.18e+04 |
| `test_single_rsi_large[mode]` | 7384 | 104.85 | 151.85 | 115.04 | 114.98 | 1.84 | 8.69e+03 |
| `test_bulk_rsi_large[simple]` | 1651 | 557.45 | 637.80 | 561.12 | 560.56 | 3.86 | 1.78e+03 |
| `test_bulk_rsi_large[mode]` | 274 | 3575.83 | 3744.26 | 3606.28 | 3607.11 | 14.12 | 2.77e+02 |
| `test_single_stoch_large` | 8745 | 80.11 | 113.28 | 80.95 | 80.67 | 1.27 | 1.24e+04 |
| `test_bulk_stoch_large` | 745 | 1173.21 | 1318.06 | 1225.38 | 1226.14 | 11.75 | 8.16e+02 |
| `test_single_slow_stoch_large[simple]` | 25246 | 35.70 | 135.48 | 36.07 | 36.00 | 0.83 | 2.77e+04 |
| `test_single_slow_stoch_large[mode]` | 9751 | 85.69 | 125.33 | 97.15 | 97.00 | 1.79 | 1.03e+04 |
| `test_bulk_slow_stoch_large[simple]` | 6696 | 120.30 | 177.26 | 121.55 | 121.33 | 1.82 | 8.23e+03 |
| `test_bulk_slow_stoch_large[mode]` | 377 | 2587.74 | 2780.20 | 2597.93 | 2596.05 | 12.97 | 3.85e+02 |
| `test_single_slowest_stoch_large[simple]` | 23643 | 36.19 | 62.72 | 36.57 | 36.50 | 0.64 | 2.73e+04 |
| `test_single_slowest_stoch_large[mode]` | 10844 | 85.93 | 182.67 | 96.43 | 96.37 | 1.86 | 1.04e+04 |
| `test_bulk_slowest_stoch_large[simple]` | 7208 | 108.13 | 156.74 | 109.17 | 108.91 | 1.82 | 9.16e+03 |
| `test_bulk_slowest_stoch_large[mode]` | 634 | 1510.25 | 1715.01 | 1518.90 | 1516.99 | 12.68 | 6.58e+02 |
| `test_single_williams_r_large` | 11704 | 77.37 | 117.93 | 78.48 | 78.48 | 1.01 | 1.27e+04 |
| `test_bulk_williams_r_large` | 3010 | 296.35 | 377.24 | 297.77 | 297.09 | 4.10 | 3.36e+03 |
| `test_single_mfi_large` | 10745 | 75.30 | 102.19 | 76.15 | 75.98 | 1.02 | 1.31e+04 |
| `test_bulk_mfi_large` | 1911 | 484.99 | 550.06 | 487.85 | 487.13 | 4.20 | 2.05e+03 |
| `test_single_roc_large` | 197824 | 0.11 | 0.79 | 0.11 | 0.11 | 0.00 | 8.72e+06 |
| `test_bulk_roc_large` | 9023 | 84.76 | 123.82 | 86.16 | 86.18 | 1.15 | 1.16e+04 |
| `test_single_obv_large` | 194932 | 0.12 | 0.71 | 0.13 | 0.13 | 0.00 | 7.85e+06 |
| `test_bulk_obv_large` | 6112 | 128.24 | 170.78 | 129.85 | 129.61 | 2.46 | 7.70e+03 |
| `test_single_cci_large[mean-simple]` | 21506 | 39.19 | 62.35 | 39.87 | 39.83 | 0.52 | 2.51e+04 |
| `test_single_cci_large[ulcer-mode]` | 145 | 6901.35 | 6994.56 | 6907.99 | 6906.17 | 9.33 | 1.45e+02 |
| `test_bulk_cci_large[mean-simple]` | 3842 | 230.67 | 317.85 | 232.68 | 232.28 | 3.52 | 4.30e+03 |
| `test_bulk_cci_large[mode-mode]` | 146 | 6790.98 | 7104.47 | 6834.63 | 6830.58 | 27.28 | 1.46e+02 |
| `test_single_mcginley_cci_large[mean]` | 22988 | 36.63 | 82.70 | 37.47 | 37.76 | 0.80 | 2.67e+04 |
| `test_single_mcginley_cci_large[ulcer]` | 147 | 6787.67 | 6856.71 | 6791.56 | 6790.00 | 7.66 | 1.47e+02 |
| `test_bulk_mcginley_cci_large[mean]` | 2937 | 292.08 | 420.15 | 295.23 | 294.26 | 7.74 | 3.39e+03 |
| `test_bulk_mcginley_cci_large[mode]` | 270 | 3626.82 | 3902.63 | 3651.63 | 3649.65 | 21.29 | 2.74e+02 |
| `test_single_macd_line_large[simple-smoothed]` | 23397 | 35.85 | 98.13 | 36.31 | 36.26 | 0.80 | 2.75e+04 |
| `test_single_macd_line_large[mode-simple]` | 5828 | 144.24 | 190.65 | 151.20 | 151.07 | 1.97 | 6.61e+03 |
| `test_bulk_macd_line_large[simple-simple]` | 4670 | 166.91 | 208.71 | 168.28 | 168.02 | 1.73 | 5.94e+03 |
| `test_bulk_macd_line_large[mode-mode]` | 174 | 5706.11 | 5880.22 | 5718.19 | 5714.60 | 18.77 | 1.75e+02 |
| `test_single_signal_line_large[simple]` | 22250 | 36.28 | 74.28 | 36.80 | 36.67 | 1.21 | 2.72e+04 |
| `test_single_signal_line_large[mode]` | 8684 | 100.39 | 159.02 | 110.31 | 110.17 | 2.51 | 9.07e+03 |
| `test_bulk_signal_line_large[simple]` | 7215 | 119.07 | 184.26 | 121.49 | 121.17 | 3.19 | 8.23e+03 |
| `test_bulk_signal_line_large[mode]` | 318 | 3097.50 | 3392.69 | 3111.16 | 3107.44 | 21.46 | 3.21e+02 |
| `test_single_mcginley_macd_line_large` | 24954 | 32.39 | 59.13 | 32.77 | 32.74 | 0.49 | 3.05e+04 |
| `test_bulk_mcginley_macd_line_large` | 854 | 297.76 | 422.98 | 301.42 | 299.20 | 11.33 | 3.32e+03 |
| `test_single_chaikin_osc_large[simple-simple]` | 5878 | 140.30 | 238.26 | 144.46 | 142.52 | 4.43 | 6.92e+03 |
| `test_single_chaikin_osc_large[mode-mode]` | 3261 | 288.96 | 420.87 | 295.70 | 294.98 | 6.89 | 3.38e+03 |
| `test_bulk_chaikin_osc_large[simple-simple]` | 489 | 505.09 | 788.49 | 514.40 | 507.85 | 33.18 | 1.94e+03 |
| `test_bulk_chaikin_osc_large[mode-mode]` | 335 | 2874.85 | 3438.02 | 2912.14 | 2889.94 | 57.21 | 3.43e+02 |
| `test_single_ppo_large[simple]` | 22671 | 35.59 | 71.68 | 35.98 | 35.93 | 0.56 | 2.78e+04 |
| `test_single_ppo_large[mode]` | 6160 | 144.61 | 195.72 | 151.32 | 151.15 | 2.05 | 6.61e+03 |
| `test_bulk_ppo_large[simple]` | 4638 | 174.93 | 224.59 | 176.19 | 175.87 | 2.00 | 5.68e+03 |
| `test_bulk_ppo_large[mode]` | 172 | 5680.49 | 5897.75 | 5748.07 | 5753.58 | 28.74 | 1.74e+02 |
| `test_single_cmo_large` | 14177 | 44.52 | 75.35 | 45.14 | 45.00 | 0.82 | 2.22e+04 |
| `test_bulk_cmo_large` | 1828 | 502.00 | 573.21 | 505.53 | 504.95 | 3.62 | 1.98e+03 |

---

#### Moving Average

##### Small 

| Run Name | Rounds | Min (µs) | Max (µs) | Mean (µs) | Median (µs) | Stddev (µs) | Ops/sec |
|----|----|----|----|----|----|----|----|
| `test_single_ma[small-simple]` | 50373 | 3.72 | 22.50 | 3.82 | 3.82 | 0.13 | 2.62e+05 |
| `test_single_ma[small-smoothed]` | 76811 | 6.52 | 36.76 | 6.64 | 6.63 | 0.24 | 1.51e+05 |
| `test_single_ma[small-exponential]` | 77586 | 6.43 | 30.41 | 6.55 | 6.54 | 0.21 | 1.53e+05 |
| `test_bulk_ma[small-simple]` | 54272 | 10.67 | 54.72 | 11.56 | 11.59 | 0.49 | 8.65e+04 |
| `test_bulk_ma[small-smoothed]` | 19362 | 39.02 | 140.22 | 39.65 | 39.54 | 1.08 | 2.52e+04 |
| `test_bulk_ma[small-exponential]` | 19839 | 39.31 | 83.11 | 39.75 | 39.65 | 0.80 | 2.52e+04 |
| `test_single_mcginley_dynamic[small]` | 195657 | 0.13 | 3.70 | 0.13 | 0.13 | 0.01 | 7.51e+06 |
| `test_bulk_mcginley_dynamic[small]` | 55216 | 10.93 | 52.00 | 11.63 | 11.69 | 0.44 | 8.60e+04 |

##### Medium

| Run Name | Rounds | Min (µs) | Max (µs) | Mean (µs) | Median (µs) | Stddev (µs) | Ops/sec |
|----|----|----|----|----|----|----|----|
| `test_single_ma[medium-simple]` | 31821 | 17.67 | 35.67 | 18.03 | 18.02 | 0.23 | 5.55e+04 |
| `test_single_ma[medium-smoothed]` | 23643 | 35.87 | 60.15 | 36.31 | 36.28 | 0.44 | 2.75e+04 |
| `test_single_ma[medium-exponential]` | 23519 | 35.91 | 56.65 | 36.19 | 36.15 | 0.44 | 2.76e+04 |
| `test_bulk_ma[medium-simple]` | 10670 | 57.37 | 141.78 | 58.10 | 57.93 | 1.16 | 1.72e+04 |
| `test_bulk_ma[medium-smoothed]` | 4525 | 204.63 | 257.80 | 207.80 | 206.96 | 2.50 | 4.81e+03 |
| `test_bulk_ma[medium-exponential]` | 4496 | 205.98 | 255.43 | 207.69 | 207.35 | 1.82 | 4.81e+03 |
| `test_single_mcginley_dynamic[medium]` | 192197 | 0.13 | 0.77 | 0.13 | 0.13 | 0.00 | 7.77e+06 |
| `test_bulk_mcginley_dynamic[medium]` | 12483 | 58.39 | 99.87 | 59.23 | 59.17 | 0.87 | 1.69e+04 |

##### Large

| Run Name | Rounds | Min (µs) | Max (µs) | Mean (µs) | Median (µs) | Stddev (µs) | Ops/sec |
|----|----|----|----|----|----|----|----|
| `test_single_ma[large-simple]` | 16818 | 34.63 | 53.24 | 35.64 | 35.61 | 0.32 | 2.81e+04 |
| `test_single_ma[large-smoothed]` | 11897 | 76.83 | 110.46 | 77.76 | 77.69 | 0.78 | 1.29e+04 |
| `test_single_ma[large-exponential]` | 11913 | 76.85 | 125.93 | 77.47 | 77.43 | 0.79 | 1.29e+04 |
| `test_bulk_ma[large-simple]` | 6242 | 114.74 | 160.09 | 115.62 | 115.39 | 1.53 | 8.65e+03 |
| `test_bulk_ma[large-smoothed]` | 2310 | 410.50 | 478.28 | 415.83 | 414.47 | 4.02 | 2.40e+03 |
| `test_bulk_ma[large-exponential]` | 2226 | 412.89 | 492.30 | 416.53 | 415.67 | 4.24 | 2.40e+03 |
| `test_single_mcginley_dynamic[large]` | 197785 | 0.13 | 2.72 | 0.13 | 0.13 | 0.01 | 7.71e+06 |
| `test_bulk_mcginley_dynamic[large]` | 6778 | 118.04 | 174.87 | 118.98 | 118.74 | 1.61 | 8.41e+03 |

---

#### Other Indicators

##### Small

| Run Name | Rounds | Min (µs) | Max (µs) | Mean (µs) | Median (µs) | Stddev (µs) | Ops/sec |
|----|----|----|----|----|----|----|----|
| `test_single_true_range[small]` | 86394 | 0.11 | 2.24 | 0.12 | 0.11 | 0.01 | 8.68e+06 |
| `test_bulk_true_range[small]` | 45377 | 14.94 | 115.06 | 15.92 | 15.93 | 1.76 | 6.28e+04 |
| `test_single_atr[small-simple]` | 55670 | 11.24 | 112.91 | 11.52 | 11.46 | 1.32 | 8.68e+04 |
| `test_single_atr[small-mode]` | 35043 | 17.70 | 123.54 | 18.96 | 18.89 | 1.70 | 5.28e+04 |
| `test_bulk_atr[small-simple]` | 26484 | 31.56 | 116.78 | 32.65 | 32.49 | 2.21 | 3.06e+04 |
| `test_bulk_atr[small-mode]` | 2584 | 295.24 | 407.24 | 300.18 | 298.62 | 7.37 | 3.33e+03 |
| `test_single_roi[small]` | 163640 | 0.16 | 2.39 | 0.16 | 0.16 | 0.03 | 6.18e+06 |
| `test_bulk_roi[small]` | 23716 | 21.74 | 139.43 | 22.60 | 22.33 | 2.22 | 4.42e+04 |
| `test_single_ibs[small]` | 80594 | 0.11 | 1.22 | 0.11 | 0.11 | 0.01 | 8.71e+06 |
| `test_bulk_ibs[small]` | 42454 | 15.02 | 217.67 | 16.10 | 16.11 | 1.95 | 6.21e+04 |
| `test_bulk_positivity[small-simple]` | 24435 | 24.70 | 290.37 | 26.04 | 25.80 | 2.93 | 3.84e+04 |
| `test_bulk_positivity[small-mode]` | 6495 | 116.24 | 224.85 | 122.02 | 121.02 | 6.63 | 8.20e+03 |

##### Medium

| Run Name | Rounds | Min (µs) | Max (µs) | Mean (µs) | Median (µs) | Stddev (µs) | Ops/sec |
|----|----|----|----|----|----|----|----|
| `test_single_true_range[medium]` | 185564 | 0.12 | 1.06 | 0.12 | 0.12 | 0.00 | 8.41e+06 |
| `test_bulk_true_range[medium]` | 10181 | 73.98 | 121.31 | 74.92 | 74.72 | 1.39 | 1.33e+04 |
| `test_single_atr[medium-simple]` | 16034 | 52.52 | 99.19 | 53.07 | 52.94 | 0.92 | 1.88e+04 |
| `test_single_atr[medium-mode]` | 10347 | 79.56 | 139.59 | 85.30 | 85.26 | 1.71 | 1.17e+04 |
| `test_bulk_atr[medium-simple]` | 4905 | 165.11 | 219.00 | 167.87 | 167.61 | 2.05 | 5.96e+03 |
| `test_bulk_atr[medium-mode]` | 617 | 1569.29 | 1744.64 | 1591.80 | 1592.21 | 13.98 | 6.28e+02 |
| `test_single_roi[medium]` | 186847 | 0.16 | 1.32 | 0.16 | 0.16 | 0.01 | 6.07e+06 |
| `test_bulk_roi[medium]` | 576 | 109.70 | 188.32 | 112.24 | 110.46 | 5.87 | 8.91e+03 |
| `test_single_ibs[medium]` | 194932 | 0.12 | 0.91 | 0.12 | 0.12 | 0.00 | 8.35e+06 |
| `test_bulk_ibs[medium]` | 10178 | 75.93 | 159.61 | 76.89 | 76.67 | 1.48 | 1.30e+04 |
| `test_bulk_positivity[medium-simple]` | 6103 | 120.11 | 218.93 | 122.39 | 121.96 | 3.80 | 8.17e+03 |
| `test_bulk_positivity[medium-mode]` | 1671 | 560.35 | 812.63 | 569.23 | 563.00 | 25.19 | 1.76e+03 |

##### Large

| Run Name | Rounds | Min (µs) | Max (µs) | Mean (µs) | Median (µs) | Stddev (µs) | Ops/sec |
|----|----|----|----|----|----|----|----|
| `test_single_true_range[large]` | 200000 | 0.12 | 1.64 | 0.12 | 0.12 | 0.01 | 8.40e+06 |
| `test_bulk_true_range[large]` | 4738 | 148.94 | 251.78 | 150.73 | 149.96 | 5.05 | 6.63e+03 |
| `test_single_atr[large-simple]` | 8875 | 103.32 | 158.67 | 104.43 | 104.28 | 1.92 | 9.58e+03 |
| `test_single_atr[large-mode]` | 5384 | 157.67 | 258.91 | 168.48 | 168.40 | 3.67 | 5.94e+03 |
| `test_bulk_atr[large-simple]` | 2744 | 329.19 | 426.97 | 335.06 | 334.32 | 5.66 | 2.98e+03 |
| `test_bulk_atr[large-mode]` | 301 | 3259.09 | 3539.54 | 3304.23 | 3281.72 | 41.93 | 3.03e+02 |
| `test_single_roi[large]` | 192160 | 0.26 | 10.13 | 0.29 | 0.28 | 0.05 | 3.51e+06 |
| `test_bulk_roi[large]` | 460 | 228.78 | 353.78 | 235.49 | 230.30 | 18.80 | 4.25e+03 |
| `test_single_ibs[large]` | 197084 | 0.12 | 1.09 | 0.12 | 0.12 | 0.00 | 8.43e+06 |
| `test_bulk_ibs[large]` | 4570 | 150.93 | 2043.16 | 153.95 | 153.13 | 28.36 | 6.50e+03 |
| `test_bulk_positivity[large-simple]` | 244 | 253.93 | 608.54 | 275.95 | 256.04 | 68.12 | 3.62e+03 |
| `test_bulk_positivity[large-mode]` | 788 | 1171.91 | 1896.51 | 1183.23 | 1177.15 | 49.04 | 8.45e+02 |

---

#### Standard Indicators

##### Small

| Run Name | Rounds | Min (µs) | Max (µs) | Mean (µs) | Median (µs) | Stddev (µs) | Ops/sec |
|----|----|----|----|----|----|----|----|
| `test_single_sma[small]` | 50610 | 3.72 | 49.04 | 3.83 | 3.81 | 0.73 | 2.61e+05 |
| `test_bulk_sma[small]` | 39301 | 10.74 | 225.91 | 11.45 | 11.41 | 2.04 | 8.74e+04 |
| `test_single_smma[small]` | 86814 | 6.37 | 345.80 | 6.66 | 6.50 | 3.50 | 1.50e+05 |
| `test_bulk_smma[small]` | 22959 | 38.07 | 280.78 | 39.13 | 38.93 | 2.77 | 2.56e+04 |
| `test_single_ema[small]` | 98184 | 6.43 | 256.67 | 6.57 | 6.54 | 1.22 | 1.52e+05 |
| `test_bulk_ema[small]` | 20165 | 38.59 | 126.68 | 39.55 | 39.28 | 2.39 | 2.53e+04 |
| `test_single_bollinger[small]` | 82190 | 0.57 | 5.90 | 0.61 | 0.61 | 0.06 | 1.63e+06 |
| `test_bulk_bollinger[small]` | 17292 | 36.22 | 258.06 | 37.40 | 37.20 | 2.88 | 2.67e+04 |
| `test_single_macd[small]` | 118428 | 3.18 | 282.65 | 3.27 | 3.24 | 1.06 | 3.06e+05 |
| `test_bulk_macd[small]` | 1729 | 552.22 | 687.36 | 558.35 | 555.80 | 9.94 | 1.79e+03 |
| `test_single_rsi[small]` | 88379 | 0.54 | 5.60 | 0.58 | 0.58 | 0.06 | 1.72e+06 |
| `test_bulk_rsi[small]` | 14336 | 59.07 | 181.28 | 60.00 | 59.68 | 3.08 | 1.67e+04 |

##### Medium

| Run Name | Rounds | Min (µs) | Max (µs) | Mean (µs) | Median (µs) | Stddev (µs) | Ops/sec |
|----|----|----|----|----|----|----|----|
| `test_single_sma[medium]` | 33068 | 17.54 | 37.93 | 17.89 | 17.89 | 0.28 | 5.59e+04 |
| `test_bulk_sma[medium]` | 12700 | 57.65 | 93.39 | 58.42 | 58.32 | 0.92 | 1.71e+04 |
| `test_single_smma[medium]` | 23852 | 35.82 | 90.22 | 36.09 | 36.04 | 0.63 | 2.77e+04 |
| `test_bulk_smma[medium]` | 4272 | 202.37 | 304.20 | 204.88 | 204.61 | 2.61 | 4.88e+03 |
| `test_single_ema[medium]` | 22728 | 35.82 | 64.35 | 36.21 | 36.17 | 0.52 | 2.76e+04 |
| `test_bulk_ema[medium]` | 4445 | 204.93 | 246.65 | 207.10 | 207.17 | 1.73 | 4.83e+03 |
| `test_single_bollinger[medium]` | 165646 | 0.68 | 27.69 | 0.73 | 0.72 | 0.12 | 1.37e+06 |
| `test_bulk_bollinger[medium]` | 381 | 192.50 | 251.08 | 196.26 | 193.45 | 8.02 | 5.10e+03 |
| `test_single_macd[medium]` | 104855 | 3.18 | 80.74 | 3.27 | 3.26 | 0.33 | 3.06e+05 |
| `test_bulk_macd[medium]` | 318 | 3092.46 | 3294.79 | 3136.57 | 3146.56 | 23.73 | 3.19e+02 |
| `test_single_rsi[medium]` | 174734 | 0.65 | 25.80 | 0.70 | 0.69 | 0.12 | 1.44e+06 |
| `test_bulk_rsi[medium]` | 2969 | 317.91 | 367.97 | 320.73 | 320.35 | 2.19 | 3.12e+03 |

##### Large

| Run Name | Rounds | Min (µs) | Max (µs) | Mean (µs) | Median (µs) | Stddev (µs) | Ops/sec |
|----|----|----|----|----|----|----|----|
| `test_single_sma[large]` | 14631 | 36.19 | 104.61 | 36.75 | 36.48 | 3.33 | 2.72e+04 |
| `test_bulk_sma[large]` | 6357 | 115.37 | 216.06 | 117.48 | 116.41 | 7.20 | 8.51e+03 |
| `test_single_smma[large]` | 12154 | 78.04 | 264.19 | 79.42 | 78.83 | 5.63 | 1.26e+04 |
| `test_bulk_smma[large]` | 2228 | 408.34 | 602.71 | 416.07 | 413.32 | 14.81 | 2.40e+03 |
| `test_single_ema[large]` | 12492 | 77.96 | 255.22 | 79.29 | 78.72 | 5.44 | 1.26e+04 |
| `test_bulk_ema[large]` | 2185 | 412.97 | 719.08 | 420.28 | 417.06 | 15.11 | 2.38e+03 |
| `test_single_bollinger[large]` | 164637 | 0.67 | 58.98 | 0.72 | 0.70 | 0.53 | 1.38e+06 |
| `test_bulk_bollinger[large]` | 376 | 395.41 | 695.60 | 405.92 | 396.95 | 30.66 | 2.46e+03 |
| `test_single_macd[large]` | 100181 | 3.17 | 183.57 | 3.28 | 3.26 | 1.11 | 3.05e+05 |
| `test_bulk_macd[large]` | 158 | 6278.97 | 6910.83 | 6359.96 | 6353.39 | 68.80 | 1.57e+02 |
| `test_single_rsi[large]` | 156986 | 0.65 | 57.35 | 0.70 | 0.69 | 0.49 | 1.43e+06 |
| `test_bulk_rsi[large]` | 1475 | 647.78 | 780.19 | 656.96 | 651.97 | 17.29 | 1.52e+03 |

---

#### Strength Indicators

##### Small

| Run Name | Rounds | Min (µs) | Max (µs) | Mean (µs) | Median (µs) | Stddev (µs) | Ops/sec |
|----|----|----|----|----|----|----|----|
| `test_single_volume_index[small]` | 84374 | 0.11 | 1.10 | 0.12 | 0.12 | 0.01 | 8.65e+06 |
| `test_bulk_accumulation_distribution[small]` | 38083 | 18.85 | 137.98 | 19.99 | 19.95 | 1.98 | 5.00e+04 |
| `test_bulk_positive_volume_index[small]` | 51333 | 11.63 | 158.91 | 12.67 | 12.74 | 1.62 | 7.89e+04 |
| `test_bulk_negative_volume_index[small]` | 39970 | 12.57 | 134.24 | 13.15 | 13.00 | 1.78 | 7.60e+04 |
| `test_single_rvi[small-simple]` | 42286 | 16.78 | 126.89 | 17.44 | 17.35 | 1.72 | 5.73e+04 |
| `test_single_rvi[small-mode]` | 24086 | 29.98 | 179.82 | 32.23 | 32.37 | 2.48 | 3.10e+04 |
| `test_bulk_rvi[small-simple]` | 8160 | 99.41 | 215.07 | 105.01 | 104.48 | 4.04 | 9.52e+03 |
| `test_bulk_rvi[small-mode]` | 1697 | 512.82 | 756.30 | 523.15 | 519.10 | 12.50 | 1.91e+03 |

##### Medium

| Run Name | Rounds | Min (µs) | Max (µs) | Mean (µs) | Median (µs) | Stddev (µs) | Ops/sec |
|----|----|----|----|----|----|----|----|
| `test_single_volume_index[medium]` | 196348 | 0.12 | 3.88 | 0.12 | 0.12 | 0.01 | 8.08e+06 |
| `test_bulk_accumulation_distribution[medium]` | 8294 | 92.22 | 271.93 | 94.05 | 93.80 | 2.78 | 1.06e+04 |
| `test_bulk_positive_volume_index[medium]` | 11576 | 60.46 | 228.58 | 61.13 | 60.93 | 2.09 | 1.64e+04 |
| `test_bulk_negative_volume_index[medium]` | 12800 | 61.41 | 111.11 | 62.36 | 62.19 | 1.36 | 1.60e+04 |
| `test_single_rvi[medium-simple]` | 10456 | 82.78 | 162.70 | 84.92 | 84.72 | 1.85 | 1.18e+04 |
| `test_single_rvi[medium-mode]` | 6171 | 135.72 | 219.11 | 148.00 | 148.00 | 3.03 | 6.76e+03 |
| `test_bulk_rvi[medium-simple]` | 1757 | 523.52 | 667.93 | 550.46 | 549.78 | 6.59 | 1.82e+03 |
| `test_bulk_rvi[medium-mode]` | 353 | 2747.57 | 2984.01 | 2791.60 | 2784.38 | 21.02 | 3.58e+02 |

##### Large

| Run Name | Rounds | Min (µs) | Max (µs) | Mean (µs) | Median (µs) | Stddev (µs) | Ops/sec |
|----|----|----|----|----|----|----|----|
| `test_single_volume_index[large]` | 83592 | 0.11 | 1.43 | 0.12 | 0.12 | 0.01 | 8.63e+06 |
| `test_bulk_accumulation_distribution[large]` | 4041 | 188.59 | 472.28 | 191.33 | 189.65 | 9.85 | 5.23e+03 |
| `test_bulk_positive_volume_index[large]` | 6318 | 120.74 | 312.89 | 122.40 | 121.46 | 5.99 | 8.17e+03 |
| `test_bulk_negative_volume_index[large]` | 6885 | 121.89 | 305.13 | 124.05 | 123.17 | 6.47 | 8.06e+03 |
| `test_single_rvi[large-simple]` | 5609 | 161.59 | 332.09 | 166.62 | 165.28 | 8.08 | 6.00e+03 |
| `test_single_rvi[large-mode]` | 3229 | 272.63 | 441.61 | 295.38 | 293.63 | 10.96 | 3.39e+03 |
| `test_bulk_rvi[large-simple]` | 859 | 1059.65 | 1309.60 | 1116.23 | 1109.76 | 20.01 | 8.96e+02 |
| `test_bulk_rvi[large-mode]` | 178 | 5553.12 | 6108.55 | 5652.71 | 5648.68 | 48.61 | 1.77e+02 |

---

#### Trend Indicators

#### Small

| Run Name | Rounds | Min (µs) | Max (µs) | Mean (µs) | Median (µs) | Stddev (µs) | Ops/sec |
|----|----|----|----|----|----|----|----|
| `test_single_aroon_oscillator[medium]` | 91836 | 0.10 | 1.22 | 0.11 | 0.11 | 0.01 | 9.27e+06 |
| `test_bulk_aroon_up[medium]` | 8633 | 91.09 | 319.17 | 92.10 | 91.56 | 4.48 | 1.09e+04 |
| `test_single_aroon_down[medium]` | 41474 | 20.04 | 145.06 | 20.35 | 20.24 | 1.80 | 4.91e+04 |
| `test_bulk_aroon_down[medium]` | 8638 | 97.52 | 224.21 | 98.62 | 98.02 | 4.30 | 1.01e+04 |
| `test_single_long_parabolic[medium]` | 194970 | 0.12 | 2.61 | 0.12 | 0.12 | 0.02 | 8.09e+06 |
| `test_bulk_parabolic[long-medium]` | 5336 | 155.08 | 357.64 | 159.42 | 158.50 | 5.91 | 6.27e+03 |
| `test_bulk_dms[simple-medium]` | 362 | 231.08 | 523.56 | 241.76 | 232.95 | 29.93 | 4.14e+03 |
| `test_bulk_dms[mode-medium]` | 747 | 1194.00 | 1490.38 | 1212.86 | 1205.43 | 26.22 | 8.25e+02 |
| `test_single_tsi[medium-simple-simple]` | 13210 | 70.02 | 229.43 | 70.76 | 70.37 | 3.43 | 1.41e+04 |
| `test_single_tsi[medium-simple-mode]` | 277 | 3555.73 | 3656.99 | 3569.14 | 3567.65 | 9.63 | 2.80e+02 |
| `test_bulk_tsi[medium-simple-simple]` | 896 | 1100.20 | 1174.09 | 1104.37 | 1103.91 | 4.31 | 9.05e+02 |
| `test_bulk_tsi[medium-simple-mode]` | 22 | 46977.34 | 47163.53 | 47054.78 | 47050.67 | 44.80 | 2.13e+01 |
| `test_single_vpt[medium]` | 197785 | 0.12 | 3.62 | 0.12 | 0.12 | 0.02 | 8.03e+06 |
| `test_bulk_vpt[medium]` | 12599 | 58.54 | 204.02 | 59.92 | 59.65 | 3.55 | 1.67e+04 |

#### Medium

| Run Name | Rounds | Min (µs) | Max (µs) | Mean (µs) | Median (µs) | Stddev (µs) | Ops/sec |
|----|----|----|----|----|----|----|----|
| `test_single_aroon_oscillator[medium]` | 91836 | 0.10 | 1.22 | 0.11 | 0.11 | 0.01 | 9.27e+06 |
| `test_bulk_aroon_up[medium]` | 8633 | 91.09 | 319.17 | 92.10 | 91.56 | 4.48 | 1.09e+04 |
| `test_single_aroon_down[medium]` | 41474 | 20.04 | 145.06 | 20.35 | 20.24 | 1.80 | 4.91e+04 |
| `test_bulk_aroon_down[medium]` | 8638 | 97.52 | 224.21 | 98.62 | 98.02 | 4.30 | 1.01e+04 |
| `test_single_long_parabolic[medium]` | 194970 | 0.12 | 2.61 | 0.12 | 0.12 | 0.02 | 8.09e+06 |
| `test_bulk_parabolic[long-medium]` | 5336 | 155.08 | 357.64 | 159.42 | 158.50 | 5.91 | 6.27e+03 |
| `test_bulk_dms[simple-medium]` | 362 | 231.08 | 523.56 | 241.76 | 232.95 | 29.93 | 4.14e+03 |
| `test_bulk_dms[mode-medium]` | 747 | 1194.00 | 1490.38 | 1212.86 | 1205.43 | 26.22 | 8.25e+02 |
| `test_single_tsi[medium-simple-simple]` | 13210 | 70.02 | 229.43 | 70.76 | 70.37 | 3.43 | 1.41e+04 |
| `test_single_tsi[medium-simple-mode]` | 277 | 3555.73 | 3656.99 | 3569.14 | 3567.65 | 9.63 | 2.80e+02 |
| `test_bulk_tsi[medium-simple-simple]` | 896 | 1100.20 | 1174.09 | 1104.37 | 1103.91 | 4.31 | 9.05e+02 |
| `test_bulk_tsi[medium-simple-mode]` | 22 | 46977.34 | 47163.53 | 47054.78 | 47050.67 | 44.80 | 2.13e+01 |
| `test_single_vpt[medium]` | 197785 | 0.12 | 3.62 | 0.12 | 0.12 | 0.02 | 8.03e+06 |
| `test_bulk_vpt[medium]` | 12599 | 58.54 | 204.02 | 59.92 | 59.65 | 3.55 | 1.67e+04 |

##### Large

| Run Name | Rounds | Min (µs) | Max (µs) | Mean (µs) | Median (µs) | Stddev (µs) | Ops/sec |
|----|----|----|----|----|----|----|----|
| `test_single_aroon_oscillator[large]` | 85035 | 0.11 | 1.70 | 0.11 | 0.11 | 0.01 | 8.80e+06 |
| `test_bulk_aroon_up[large]` | 4510 | 184.37 | 430.23 | 186.17 | 184.91 | 7.21 | 5.37e+03 |
| `test_single_aroon_down[large]` | 20809 | 40.41 | 248.00 | 40.95 | 40.69 | 2.99 | 2.44e+04 |
| `test_bulk_aroon_down[large]` | 4272 | 196.04 | 487.71 | 198.27 | 197.06 | 7.67 | 5.04e+03 |
| `test_single_long_parabolic[large]` | 194251 | 0.12 | 2.56 | 0.13 | 0.13 | 0.02 | 7.84e+06 |
| `test_bulk_parabolic[long-large]` | 2591 | 338.43 | 699.57 | 344.41 | 341.84 | 12.85 | 2.90e+03 |
| `test_bulk_dms[simple-large]` | 106 | 481.47 | 1374.71 | 541.15 | 487.58 | 158.03 | 1.85e+03 |
| `test_bulk_dms[mode-large]` | 403 | 2394.61 | 3151.40 | 2424.95 | 2408.45 | 53.86 | 4.12e+02 |
| `test_single_tsi[large-simple-simple]` | 6649 | 140.91 | 357.69 | 142.20 | 141.39 | 5.50 | 7.03e+03 |
| `test_single_tsi[large-simple-mode]` | 142 | 7019.85 | 7282.04 | 7059.82 | 7064.77 | 29.61 | 1.42e+02 |
| `test_bulk_tsi[large-simple-simple]` | 430 | 2235.64 | 2547.61 | 2251.27 | 2242.19 | 24.20 | 4.44e+02 |
| `test_bulk_tsi[large-simple-mode]` | 11 | 95097.01 | 96275.36 | 95418.25 | 95178.38 | 405.93 | 1.05e+01 |
| `test_single_vpt[large]` | 197785 | 0.12 | 2.36 | 0.13 | 0.13 | 0.02 | 7.81e+06 |
| `test_bulk_vpt[large]` | 6288 | 116.96 | 321.36 | 118.75 | 117.87 | 6.00 | 8.42e+03 |

---

#### Volatiltiy Indicators

##### Small

| Run Name | Rounds | Min (µs) | Max (µs) | Mean (µs) | Median (µs) | Stddev (µs) | Ops/sec |
|----|----|----|----|----|----|----|----|
| `test_bulk_volatility_system[small-simple]` | 18225 | 32.67 | 165.74 | 33.61 | 33.37 | 2.58 | 2.98e+04 |
| `test_bulk_volatility_system[small-mode]` | 4074 | 210.10 | 306.21 | 217.65 | 216.46 | 6.20 | 4.59e+03 |
| `test_single_ulcer_index[small]` | 12591 | 67.81 | 110.58 | 68.21 | 67.93 | 2.75 | 1.47e+04 |
| `test_bulk_ulcer_index[small]` | 10508 | 90.02 | 273.06 | 90.82 | 90.35 | 3.86 | 1.10e+04 |

##### Medium

| Run Name | Rounds | Min (µs) | Max (µs) | Mean (µs) | Median (µs) | Stddev (µs) | Ops/sec |
|----|----|----|----|----|----|----|----|
| `test_bulk_volatility_system[medium-simple]` | 4961 | 162.71 | 527.14 | 166.19 | 164.69 | 9.01 | 6.02e+03 |
| `test_bulk_volatility_system[medium-mode]` | 863 | 1113.10 | 1321.52 | 1126.33 | 1119.94 | 19.42 | 8.88e+02 |
| `test_single_ulcer_index[medium]` | 585 | 1697.69 | 2104.08 | 1721.55 | 1702.17 | 53.06 | 5.81e+02 |
| `test_bulk_ulcer_index[medium]` | 1994 | 477.67 | 626.60 | 482.34 | 478.99 | 11.38 | 2.07e+03 |

##### Large

| Run Name | Rounds | Min (µs) | Max (µs) | Mean (µs) | Median (µs) | Stddev (µs) | Ops/sec |
|----|----|----|----|----|----|----|----|
| `test_bulk_volatility_system[large-simple]` | 2600 | 326.17 | 520.64 | 332.47 | 328.93 | 15.31 | 3.01e+03 |
| `test_bulk_volatility_system[large-mode]` | 432 | 2255.08 | 2805.16 | 2284.26 | 2267.51 | 40.47 | 4.38e+02 |
| `test_single_ulcer_index[large]` | 146 | 6792.26 | 6883.00 | 6835.86 | 6853.75 | 28.69 | 1.46e+02 |
| `test_bulk_ulcer_index[large]` | 991 | 961.92 | 1105.03 | 971.76 | 964.42 | 19.92 | 1.03e+03 |

---

## 📚 About This Repo

This repository is part of a structured documentation suite:

- 📕 **Tutorials:** — [See here](https://github.com/ChironMind/PyTechnicalIndicators_Tutorials)
- 📘 **How-To Guides:** — [See here](https://github.com/ChironMind/PyTechnicalIndicators-How-To-guides)
- ⏱️ **Benchmarks:** This repo!
- 📙 **Explanations:** — Coming soon
- 📗 **Reference:** — [See here](https://github.com/ChironMind/PyTechnicalIndicators/wiki)

---


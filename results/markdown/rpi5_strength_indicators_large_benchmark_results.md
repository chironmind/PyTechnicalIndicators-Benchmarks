| Run Name | Rounds | Min (µs) | Max (µs) | Mean (µs) | Median (µs) | Stddev (µs) | Ops/sec |
|----|----|----|----|----|----|----|----|
| `test_single_accumulation_distribution[large]` | 185564 | 0.22 | 43.57 | 0.25 | 0.24 | 0.20 | 4.07e+06 |
| `test_bulk_accumulation_distribution[large]` | 4041 | 188.59 | 472.28 | 191.33 | 189.65 | 9.85 | 5.23e+03 |
| `test_single_volume_index[large]` | 83592 | 0.11 | 1.43 | 0.12 | 0.12 | 0.01 | 8.63e+06 |
| `test_bulk_positive_volume_index[large]` | 6318 | 120.74 | 312.89 | 122.40 | 121.46 | 5.99 | 8.17e+03 |
| `test_bulk_negative_volume_index[large]` | 6885 | 121.89 | 305.13 | 124.05 | 123.17 | 6.47 | 8.06e+03 |
| `test_single_rvi[large-simple]` | 5609 | 161.59 | 332.09 | 166.62 | 165.28 | 8.08 | 6.00e+03 |
| `test_single_rvi[large-smoothed]` | 3797 | 247.08 | 542.09 | 252.97 | 251.06 | 10.27 | 3.95e+03 |
| `test_single_rvi[large-exponential]` | 3871 | 244.17 | 394.35 | 250.83 | 249.00 | 9.53 | 3.99e+03 |
| `test_single_rvi[large-median]` | 3066 | 258.78 | 525.72 | 266.46 | 263.59 | 14.35 | 3.75e+03 |
| `test_single_rvi[large-mode]` | 3229 | 272.63 | 441.61 | 295.38 | 293.63 | 10.96 | 3.39e+03 |
| `test_bulk_rvi[large-simple]` | 859 | 1059.65 | 1309.60 | 1116.23 | 1109.76 | 20.01 | 8.96e+02 |
| `test_bulk_rvi[large-smoothed]` | 631 | 1552.53 | 1993.08 | 1611.38 | 1603.38 | 25.68 | 6.21e+02 |
| `test_bulk_rvi[large-exponential]` | 604 | 1593.45 | 1773.27 | 1607.70 | 1599.88 | 20.31 | 6.22e+02 |
| `test_bulk_rvi[large-median]` | 317 | 3063.53 | 3505.44 | 3163.21 | 3155.57 | 40.78 | 3.16e+02 |
| `test_bulk_rvi[large-mode]` | 178 | 5553.12 | 6108.55 | 5652.71 | 5648.68 | 48.61 | 1.77e+02 |

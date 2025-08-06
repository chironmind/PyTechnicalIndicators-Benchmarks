"""Benchmark tests for chart trends (all dataset sizes and all parameter variations)"""
import pytest
from pytechnicalindicators import chart_trends
from data_constants import get_test_data

data_sizes = ["small", "medium", "large"]

class TestPeaks:
    @pytest.mark.benchmark(group="peaks")
    @pytest.mark.parametrize("data_size", data_sizes)
    @pytest.mark.parametrize("closest_neighbor", [1, 5, 10])
    def test_peaks(self, benchmark, data_size, closest_neighbor):
        data = get_test_data(data_size)
        period = min(50, len(data['close']))
        result = benchmark(chart_trends.peaks, data['close'], period, closest_neighbor)
        assert isinstance(result, list)

class TestValleys:
    @pytest.mark.benchmark(group="valleys")
    @pytest.mark.parametrize("data_size", data_sizes)
    @pytest.mark.parametrize("closest_neighbor", [1, 5, 10])
    def test_valleys(self, benchmark, data_size, closest_neighbor):
        data = get_test_data(data_size)
        period = min(50, len(data['close']))
        result = benchmark(chart_trends.valleys, data['close'], period, closest_neighbor)
        assert isinstance(result, list)

class TestPeakTrend:
    @pytest.mark.benchmark(group="peak_trend")
    @pytest.mark.parametrize("data_size", data_sizes)
    @pytest.mark.parametrize("period", [3, 5, 10, 20])
    def test_peak_trend(self, benchmark, data_size, period):
        data = get_test_data(data_size)
        result = benchmark(chart_trends.peak_trend, data['close'], period)
        assert isinstance(result, tuple) and len(result) == 2

class TestValleyTrend:
    @pytest.mark.benchmark(group="valley_trend")
    @pytest.mark.parametrize("data_size", data_sizes)
    @pytest.mark.parametrize("period", [3, 5, 10, 20])
    def test_valley_trend(self, benchmark, data_size, period):
        data = get_test_data(data_size)
        result = benchmark(chart_trends.valley_trend, data['close'], period)
        assert isinstance(result, tuple) and len(result) == 2

class TestOverallTrend:
    @pytest.mark.benchmark(group="overall_trend")
    @pytest.mark.parametrize("data_size", data_sizes)
    def test_overall_trend(self, benchmark, data_size):
        data = get_test_data(data_size)
        result = benchmark(chart_trends.overall_trend, data['close'])
        assert isinstance(result, tuple) and len(result) == 2

class TestBreakDownTrends:
    @pytest.mark.benchmark(group="break_down_trends")
    @pytest.mark.parametrize("data_size", data_sizes)
    @pytest.mark.parametrize("max_outliers", [0, 1, 2])
    @pytest.mark.parametrize("soft_r2", [0.5, 0.75])
    @pytest.mark.parametrize("hard_r2", [1.0, 1.5])
    def test_break_down_trends(self, benchmark, data_size, max_outliers, soft_r2, hard_r2):
        data = get_test_data(data_size)
        result = benchmark(
            chart_trends.break_down_trends,
            data['close'],
            max_outliers,
            soft_r2, 1.0,
            soft_r2-0.2, hard_r2,
            2.0, 3.0, 2.0, 3.0
        )
        assert isinstance(result, list)

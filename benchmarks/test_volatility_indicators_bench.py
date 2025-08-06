"""Benchmark tests for volatility_indicators (single and bulk, all dataset sizes and parameter variations)"""
import pytest
from pytechnicalindicators import volatility_indicators
from data_constants import get_test_data

ma_types = ["simple", "smoothed", "exponential", "median", "mode"]
data_sizes = ["small", "medium", "large"]

class TestUlcerIndex:
    @pytest.mark.benchmark(group="ulcer_index_single")
    @pytest.mark.parametrize("data_size", data_sizes)
    def test_single_ulcer_index(self, benchmark, data_size):
        data = get_test_data(data_size)
        result = benchmark(volatility_indicators.single.ulcer_index, data['close'])
        assert isinstance(result, float)

    @pytest.mark.benchmark(group="ulcer_index_bulk")
    @pytest.mark.parametrize("data_size", data_sizes)
    def test_bulk_ulcer_index(self, benchmark, data_size):
        data = get_test_data(data_size)
        period = min(20, len(data['close']))
        result = benchmark(volatility_indicators.bulk.ulcer_index, data['close'], period)
        assert isinstance(result, list)

@pytest.mark.parametrize("ma_type", ma_types)
@pytest.mark.parametrize("data_size", data_sizes)
class TestVolatilitySystem:
    @pytest.mark.benchmark(group="volatility_system_bulk")
    def test_bulk_volatility_system(self, benchmark, data_size, ma_type):
        data = get_test_data(data_size)
        period = min(14, len(data['close']), len(data['high']), len(data['low']))
        multiplier = 2.0
        result = benchmark(
            volatility_indicators.bulk.volatility_system,
            data['high'], data['low'], data['close'], period, multiplier, ma_type
        )
        assert isinstance(result, list)

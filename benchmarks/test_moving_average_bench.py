"""Benchmark tests for moving average indicators (single and bulk, all dataset sizes and MA types)"""
import pytest
from pytechnicalindicators import moving_average
from data_constants import get_test_data

ma_types = ["simple", "smoothed", "exponential"]
data_sizes = ["small", "medium", "large"]

@pytest.mark.parametrize("ma_type", ma_types)
@pytest.mark.parametrize("data_size", data_sizes)
class TestMovingAverage:
    @pytest.mark.benchmark(group="ma_single")
    def test_single_ma(self, benchmark, data_size, ma_type):
        data = get_test_data(data_size)
        result = benchmark(
            moving_average.single.moving_average,
            data['close'], ma_type
        )
        assert isinstance(result, float)

    @pytest.mark.benchmark(group="ma_bulk")
    def test_bulk_ma(self, benchmark, data_size, ma_type):
        data = get_test_data(data_size)
        period = min(20, len(data['close']))
        result = benchmark(
            moving_average.bulk.moving_average,
            data['close'], ma_type, period
        )
        assert isinstance(result, list)

@pytest.mark.parametrize("data_size", data_sizes)
class TestMcGinleyDynamic:
    @pytest.mark.benchmark(group="mcginley_single")
    def test_single_mcginley_dynamic(self, benchmark, data_size):
        data = get_test_data(data_size)
        latest_price = data['close'][-1]
        previous_mcginley = data['close'][-2] if len(data['close']) > 1 else 0.0
        period = min(20, len(data['close']))
        result = benchmark(
            moving_average.single.mcginley_dynamic,
            latest_price, previous_mcginley, period
        )
        assert isinstance(result, float)

    @pytest.mark.benchmark(group="mcginley_bulk")
    def test_bulk_mcginley_dynamic(self, benchmark, data_size):
        data = get_test_data(data_size)
        previous_mcginley = data['close'][0] if data['close'] else 0.0
        period = min(20, len(data['close']))
        result = benchmark(
            moving_average.bulk.mcginley_dynamic,
            data['close'], previous_mcginley, period
        )
        assert isinstance(result, list)

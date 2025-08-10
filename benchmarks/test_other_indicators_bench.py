"""Benchmark tests for other_indicators (single and bulk, all dataset sizes and variations)"""
import pytest
from pytechnicalindicators import other_indicators
from data_constants import get_test_data

ma_types = ["simple", "smoothed", "exponential", "median", "mode"]
data_sizes = ["small", "medium", "large"]

class TestReturnOnInvestment:
    @pytest.mark.benchmark(group="roi_single")
    @pytest.mark.parametrize("data_size", data_sizes)
    def test_single_roi(self, benchmark, data_size):
        data = get_test_data(data_size)
        start_price = data['close'][0] 
        end_price = data['close'][-1] 
        investment = 1000.0
        result = benchmark(
            other_indicators.single.return_on_investment,
            start_price, end_price, investment
        )
        assert isinstance(result, tuple) and len(result) == 2

    @pytest.mark.benchmark(group="roi_bulk")
    @pytest.mark.parametrize("data_size", data_sizes)
    def test_bulk_roi(self, benchmark, data_size):
        data = get_test_data(data_size)
        investment = 1000.0
        result = benchmark(
            other_indicators.bulk.return_on_investment,
            data['close'], investment
        )
        assert isinstance(result, list)

class TestTrueRange:
    @pytest.mark.benchmark(group="tr_single")
    @pytest.mark.parametrize("data_size", data_sizes)
    def test_single_true_range(self, benchmark, data_size):
        data = get_test_data(data_size)
        close = data['close'][-2] 
        high = data['high'][-1] 
        low = data['low'][-1] 
        result = benchmark(
            other_indicators.single.true_range,
            close, high, low
        )
        assert isinstance(result, float)

    @pytest.mark.benchmark(group="tr_bulk")
    @pytest.mark.parametrize("data_size", data_sizes)
    def test_bulk_true_range(self, benchmark, data_size):
        data = get_test_data(data_size)
        result = benchmark(
            other_indicators.bulk.true_range,
            data['close'], data['high'], data['low']
        )
        assert isinstance(result, list)

@pytest.mark.parametrize("ma_type", ma_types)
@pytest.mark.parametrize("data_size", data_sizes)
class TestAverageTrueRange:
    @pytest.mark.benchmark(group="atr_single")
    def test_single_atr(self, benchmark, data_size, ma_type):
        data = get_test_data(data_size)
        result = benchmark(
            other_indicators.single.average_true_range,
            data['close'], data['high'], data['low'], ma_type
        )
        assert isinstance(result, float)

    @pytest.mark.benchmark(group="atr_bulk")
    def test_bulk_atr(self, benchmark, data_size, ma_type):
        data = get_test_data(data_size)
        period = min(20, len(data['close']))
        result = benchmark(
            other_indicators.bulk.average_true_range,
            data['close'], data['high'], data['low'], ma_type, period
        )
        assert isinstance(result, list)

class TestInternalBarStrength:
    @pytest.mark.benchmark(group="ibs_single")
    @pytest.mark.parametrize("data_size", data_sizes)
    def test_single_ibs(self, benchmark, data_size):
        data = get_test_data(data_size)
        high = data['high'][-1] 
        low = data['low'][-1] 
        close = data['close'][-1] 
        result = benchmark(
            other_indicators.single.internal_bar_strength,
            high, low, close
        )
        assert isinstance(result, float)

    @pytest.mark.benchmark(group="ibs_bulk")
    @pytest.mark.parametrize("data_size", data_sizes)
    def test_bulk_ibs(self, benchmark, data_size):
        data = get_test_data(data_size)
        result = benchmark(
            other_indicators.bulk.internal_bar_strength,
            data['high'], data['low'], data['close']
        )
        assert isinstance(result, list)

@pytest.mark.parametrize("ma_type", ma_types)
@pytest.mark.parametrize("data_size", data_sizes)
class TestPositivityIndicator:
    @pytest.mark.benchmark(group="positivity_bulk")
    def test_bulk_positivity(self, benchmark, data_size, ma_type):
        data = get_test_data(data_size)
        open_ = data['open'] 
        prev_close = data['close']
        period = min(10, len(prev_close))
        result = benchmark(
            other_indicators.bulk.positivity_indicator,
            open_, prev_close, period, ma_type
        )
        assert isinstance(result, list)

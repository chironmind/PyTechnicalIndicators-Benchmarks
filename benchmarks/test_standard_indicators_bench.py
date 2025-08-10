"""Benchmark tests for standard_indicators (single and bulk, all dataset sizes)"""
import pytest
from pytechnicalindicators import standard_indicators
from data_constants import get_test_data

data_sizes = ["small", "medium", "large"]

@pytest.mark.parametrize("data_size", data_sizes)
class TestSimpleMovingAverage:
    @pytest.mark.benchmark(group="sma_single")
    def test_single_sma(self, benchmark, data_size):
        data = get_test_data(data_size)
        result = benchmark(
            standard_indicators.single.simple_moving_average,
            data['close']
        )
        assert isinstance(result, float)

    @pytest.mark.benchmark(group="sma_bulk")
    def test_bulk_sma(self, benchmark, data_size):
        data = get_test_data(data_size)
        period = min(20, len(data['close']))
        result = benchmark(
            standard_indicators.bulk.simple_moving_average,
            data['close'], period
        )
        assert isinstance(result, list)

@pytest.mark.parametrize("data_size", data_sizes)
class TestSmoothedMovingAverage:
    @pytest.mark.benchmark(group="smma_single")
    def test_single_smma(self, benchmark, data_size):
        data = get_test_data(data_size)
        result = benchmark(
            standard_indicators.single.smoothed_moving_average,
            data['close']
        )
        assert isinstance(result, float)

    @pytest.mark.benchmark(group="smma_bulk")
    def test_bulk_smma(self, benchmark, data_size):
        data = get_test_data(data_size)
        period = min(20, len(data['close']))
        result = benchmark(
            standard_indicators.bulk.smoothed_moving_average,
            data['close'], period
        )
        assert isinstance(result, list)

@pytest.mark.parametrize("data_size", data_sizes)
class TestExponentialMovingAverage:
    @pytest.mark.benchmark(group="ema_single")
    def test_single_ema(self, benchmark, data_size):
        data = get_test_data(data_size)
        result = benchmark(
            standard_indicators.single.exponential_moving_average,
            data['close']
        )
        assert isinstance(result, float)

    @pytest.mark.benchmark(group="ema_bulk")
    def test_bulk_ema(self, benchmark, data_size):
        data = get_test_data(data_size)
        period = min(20, len(data['close']))
        result = benchmark(
            standard_indicators.bulk.exponential_moving_average,
            data['close'], period
        )
        assert isinstance(result, list)

@pytest.mark.parametrize("data_size", data_sizes)
class TestBollingerBands:
    @pytest.mark.benchmark(group="bb_single")
    def test_single_bollinger(self, benchmark, data_size):
        data = get_test_data(data_size)
        result = benchmark(
            standard_indicators.single.bollinger_bands,
            data['close'][:20]
        )
        assert isinstance(result, tuple) and len(result) == 3

    @pytest.mark.benchmark(group="bb_bulk")
    def test_bulk_bollinger(self, benchmark, data_size):
        data = get_test_data(data_size)
        result = benchmark(
            standard_indicators.bulk.bollinger_bands,
            data['close']
        )
        assert isinstance(result, list)

@pytest.mark.parametrize("data_size", data_sizes)
class TestMACD:
    @pytest.mark.benchmark(group="macd_single")
    def test_single_macd(self, benchmark, data_size):
        data = get_test_data(data_size)
        result = benchmark(
            standard_indicators.single.macd,
            data['close'][:34]
        )
        assert isinstance(result, tuple) and len(result) == 3

    @pytest.mark.benchmark(group="macd_bulk")
    def test_bulk_macd(self, benchmark, data_size):
        data = get_test_data(data_size)
        result = benchmark(
            standard_indicators.bulk.macd,
            data['close']
        )
        assert isinstance(result, list)

@pytest.mark.parametrize("data_size", data_sizes)
class TestRSI:
    @pytest.mark.benchmark(group="rsi_single")
    def test_single_rsi(self, benchmark, data_size):
        data = get_test_data(data_size)
        result = benchmark(
            standard_indicators.single.rsi,
            data['close'][:14]
        )
        assert isinstance(result, float)

    @pytest.mark.benchmark(group="rsi_bulk")
    def test_bulk_rsi(self, benchmark, data_size):
        data = get_test_data(data_size)
        result = benchmark(
            standard_indicators.bulk.rsi,
            data['close']
        )
        assert isinstance(result, list)

"""Benchmark tests for strength_indicators (single and bulk, all dataset sizes and variations)"""
import pytest
from pytechnicalindicators import strength_indicators
from data_constants import get_test_data

ma_types = ["simple", "smoothed", "exponential", "median", "mode"]
data_sizes = ["small", "medium", "large"]

class TestAccumulationDistribution:
    @pytest.mark.benchmark(group="ad_single")
    @pytest.mark.parametrize("data_size", data_sizes)
    def test_single_accumulation_distribution(self, benchmark, data_size):
        data = get_test_data(data_size)
        high = data['high'][-1] if data['high'] else 2.0
        low = data['low'][-1] if data['low'] else 1.0
        close = data['close'][-1] if data['close'] else 1.5
        volume = data['volume'][-1] if 'volume' in data and data['volume'] else 1000.0
        prev_ad = data['close'][-2] if len(data['close']) > 1 else 0.0
        result = benchmark(
            strength_indicators.single.accumulation_distribution,
            high, low, close, volume, prev_ad
        )
        assert isinstance(result, float)

    @pytest.mark.benchmark(group="ad_bulk")
    @pytest.mark.parametrize("data_size", data_sizes)
    def test_bulk_accumulation_distribution(self, benchmark, data_size):
        data = get_test_data(data_size)
        prev_ad = data['close'][0] if data['close'] else 0.0
        result = benchmark(
            strength_indicators.bulk.accumulation_distribution,
            data['high'], data['low'], data['close'], data['volume'], prev_ad
        )
        assert isinstance(result, list)

class TestVolumeIndex:
    @pytest.mark.benchmark(group="vi_single")
    @pytest.mark.parametrize("data_size", data_sizes)
    def test_single_volume_index(self, benchmark, data_size):
        data = get_test_data(data_size)
        curr_close = data['close'][-1] if data['close'] else 2.0
        prev_close = data['close'][-2] if len(data['close']) > 1 else 1.5
        prev_vi = 0.0
        result = benchmark(
            strength_indicators.single.volume_index,
            curr_close, prev_close, prev_vi
        )
        assert isinstance(result, float)

    @pytest.mark.benchmark(group="pvi_bulk")
    @pytest.mark.parametrize("data_size", data_sizes)
    def test_bulk_positive_volume_index(self, benchmark, data_size):
        data = get_test_data(data_size)
        prev_vi = 0.0
        result = benchmark(
            strength_indicators.bulk.positive_volume_index,
            data['close'], data['volume'], prev_vi
        )
        assert isinstance(result, list)

    @pytest.mark.benchmark(group="nvi_bulk")
    @pytest.mark.parametrize("data_size", data_sizes)
    def test_bulk_negative_volume_index(self, benchmark, data_size):
        data = get_test_data(data_size)
        prev_vi = 0.0
        result = benchmark(
            strength_indicators.bulk.negative_volume_index,
            data['close'], data['volume'], prev_vi
        )
        assert isinstance(result, list)

@pytest.mark.parametrize("ma_type", ma_types)
@pytest.mark.parametrize("data_size", data_sizes)
class TestRelativeVigorIndex:
    @pytest.mark.benchmark(group="rvi_single")
    def test_single_rvi(self, benchmark, data_size, ma_type):
        data = get_test_data(data_size)
        result = benchmark(
            strength_indicators.single.relative_vigor_index,
            data['open'], data['high'], data['low'], data['close'], ma_type
        )
        assert isinstance(result, float)

    @pytest.mark.benchmark(group="rvi_bulk")
    def test_bulk_rvi(self, benchmark, data_size, ma_type):
        data = get_test_data(data_size)
        period = min(20, len(data['close']))
        result = benchmark(
            strength_indicators.bulk.relative_vigor_index,
            data['open'], data['high'], data['low'], data['close'], ma_type, period
        )
        assert isinstance(result, list)

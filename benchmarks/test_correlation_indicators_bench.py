"""Benchmark tests for correlation indicators (single and bulk, all full cross-product variations)"""
import pytest
from pytechnicalindicators import correlation_indicators
from data_constants import get_test_data

ma_types = ["simple", "smoothed", "exponential", "median", "mode"]
dev_types = ["standard", "mean", "median", "ulcer", "mode"]

@pytest.mark.parametrize("ma_type", ma_types)
@pytest.mark.parametrize("dev_type", dev_types)
class TestSingleCorrelateAssetPrices:
    """Single correlation calculation benchmarks (full cross-product)"""

    @pytest.mark.benchmark(group="single_correlation")
    def test_single_correlation_small(self, benchmark, ma_type, dev_type):
        data = get_test_data("small")
        result = benchmark(
            correlation_indicators.single.correlate_asset_prices,
            data['close'], data['high'], ma_type, dev_type
        )
        assert isinstance(result, float)

    @pytest.mark.benchmark(group="single_correlation")
    def test_single_correlation_medium(self, benchmark, ma_type, dev_type):
        data = get_test_data("medium")
        result = benchmark(
            correlation_indicators.single.correlate_asset_prices,
            data['close'], data['high'], ma_type, dev_type
        )
        assert isinstance(result, float)

    @pytest.mark.benchmark(group="single_correlation")
    def test_single_correlation_large(self, benchmark, ma_type, dev_type):
        data = get_test_data("large")
        result = benchmark(
            correlation_indicators.single.correlate_asset_prices,
            data['close'], data['high'], ma_type, dev_type
        )
        assert isinstance(result, float)

@pytest.mark.parametrize("ma_type", ma_types)
@pytest.mark.parametrize("dev_type", dev_types)
class TestBulkCorrelateAssetPrices:
    """Bulk correlation calculation benchmarks (full cross-product)"""

    @pytest.mark.benchmark(group="bulk_correlation")
    def test_bulk_correlation_small(self, benchmark, ma_type, dev_type):
        data = get_test_data("small")
        period = min(20, len(data['close']) - 1)
        result = benchmark(
            correlation_indicators.bulk.correlate_asset_prices,
            data['close'], data['high'], ma_type, dev_type, period
        )
        assert isinstance(result, list)
        assert len(result) > 0

    @pytest.mark.benchmark(group="bulk_correlation")
    def test_bulk_correlation_medium(self, benchmark, ma_type, dev_type):
        data = get_test_data("medium")
        result = benchmark(
            correlation_indicators.bulk.correlate_asset_prices,
            data['close'], data['high'], ma_type, dev_type, 20
        )
        assert isinstance(result, list)
        assert len(result) > 0

    @pytest.mark.benchmark(group="bulk_correlation")
    def test_bulk_correlation_large(self, benchmark, ma_type, dev_type):
        data = get_test_data("large")
        result = benchmark(
            correlation_indicators.bulk.correlate_asset_prices,
            data['close'], data['high'], ma_type, dev_type, 20
        )
        assert isinstance(result, list)
        assert len(result) > 0

@pytest.mark.benchmark(group="bulk_correlation")
@pytest.mark.parametrize("period", [5, 10, 20, 50])
def test_bulk_correlation_different_periods_large(benchmark, period):
    data = get_test_data("large")
    result = benchmark(
        correlation_indicators.bulk.correlate_asset_prices,
        data['close'], data['high'], "simple", "standard", period
    )
    assert isinstance(result, list)
    assert len(result) > 0


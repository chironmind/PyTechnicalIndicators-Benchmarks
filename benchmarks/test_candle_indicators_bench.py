"""Benchmark tests for candle indicators (single and bulk, all variations, all dataset sizes)"""
import pytest
from pytechnicalindicators import candle_indicators
from data_constants import get_test_data

ma_types = ["simple", "smoothed", "exponential", "median", "mode"]
dev_types = ["standard", "mean", "median", "mode", "ulcer"]
data_sizes = ["small", "medium", "large"]

# Moving Constant Envelopes (single & bulk)
@pytest.mark.parametrize("ma_type", ma_types)
@pytest.mark.parametrize("data_size", data_sizes)
class TestMovingConstantEnvelopes:
    @pytest.mark.benchmark(group="mce_single")
    def test_single_mce(self, benchmark, data_size, ma_type):
        data = get_test_data(data_size)
        result = benchmark(
            candle_indicators.single.moving_constant_envelopes,
            data['close'], ma_type, 3.0
        )
        assert isinstance(result, tuple) and len(result) == 3

    @pytest.mark.benchmark(group="mce_bulk")
    def test_bulk_mce(self, benchmark, data_size, ma_type):
        data = get_test_data(data_size)
        period = min(20, len(data['close']))
        result = benchmark(
            candle_indicators.bulk.moving_constant_envelopes,
            data['close'], ma_type, 3.0, period
        )
        assert isinstance(result, list)

# McGinley Dynamic Envelopes (single & bulk)
@pytest.mark.parametrize("data_size", data_sizes)
class TestMcGinleyDynamicEnvelopes:
    @pytest.mark.benchmark(group="mcginley_env_single")
    def test_single_mcginley_env(self, benchmark, data_size):
        data = get_test_data(data_size)
        result = benchmark(
            candle_indicators.single.mcginley_dynamic_envelopes,
            data['close'], 3.0, 0.0
        )
        assert isinstance(result, tuple) and len(result) == 3

    @pytest.mark.benchmark(group="mcginley_env_bulk")
    def test_bulk_mcginley_env(self, benchmark, data_size):
        data = get_test_data(data_size)
        period = min(20, len(data['close']))
        result = benchmark(
            candle_indicators.bulk.mcginley_dynamic_envelopes,
            data['close'], 3.0, 0.0, period
        )
        assert isinstance(result, list)

# Moving Constant Bands (single & bulk, full cross-product)
@pytest.mark.parametrize("ma_type", ma_types)
@pytest.mark.parametrize("dev_type", dev_types)
@pytest.mark.parametrize("data_size", data_sizes)
class TestMovingConstantBands:
    @pytest.mark.benchmark(group="bands_single")
    def test_single_bands(self, benchmark, data_size, ma_type, dev_type):
        data = get_test_data(data_size)
        result = benchmark(
            candle_indicators.single.moving_constant_bands,
            data['close'], ma_type, dev_type, 3.0
        )
        assert isinstance(result, tuple) and len(result) == 3

    @pytest.mark.benchmark(group="bands_bulk")
    def test_bulk_bands(self, benchmark, data_size, ma_type, dev_type):
        data = get_test_data(data_size)
        period = min(20, len(data['close']))
        result = benchmark(
            candle_indicators.bulk.moving_constant_bands,
            data['close'], ma_type, dev_type, 3.0, period
        )
        assert isinstance(result, list)

# McGinley Dynamic Bands (single & bulk, dev_types)
@pytest.mark.parametrize("dev_type", dev_types)
@pytest.mark.parametrize("data_size", data_sizes)
class TestMcGinleyDynamicBands:
    @pytest.mark.benchmark(group="mcginley_bands_single")
    def test_single_mcginley_bands(self, benchmark, data_size, dev_type):
        data = get_test_data(data_size)
        result = benchmark(
            candle_indicators.single.mcginley_dynamic_bands,
            data['close'], dev_type, 3.0, 0.0
        )
        assert isinstance(result, tuple) and len(result) == 3

    @pytest.mark.benchmark(group="mcginley_bands_bulk")
    def test_bulk_mcginley_bands(self, benchmark, data_size, dev_type):
        data = get_test_data(data_size)
        period = min(20, len(data['close']))
        result = benchmark(
            candle_indicators.bulk.mcginley_dynamic_bands,
            data['close'], dev_type, 3.0, 0.0, period
        )
        assert isinstance(result, list)

# Ichimoku Cloud (single & bulk)
@pytest.mark.parametrize("data_size", data_sizes)
class TestIchimokuCloud:
    @pytest.mark.benchmark(group="ichimoku_single")
    def test_single_ichimoku(self, benchmark, data_size):
        data = get_test_data(data_size)
        result = benchmark(
            candle_indicators.single.ichimoku_cloud,
            data['high'], data['low'], data['close'],
            9, 26, 52
        )
        assert isinstance(result, tuple) and len(result) == 5

    @pytest.mark.benchmark(group="ichimoku_bulk")
    def test_bulk_ichimoku(self, benchmark, data_size):
        data = get_test_data(data_size)
        result = benchmark(
            candle_indicators.bulk.ichimoku_cloud,
            data['high'], data['low'], data['close'],
            9, 26, 52
        )
        assert isinstance(result, list)

# Donchian Channels (single & bulk)
@pytest.mark.parametrize("data_size", data_sizes)
class TestDonchianChannels:
    @pytest.mark.benchmark(group="donchian_single")
    def test_single_donchian(self, benchmark, data_size):
        data = get_test_data(data_size)
        result = benchmark(
            candle_indicators.single.donchian_channels,
            data['high'], data['low']
        )
        assert isinstance(result, tuple) and len(result) == 3

    @pytest.mark.benchmark(group="donchian_bulk")
    def test_bulk_donchian(self, benchmark, data_size):
        data = get_test_data(data_size)
        period = min(20, len(data['high']))
        result = benchmark(
            candle_indicators.bulk.donchian_channels,
            data['high'], data['low'], period
        )
        assert isinstance(result, list)

# Keltner Channel (single & bulk, full cross-product of ma_types)
@pytest.mark.parametrize("ma_type", ma_types)
@pytest.mark.parametrize("atr_type", ma_types)
@pytest.mark.parametrize("data_size", data_sizes)
class TestKeltnerChannel:
    @pytest.mark.benchmark(group="keltner_single")
    def test_single_keltner(self, benchmark, data_size, ma_type, atr_type):
        data = get_test_data(data_size)
        result = benchmark(
            candle_indicators.single.keltner_channel,
            data['high'], data['low'], data['close'], ma_type, atr_type, 2.0
        )
        assert isinstance(result, tuple) and len(result) == 3

    @pytest.mark.benchmark(group="keltner_bulk")
    def test_bulk_keltner(self, benchmark, data_size, ma_type, atr_type):
        data = get_test_data(data_size)
        period = min(20, len(data['high']))
        result = benchmark(
            candle_indicators.bulk.keltner_channel,
            data['high'], data['low'], data['close'], ma_type, atr_type, 2.0, period
        )
        assert isinstance(result, list)

# Supertrend (single & bulk, ma_types)
@pytest.mark.parametrize("ma_type", ma_types)
@pytest.mark.parametrize("data_size", data_sizes)
class TestSupertrend:
    @pytest.mark.benchmark(group="supertrend_single")
    def test_single_supertrend(self, benchmark, data_size, ma_type):
        data = get_test_data(data_size)
        result = benchmark(
            candle_indicators.single.supertrend,
            data['high'], data['low'], data['close'], ma_type, 2.0
        )
        assert isinstance(result, float)

    @pytest.mark.benchmark(group="supertrend_bulk")
    def test_bulk_supertrend(self, benchmark, data_size, ma_type):
        data = get_test_data(data_size)
        period = min(20, len(data['high']))
        result = benchmark(
            candle_indicators.bulk.supertrend,
            data['high'], data['low'], data['close'], ma_type, 2.0, period
        )
        assert isinstance(result, list)


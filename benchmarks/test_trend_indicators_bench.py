"""Benchmark tests for trend_indicators (single and bulk, all dataset sizes and parameter variations)"""
import pytest
from pytechnicalindicators import trend_indicators
from data_constants import get_test_data

ma_types = ["simple", "smoothed", "exponential", "median", "mode"]
positions = ["long", "short"]
data_sizes = ["small", "medium", "large"]

class TestAroon:
    @pytest.mark.benchmark(group="aroon_up_single")
    @pytest.mark.parametrize("data_size", data_sizes)
    def test_single_aroon_up(self, benchmark, data_size):
        data = get_test_data(data_size)
        result = benchmark(trend_indicators.single.aroon_up, data['high'])
        assert isinstance(result, float)

    @pytest.mark.benchmark(group="aroon_up_bulk")
    @pytest.mark.parametrize("data_size", data_sizes)
    def test_bulk_aroon_up(self, benchmark, data_size):
        data = get_test_data(data_size)
        period = min(20, len(data['high']))
        result = benchmark(trend_indicators.bulk.aroon_up, data['high'], period)
        assert isinstance(result, list)

    @pytest.mark.benchmark(group="aroon_down_single")
    @pytest.mark.parametrize("data_size", data_sizes)
    def test_single_aroon_down(self, benchmark, data_size):
        data = get_test_data(data_size)
        result = benchmark(trend_indicators.single.aroon_down, data['low'])
        assert isinstance(result, float)

    @pytest.mark.benchmark(group="aroon_down_bulk")
    @pytest.mark.parametrize("data_size", data_sizes)
    def test_bulk_aroon_down(self, benchmark, data_size):
        data = get_test_data(data_size)
        period = min(20, len(data['low']))
        result = benchmark(trend_indicators.bulk.aroon_down, data['low'], period)
        assert isinstance(result, list)

    @pytest.mark.benchmark(group="aroon_oscillator_single")
    @pytest.mark.parametrize("data_size", data_sizes)
    def test_single_aroon_oscillator(self, benchmark, data_size):
        data = get_test_data(data_size)
        up = trend_indicators.single.aroon_up(data['high'])
        down = trend_indicators.single.aroon_down(data['low'])
        result = benchmark(trend_indicators.single.aroon_oscillator, up, down)
        assert isinstance(result, float)

    @pytest.mark.benchmark(group="aroon_oscillator_bulk")
    @pytest.mark.parametrize("data_size", data_sizes)
    def test_bulk_aroon_oscillator(self, benchmark, data_size):
        data = get_test_data(data_size)
        period = min(20, len(data['high']))
        aroon_up = trend_indicators.bulk.aroon_up(data['high'], period)
        aroon_down = trend_indicators.bulk.aroon_down(data['low'], period)
        result = benchmark(trend_indicators.bulk.aroon_oscillator, aroon_up, aroon_down)
        assert isinstance(result, list)

    @pytest.mark.benchmark(group="aroon_indicator_single")
    @pytest.mark.parametrize("data_size", data_sizes)
    def test_single_aroon_indicator(self, benchmark, data_size):
        data = get_test_data(data_size)
        result = benchmark(trend_indicators.single.aroon_indicator, data['high'], data['low'])
        assert isinstance(result, tuple) and len(result) == 3

    @pytest.mark.benchmark(group="aroon_indicator_bulk")
    @pytest.mark.parametrize("data_size", data_sizes)
    def test_bulk_aroon_indicator(self, benchmark, data_size):
        data = get_test_data(data_size)
        period = min(20, len(data['high']), len(data['low']))
        result = benchmark(trend_indicators.bulk.aroon_indicator, data['high'], data['low'], period)
        assert isinstance(result, list)

class TestParabolicTimePriceSystem:
    @pytest.mark.benchmark(group="parabolic_long_single")
    @pytest.mark.parametrize("data_size", data_sizes)
    def test_single_long_parabolic(self, benchmark, data_size):
        data = get_test_data(data_size)
        prev_sar = data['low'][-2] if len(data['low']) > 1 else 0.0
        extreme = max(data['high']) if data['high'] else 0.0
        af = 0.02
        low = min(data['low']) if data['low'] else 0.0
        result = benchmark(
            trend_indicators.single.long_parabolic_time_price_system,
            prev_sar, extreme, af, low
        )
        assert isinstance(result, float)

    @pytest.mark.benchmark(group="parabolic_short_single")
    @pytest.mark.parametrize("data_size", data_sizes)
    def test_single_short_parabolic(self, benchmark, data_size):
        data = get_test_data(data_size)
        prev_sar = data['high'][-2] if len(data['high']) > 1 else 0.0
        extreme = min(data['low']) if data['low'] else 0.0
        af = 0.02
        high = max(data['high']) if data['high'] else 0.0
        result = benchmark(
            trend_indicators.single.short_parabolic_time_price_system,
            prev_sar, extreme, af, high
        )
        assert isinstance(result, float)

    @pytest.mark.benchmark(group="parabolic_bulk")
    @pytest.mark.parametrize("data_size", data_sizes)
    @pytest.mark.parametrize("position", positions)
    def test_bulk_parabolic(self, benchmark, data_size, position):
        data = get_test_data(data_size)
        af_start, af_step, af_max = 0.02, 0.02, 0.2
        prev_sar = 0.0
        result = benchmark(
            trend_indicators.bulk.parabolic_time_price_system,
            data['high'], data['low'], af_start, af_step, af_max, position, prev_sar
        )
        assert isinstance(result, list)

class TestDirectionalMovementSystem:
    @pytest.mark.benchmark(group="dms_bulk")
    @pytest.mark.parametrize("data_size", data_sizes)
    @pytest.mark.parametrize("ma_type", ma_types)
    def test_bulk_dms(self, benchmark, data_size, ma_type):
        data = get_test_data(data_size)
        period = min(14, len(data['high']), len(data['low']), len(data['close']))
        result = benchmark(
            trend_indicators.bulk.directional_movement_system,
            data['high'], data['low'], data['close'], period, ma_type
        )
        assert isinstance(result, list)

class TestVolumePriceTrend:
    @pytest.mark.benchmark(group="vpt_single")
    @pytest.mark.parametrize("data_size", data_sizes)
    def test_single_vpt(self, benchmark, data_size):
        data = get_test_data(data_size)
        current_price = data['close'][-1] if data['close'] else 2.0
        previous_price = data['close'][-2] if len(data['close']) > 1 else 1.0
        current_volume = data['volume'][-1] if 'volume' in data and data['volume'] else 1000.0
        previous_vpt = 0.0
        result = benchmark(
            trend_indicators.single.volume_price_trend,
            current_price, previous_price, current_volume, previous_vpt
        )
        assert isinstance(result, float)

    @pytest.mark.benchmark(group="vpt_bulk")
    @pytest.mark.parametrize("data_size", data_sizes)
    def test_bulk_vpt(self, benchmark, data_size):
        data = get_test_data(data_size)
        previous_vpt = 0.0
        result = benchmark(
            trend_indicators.bulk.volume_price_trend,
            data['close'], data['volume'], previous_vpt
        )
        assert isinstance(result, list)

@pytest.mark.parametrize("ma1", ma_types)
@pytest.mark.parametrize("ma2", ma_types)
@pytest.mark.parametrize("data_size", data_sizes)
class TestTrueStrengthIndex:
    @pytest.mark.benchmark(group="tsi_single")
    def test_single_tsi(self, benchmark, data_size, ma1, ma2):
        data = get_test_data(data_size)
        first_period = min(25, len(data['close']))
        result = benchmark(
            trend_indicators.single.true_strength_index,
            data['close'], first_period, ma1, ma2
        )
        assert isinstance(result, float)

    @pytest.mark.benchmark(group="tsi_bulk")
    def test_bulk_tsi(self, benchmark, data_size, ma1, ma2):
        data = get_test_data(data_size)
        first_period = min(13, len(data['close']))
        second_period = min(25, len(data['close']))
        result = benchmark(
            trend_indicators.bulk.true_strength_index,
            data['close'], ma1, first_period, ma2, second_period
        )
        assert isinstance(result, list)

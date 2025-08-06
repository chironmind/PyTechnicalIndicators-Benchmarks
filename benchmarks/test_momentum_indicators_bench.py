"""Benchmark tests for momentum indicators (single and bulk, all variations)"""
import pytest
from pytechnicalindicators import momentum_indicators
from data_constants import get_test_data

ma_types = ["simple", "smoothed", "exponential", "median", "mode"]
dev_types = ["standard", "mean", "median", "ulcer", "mode"]

@pytest.mark.parametrize("ma_type", ma_types)
class TestRelativeStrengthIndex:
    """RSI single and bulk benchmarks (all ma_types)"""

    @pytest.mark.benchmark(group="rsi_single")
    def test_single_rsi_small(self, benchmark, ma_type):
        data = get_test_data("small")
        result = benchmark(momentum_indicators.single.relative_strength_index, data['close'], ma_type)
        assert isinstance(result, float)

    @pytest.mark.benchmark(group="rsi_single")
    def test_single_rsi_medium(self, benchmark, ma_type):
        data = get_test_data("medium")
        result = benchmark(momentum_indicators.single.relative_strength_index, data['close'], ma_type)
        assert isinstance(result, float)

    @pytest.mark.benchmark(group="rsi_single")
    def test_single_rsi_large(self, benchmark, ma_type):
        data = get_test_data("large")
        result = benchmark(momentum_indicators.single.relative_strength_index, data['close'], ma_type)
        assert isinstance(result, float)

    @pytest.mark.benchmark(group="rsi_bulk")
    def test_bulk_rsi_small(self, benchmark, ma_type):
        data = get_test_data("small")
        period = min(20, len(data['close']) - 1)
        result = benchmark(momentum_indicators.bulk.relative_strength_index, data['close'], ma_type, period)
        assert isinstance(result, list)

    @pytest.mark.benchmark(group="rsi_bulk")
    def test_bulk_rsi_medium(self, benchmark, ma_type):
        data = get_test_data("medium")
        result = benchmark(momentum_indicators.bulk.relative_strength_index, data['close'], ma_type, 20)
        assert isinstance(result, list)

    @pytest.mark.benchmark(group="rsi_bulk")
    def test_bulk_rsi_large(self, benchmark, ma_type):
        data = get_test_data("large")
        result = benchmark(momentum_indicators.bulk.relative_strength_index, data['close'], ma_type, 20)
        assert isinstance(result, list)

class TestStochasticOscillator:
    """Stochastic Oscillator single and bulk benchmarks"""

    @pytest.mark.benchmark(group="stoch_single")
    def test_single_stoch_small(self, benchmark):
        data = get_test_data("small")
        result = benchmark(momentum_indicators.single.stochastic_oscillator, data['close'])
        assert isinstance(result, float)

    @pytest.mark.benchmark(group="stoch_single")
    def test_single_stoch_medium(self, benchmark):
        data = get_test_data("medium")
        result = benchmark(momentum_indicators.single.stochastic_oscillator, data['close'])
        assert isinstance(result, float)

    @pytest.mark.benchmark(group="stoch_single")
    def test_single_stoch_large(self, benchmark):
        data = get_test_data("large")
        result = benchmark(momentum_indicators.single.stochastic_oscillator, data['close'])
        assert isinstance(result, float)

    @pytest.mark.benchmark(group="stoch_bulk")
    def test_bulk_stoch_small(self, benchmark):
        data = get_test_data("small")
        period = min(20, len(data['close']) - 1)
        result = benchmark(momentum_indicators.bulk.stochastic_oscillator, data['close'], period)
        assert isinstance(result, list)

    @pytest.mark.benchmark(group="stoch_bulk")
    def test_bulk_stoch_medium(self, benchmark):
        data = get_test_data("medium")
        result = benchmark(momentum_indicators.bulk.stochastic_oscillator, data['close'], 20)
        assert isinstance(result, list)

    @pytest.mark.benchmark(group="stoch_bulk")
    def test_bulk_stoch_large(self, benchmark):
        data = get_test_data("large")
        result = benchmark(momentum_indicators.bulk.stochastic_oscillator, data['close'], 20)
        assert isinstance(result, list)

@pytest.mark.parametrize("ma_type", ma_types)
class TestSlowStochastic:
    """Slow Stochastic single and bulk benchmarks"""

    @pytest.mark.benchmark(group="slow_stoch_single")
    def test_single_slow_stoch_large(self, benchmark, ma_type):
        # Use a rolling window to simulate the oscillator input
        data = get_test_data("large")
        stoch_values = [momentum_indicators.single.stochastic_oscillator(data['close'][i:i+10])
                        for i in range(len(data['close'])-10)]
        result = benchmark(momentum_indicators.single.slow_stochastic, stoch_values, ma_type)
        assert isinstance(result, float)

    @pytest.mark.benchmark(group="slow_stoch_bulk")
    def test_bulk_slow_stoch_large(self, benchmark, ma_type):
        data = get_test_data("large")
        stoch_values = [momentum_indicators.single.stochastic_oscillator(data['close'][i:i+10])
                        for i in range(len(data['close'])-10)]
        result = benchmark(momentum_indicators.bulk.slow_stochastic, stoch_values, ma_type, 20)
        assert isinstance(result, list)

@pytest.mark.parametrize("ma_type", ma_types)
class TestSlowestStochastic:
    """Slowest Stochastic single and bulk benchmarks"""

    @pytest.mark.benchmark(group="slowest_stoch_single")
    def test_single_slowest_stoch_large(self, benchmark, ma_type):
        # Simulate slow stochastic values as input
        data = get_test_data("large")
        stoch_values = [momentum_indicators.single.stochastic_oscillator(data['close'][i:i+10])
                        for i in range(len(data['close'])-10)]
        slow_stoch_values = [momentum_indicators.single.slow_stochastic(stoch_values[i:i+20], "simple")
                             for i in range(len(stoch_values)-20)]
        result = benchmark(momentum_indicators.single.slowest_stochastic, slow_stoch_values, ma_type)
        assert isinstance(result, float)

    @pytest.mark.benchmark(group="slowest_stoch_bulk")
    def test_bulk_slowest_stoch_large(self, benchmark, ma_type):
        data = get_test_data("large")
        stoch_values = [momentum_indicators.single.stochastic_oscillator(data['close'][i:i+10])
                        for i in range(len(data['close'])-10)]
        slow_stoch_values = [momentum_indicators.single.slow_stochastic(stoch_values[i:i+20], "simple")
                             for i in range(len(stoch_values)-20)]
        result = benchmark(momentum_indicators.bulk.slowest_stochastic, slow_stoch_values, ma_type, 10)
        assert isinstance(result, list)

class TestWilliamsPercentR:
    """Williams %R single and bulk benchmarks"""

    @pytest.mark.benchmark(group="williams_single")
    def test_single_williams_r_large(self, benchmark):
        data = get_test_data("large")
        result = benchmark(momentum_indicators.single.williams_percent_r, data['high'], data['low'], data['close'][-1])
        assert isinstance(result, float)

    @pytest.mark.benchmark(group="williams_bulk")
    def test_bulk_williams_r_large(self, benchmark):
        data = get_test_data("large")
        result = benchmark(momentum_indicators.bulk.williams_percent_r, data['high'], data['low'], data['close'], 20)
        assert isinstance(result, list)

class TestMoneyFlowIndex:
    """Money Flow Index single and bulk benchmarks"""

    @pytest.mark.benchmark(group="mfi_single")
    def test_single_mfi_large(self, benchmark):
        data = get_test_data("large")
        result = benchmark(momentum_indicators.single.money_flow_index, data['close'], data['volume'])
        assert isinstance(result, float)

    @pytest.mark.benchmark(group="mfi_bulk")
    def test_bulk_mfi_large(self, benchmark):
        data = get_test_data("large")
        result = benchmark(momentum_indicators.bulk.money_flow_index, data['close'], data['volume'], 20)
        assert isinstance(result, list)

class TestRateOfChange:
    """Rate of Change single and bulk benchmarks"""

    @pytest.mark.benchmark(group="roc_single")
    def test_single_roc_large(self, benchmark):
        data = get_test_data("large")
        result = benchmark(momentum_indicators.single.rate_of_change, data['close'][-1], data['close'][-2])
        assert isinstance(result, float)

    @pytest.mark.benchmark(group="roc_bulk")
    def test_bulk_roc_large(self, benchmark):
        data = get_test_data("large")
        result = benchmark(momentum_indicators.bulk.rate_of_change, data['close'])
        assert isinstance(result, list)

class TestOnBalanceVolume:
    """On Balance Volume single and bulk benchmarks"""

    @pytest.mark.benchmark(group="obv_single")
    def test_single_obv_large(self, benchmark):
        data = get_test_data("large")
        result = benchmark(momentum_indicators.single.on_balance_volume, data['close'][-1], data['close'][-2], data['volume'][-1], 0.0)
        assert isinstance(result, float)

    @pytest.mark.benchmark(group="obv_bulk")
    def test_bulk_obv_large(self, benchmark):
        data = get_test_data("large")
        result = benchmark(momentum_indicators.bulk.on_balance_volume, data['close'], data['volume'], 0.0)
        assert isinstance(result, list)

@pytest.mark.parametrize("ma_type", ma_types)
@pytest.mark.parametrize("dev_type", dev_types)
class TestCommodityChannelIndex:
    """CCI single and bulk benchmarks (full cross-product)"""

    @pytest.mark.benchmark(group="cci_single")
    def test_single_cci_large(self, benchmark, ma_type, dev_type):
        data = get_test_data("large")
        result = benchmark(momentum_indicators.single.commodity_channel_index, data['close'], ma_type, dev_type, 0.015)
        assert isinstance(result, float)

    @pytest.mark.benchmark(group="cci_bulk")
    def test_bulk_cci_large(self, benchmark, ma_type, dev_type):
        data = get_test_data("large")
        result = benchmark(momentum_indicators.bulk.commodity_channel_index, data['close'], ma_type, dev_type, 0.015, 20)
        assert isinstance(result, list)

@pytest.mark.parametrize("dev_type", dev_types)
class TestMcGinleyDynamicCCI:
    """McGinley Dynamic CCI single and bulk benchmarks (dev_types only)"""

    @pytest.mark.benchmark(group="mcginley_cci_single")
    def test_single_mcginley_cci_large(self, benchmark, dev_type):
        data = get_test_data("large")
        result = benchmark(momentum_indicators.single.mcginley_dynamic_commodity_channel_index, data['close'], 0.0, dev_type, 0.015)
        assert isinstance(result, tuple)
        assert len(result) == 2

    @pytest.mark.benchmark(group="mcginley_cci_bulk")
    def test_bulk_mcginley_cci_large(self, benchmark, dev_type):
        data = get_test_data("large")
        result = benchmark(momentum_indicators.bulk.mcginley_dynamic_commodity_channel_index, data['close'], 0.0, dev_type, 0.015, 20)
        assert isinstance(result, list)

@pytest.mark.parametrize("fast_type", ma_types)
@pytest.mark.parametrize("slow_type", ma_types)
class TestMACDLine:
    """MACD Line single and bulk benchmarks (full cross-product)"""

    @pytest.mark.benchmark(group="macd_line_single")
    def test_single_macd_line_large(self, benchmark, fast_type, slow_type):
        data = get_test_data("large")
        result = benchmark(momentum_indicators.single.macd_line, data['close'], 12, fast_type, slow_type)
        assert isinstance(result, float)

    @pytest.mark.benchmark(group="macd_line_bulk")
    def test_bulk_macd_line_large(self, benchmark, fast_type, slow_type):
        data = get_test_data("large")
        result = benchmark(momentum_indicators.bulk.macd_line, data['close'], 12, fast_type, 26, slow_type)
        assert isinstance(result, list)

@pytest.mark.parametrize("ma_type", ma_types)
class TestSignalLine:
    """Signal Line single and bulk benchmarks"""

    @pytest.mark.benchmark(group="signal_line_single")
    def test_single_signal_line_large(self, benchmark, ma_type):
        data = get_test_data("large")
        # Generate MACD values as input
        macd_values = [momentum_indicators.single.macd_line(data['close'][i:i+50], 12, "simple", "simple")
                       for i in range(len(data['close'])-50)]
        result = benchmark(momentum_indicators.single.signal_line, macd_values, ma_type)
        assert isinstance(result, float)

    @pytest.mark.benchmark(group="signal_line_bulk")
    def test_bulk_signal_line_large(self, benchmark, ma_type):
        data = get_test_data("large")
        macd_values = [momentum_indicators.single.macd_line(data['close'][i:i+50], 12, "simple", "simple")
                       for i in range(len(data['close'])-50)]
        result = benchmark(momentum_indicators.bulk.signal_line, macd_values, ma_type, 20)
        assert isinstance(result, list)

class TestMcGinleyDynamicMACDLine:
    """McGinley Dynamic MACD Line single and bulk benchmarks"""

    @pytest.mark.benchmark(group="mcginley_macd_line_single")
    def test_single_mcginley_macd_line_large(self, benchmark):
        data = get_test_data("large")
        result = benchmark(momentum_indicators.single.mcginley_dynamic_macd_line, data['close'], 12, 0.0, 0.0)
        assert isinstance(result, tuple)
        assert len(result) == 3

    @pytest.mark.benchmark(group="mcginley_macd_line_bulk")
    def test_bulk_mcginley_macd_line_large(self, benchmark):
        data = get_test_data("large")
        result = benchmark(momentum_indicators.bulk.mcginley_dynamic_macd_line, data['close'], 12, 0.0, 26, 0.0)
        assert isinstance(result, list)

@pytest.mark.parametrize("fast_type", ma_types)
@pytest.mark.parametrize("slow_type", ma_types)
class TestChaikinOscillator:
    """Chaikin Oscillator single and bulk benchmarks (full cross-product)"""

    @pytest.mark.benchmark(group="chaikin_osc_single")
    def test_single_chaikin_osc_large(self, benchmark, fast_type, slow_type):
        data = get_test_data("large")
        result = benchmark(momentum_indicators.single.chaikin_oscillator, data['high'], data['low'], data['close'], data['volume'], 3, 0.0, fast_type, slow_type)
        assert isinstance(result, tuple)
        assert len(result) == 2

    @pytest.mark.benchmark(group="chaikin_osc_bulk")
    def test_bulk_chaikin_osc_large(self, benchmark, fast_type, slow_type):
        data = get_test_data("large")
        result = benchmark(momentum_indicators.bulk.chaikin_oscillator, data['high'], data['low'], data['close'], data['volume'], 3, 10, 0.0, fast_type, slow_type)
        assert isinstance(result, list)

@pytest.mark.parametrize("ma_type", ma_types)
class TestPercentagePriceOscillator:
    """PPO single and bulk benchmarks"""

    @pytest.mark.benchmark(group="ppo_single")
    def test_single_ppo_large(self, benchmark, ma_type):
        data = get_test_data("large")
        result = benchmark(momentum_indicators.single.percentage_price_oscillator, data['close'], 12, ma_type)
        assert isinstance(result, float)

    @pytest.mark.benchmark(group="ppo_bulk")
    def test_bulk_ppo_large(self, benchmark, ma_type):
        data = get_test_data("large")
        result = benchmark(momentum_indicators.bulk.percentage_price_oscillator, data['close'], 12, 26, ma_type)
        assert isinstance(result, list)

class TestChandeMomentumOscillator:
    """Chande Momentum Oscillator single and bulk benchmarks"""

    @pytest.mark.benchmark(group="cmo_single")
    def test_single_cmo_large(self, benchmark):
        data = get_test_data("large")
        result = benchmark(momentum_indicators.single.chande_momentum_oscillator, data['close'])
        assert isinstance(result, float)

    @pytest.mark.benchmark(group="cmo_bulk")
    def test_bulk_cmo_large(self, benchmark):
        data = get_test_data("large")
        result = benchmark(momentum_indicators.bulk.chande_momentum_oscillator, data['close'], 20)
        assert isinstance(result, list)

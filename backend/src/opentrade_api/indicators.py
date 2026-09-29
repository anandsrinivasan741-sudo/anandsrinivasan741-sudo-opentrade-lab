from collections.abc import Sequence


def _clean(values: Sequence[float]) -> list[float]:
    return [float(value) for value in values]


def sma(values: Sequence[float], period: int) -> list[float | None]:
    data = _clean(values)
    if period < 1:
        raise ValueError("period must be positive")
    return [None if i + 1 < period else sum(data[i + 1 - period : i + 1]) / period for i in range(len(data))]


def ema(values: Sequence[float], period: int) -> list[float | None]:
    data = _clean(values)
    if period < 1:
        raise ValueError("period must be positive")
    result: list[float | None] = [None] * len(data)
    if len(data) < period:
        return result
    previous = sum(data[:period]) / period
    result[period - 1] = previous
    multiplier = 2 / (period + 1)
    for i in range(period, len(data)):
        previous = (data[i] - previous) * multiplier + previous
        result[i] = previous
    return result


def rsi(values: Sequence[float], period: int = 14) -> list[float | None]:
    data = _clean(values)
    if period < 1:
        raise ValueError("period must be positive")
    result: list[float | None] = [None] * len(data)
    if len(data) <= period:
        return result
    gains = [max(data[i] - data[i - 1], 0) for i in range(1, len(data))]
    losses = [max(data[i - 1] - data[i], 0) for i in range(1, len(data))]
    average_gain = sum(gains[:period]) / period
    average_loss = sum(losses[:period]) / period
    result[period] = 100 if average_loss == 0 else 100 - (100 / (1 + average_gain / average_loss))
    for i in range(period + 1, len(data)):
        average_gain = (average_gain * (period - 1) + gains[i - 1]) / period
        average_loss = (average_loss * (period - 1) + losses[i - 1]) / period
        result[i] = 100 if average_loss == 0 else 100 - (100 / (1 + average_gain / average_loss))
    return result

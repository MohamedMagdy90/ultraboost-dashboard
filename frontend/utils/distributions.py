"""
Local implementation of Distributions class to avoid hummingbot dependency.
This replaces: from hummingbot.strategy_v2.utils.distributions import Distributions
"""
from decimal import Decimal
from math import log, exp
from typing import List


class Distributions:
    """Utility class for generating various distribution patterns for trading strategies."""

    @staticmethod
    def linear(n_levels: int, start: float, end: float) -> List[Decimal]:
        """Generate a linear distribution."""
        if n_levels <= 1:
            return [Decimal(str(start))]
        step = (end - start) / (n_levels - 1)
        return [Decimal(str(start + i * step)) for i in range(n_levels)]

    @staticmethod
    def arithmetic(n_levels: int, start: float, step: float) -> List[Decimal]:
        """Generate an arithmetic distribution."""
        return [Decimal(str(start + i * step)) for i in range(n_levels)]

    @staticmethod
    def geometric(n_levels: int, start: float, ratio: float) -> List[Decimal]:
        """Generate a geometric distribution."""
        return [Decimal(str(start * (ratio ** i))) for i in range(n_levels)]

    @staticmethod
    def fibonacci(n_levels: int, start: float) -> List[Decimal]:
        """Generate a Fibonacci-based distribution."""
        fib = [1, 1]
        for i in range(2, n_levels):
            fib.append(fib[-1] + fib[-2])
        return [Decimal(str(start * f)) for f in fib[:n_levels]]

    @staticmethod
    def logarithmic(n_levels: int, base: float, scaling_factor: float, start: float) -> List[Decimal]:
        """Generate a logarithmic distribution."""
        if base <= 0 or base == 1:
            base = exp(1)  # Default to natural log base
        result = []
        for i in range(n_levels):
            value = start + scaling_factor * log(i + 1, base)
            result.append(Decimal(str(value)))
        return result

#!/usr/bin/env python3
"""The minimum_operations module."""

from prime_factorisation import prime_factors


def minOperations(n: int) -> int:
    """The minimum_operations function calculates
    the minimum_operations"""
    if n <= 1:
        return 0

    primes = prime_factors(n)

    min_operations = sum(primes)

    return min_operations

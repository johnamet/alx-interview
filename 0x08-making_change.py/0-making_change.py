#!/usr/bin/python3
"""
The module for change function
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    we determine ht efewest number of coins needed
    to meet a given amount
    :param: coins: A list of int (coins) in our posession
    :param: total: The amount to meet
    :return: int: the number of coins needed
    """

    change = [total + 1] * (total + 1)

    change[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                change[i] = min(change[i], change[i - coin] + 1)
    return change[total] if change[total] != total + 1 else -1

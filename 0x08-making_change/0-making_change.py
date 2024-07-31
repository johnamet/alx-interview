#!/usr/bin/python3
"""
The module for change function
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    we determine the fewest number of coins needed
    to meet a given amount
    :param coins: A list of int (coins) in our possession
    :param total: The amount to meet
    :return: int: the number of coins needed
    """

    if total <= 0:
        return 0

    # Initialize a DP array with total + 1, which is an impossible number of coins to use
    change = [total + 1] * (total + 1)

    # Base case: To make 0, we need 0 coins
    change[0] = 0

    # Iterate through each amount from 1 to total
    for i in range(1, total + 1):
        # Try every coin that is smaller than or equal to the current amount
        for coin in coins:
            if coin <= i:
                # Update the DP array with the minimum coins needed
                change[i] = min(change[i], change[i - coin] + 1)

    # If change[total] is still total + 1, it means it's impossible to make the amount
    return change[total] if change[total] != total + 1 else -1

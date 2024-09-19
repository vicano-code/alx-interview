#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest
number of coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """return minimum number of coins that sum to give total"""
    if total <= 0:
        return 0
    # Sort the coins
    sorted_coins = sorted(coins)

    ans = []
    i = len(coins) - 1
    while i > 0:
        while (total >= sorted_coins[i]):
            total -= sorted_coins[i]
            ans.append(sorted_coins[i])

        i -= 1
    if total > 0:
        return -1

    return len(ans)

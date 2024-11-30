#!/usr/bin/python3
""" change coins """


def makeChange(coins, total):
    """ how many coins to reach total

    Args:
        coins([List]): [List of Coins]
        total([int]): [total amount needed]
    """
    if (total <= 0):
        return 0

    num_of_coins = 0
    biggest = 0

    sorted_coins = sorted(coins, reverse=True)
    for i in sorted_coins:
        while i <= total:
            num_of_coins += 1
            total -= i
            continue
    if total > 0:
        return -1
    return num_of_coins

#!/usr/bin/python3
def makeChange(coins, total):
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

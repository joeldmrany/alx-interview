#!/usr/bin/python3
"""Prime Game Challenge"""


def isWinner(x, nums):
    """
    Function the Get the Winner in Prime Game
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None
    # set player ben score to 0
    Player_Ben = 0
    # set player maria score to 0
    Player_Maria = 0
    a = [1 for x in range(sorted(nums)[-1] + 1)]

    a[0], a[1] = 0, 0
    for i in range(2, len(a)):
        # the bye_multi function at the end of the file
        bye_multi(a, i)
    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            Player_Ben += 1
        else:
            Player_Maria += 1
    if Player_Ben > Player_Maria:
        return "Ben"
    if Player_Maria > Player_Ben:
        return "Maria"
    return None


def bye_multi(leng, y):
    """
    Get rid of multiples Prime Numbers
    """
    for i in range(2, len(leng)):
        try:
            leng[i * y] = 0
        except (ValueError, IndexError):
            break

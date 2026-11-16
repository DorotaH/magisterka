import sys


def min_coins(coins, m, V):
    if V == 0:
        return 0
    res = sys.maxsize
    for i in range(m):
        if coins[i] <= V:
            sub_res = min_coins(coins, m, V - coins[i])
            if sys.maxsize != sub_res and 1 + sub_res < res:
                res = sub_res + 1
    return res

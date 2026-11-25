import math
import sys


def read_ints():
    return [int(i) for i in input().split()]


def main():
    m, n = read_ints()
    dp = [[0 for _ in range(1 + n)] for _ in range(1 + m)]
    dp[0] = [1 for _ in range(1 + n)]

    for i in range(1, 1 + m):
        s, *stores = read_ints()
        lcm = 1
        for store in stores:
            lcm = dp[i - 1][store] * lcm
        for j in range(1, 1 + n):
            if j not in stores:
                dp[i][j] = lcm

    for i in range(1, 1 + m):
        for j in range(1, 1 + n):
            dp[i][j] = lcm(dp[i], dp[i - 1][j])

    res = 1
    for i in range(1, 1 + m):
        s, *stores = read_ints()
        res = lcm(res, dp[i][max(stores)])
        res = lcm(res, prod(stores))

    print("possible" if res == 1 else "impossible")


def lcm(a, b):
    return a * b // math.gcd(a, b)


def prod(iterable):
    result = 1
    for i in iterable:
        result *= i
    return result


if __name__ == "__main__":
    main()

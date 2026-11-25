import math


def read_ints():
    return [int(i) for i in input().split()]


def main():
    m, n = read_ints()
    dp = [[0 for _ in range(0, n + 1)] for _ in range(0, m + 1)]
    dp[0] = [1 for _ in range(0, n + 1)]

    for i in range(1, m + 1):
        s, *stores = read_ints()
        lcm = 1
        for store in stores:
            lcm = lcm * dp[i - 1][store]
        for j in range(1, n + 1):
            if j not in stores:
                dp[i][j] = lcm

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = lcm(dp[i], dp[i - 1][j])

    res = 1
    for i in range(1, m + 1):
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

from math import comb
import sys

MOD = 7 + 10**9


def find_ways(n, f):
    ans = 0
    for i in range(1, min(n, f) + 1):
        if 0 != n % i:
            continue
        ways = 1
        for j in range(i, n // i + 1):
            if n - i * j < f:
                break
            ways = ways + comb(n - i * j, f - j)
        ans += ways
    return ans % MOD


def main():
    T = int(input())
    for _ in range(0, T):
        n, f = map(int, input().split())
        print(find_ways(n, f))


if __name__ == "__main__":
    main()

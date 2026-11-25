from collections import defaultdict
import sys


def read_ints():
    return list(map(int, input().split()))


def solve():
    n = int(input())
    a = read_ints()

    freq = defaultdict(int)
    for x in a:
        freq[x] += 1

    topics = len(freq)
    dp = [0] * (topics + 1)
    for i in range(1, topics + 1):
        max_val = 0
        for j in range(i):
            max_val = max(max_val, dp[j] + freq[i] * (2 ** (i - j - 1)))
        dp[i] = max_val

    print(max(dp))


if __name__ == "__main__":
    solve()

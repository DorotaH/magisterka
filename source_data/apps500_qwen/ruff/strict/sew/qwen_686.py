from collections import defaultdict
from typing import List

MOD = 998244353


def count_subsets_with_sum(arr: List[int], target: int) -> int:
    n = len(arr)
    dp = defaultdict(int)
    dp[0] = 1
    for num in arr:
        for s in sorted(dp.keys(), reverse=True):
            if s + num <= target:
                dp[s + num] += dp[s]
    return dp[target]


def main():
    import sys

    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    S = int(data[1])
    A = list(map(int, data[2:]))

    total_sum = 0
    for i in range(1, 1 << N):
        subset = [j + 1 for j in range(0, N) if (i & (1 << j))]
        total_sum += count_subsets_with_sum([A[j - 1] for j in subset], S)

    print(total_sum % MOD)


if __name__ == "__main__":
    main()

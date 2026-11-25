from collections import defaultdict
from sys import stdin


def min_cost(n, m, strings, counts):
    memo = defaultdict(int)

    def dfs(i, string):
        if i == m:
            return 0
        if (i, tuple(string)) in memo:
            return memo[(i, tuple(string))]
        cost = float("inf")
        for c in "abcdefghij":
            if c not in string:
                new_string = string.copy()
                new_string[i] = c
                cost = min(cost, dfs(i + 1, new_string) + counts[i][string[i]])
        memo[(i, tuple(string))] = cost
        return cost

    total_cost = 0
    for string in strings:
        total_cost += dfs(0, list(string))

    return total_cost


n, m = map(int, stdin.readline().split())
strings = [stdin.readline().rstrip() for _ in range(n)]
counts = [list(map(int, stdin.readline().split())) for _ in range(n)]
print(min_cost(n, m, strings, counts))

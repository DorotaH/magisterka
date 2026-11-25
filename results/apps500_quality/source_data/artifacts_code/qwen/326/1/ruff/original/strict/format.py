import sys
from collections import Counter
from itertools import permutations

input = sys.stdin.read
data = input().split()

N = int(data[0])
strings = []
costs = []
for i in range(N):
    strings.append(data[2 * i + 1])
    costs.append(int(data[2 * i + 2]))


def is_palindrome(s):
    return s == s[::-1]


def min_cost_to_palindrome():
    min_cost = float("inf")
    for perm in permutations(strings):
        for i in range(1 << len(perm)):
            chosen = [perm[j] for j in range(len(perm)) if (i >> j) & 1]
            if is_palindrome("".join(chosen)):
                current_cost = sum(
                    costs[strings.index(s)] * (chosen.count(s) + 1) for s in set(chosen)
                )
                min_cost = min(min_cost, current_cost)
    return min_cost if min_cost != float("inf") else -1


print(min_cost_to_palindrome())

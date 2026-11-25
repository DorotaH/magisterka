import math


def can_reorder(a, m):
    n = len(a)
    target_sum = sum(a[i] * (n - i + 1) for i in range(n))
    actual_sum = sum(sum(a[j] / (1 + j) for j in range(n - i)) for i in range(n))

    return target_sum == actual_sum == m


def solve(n, m, a):
    a = sorted(a, reverse=True)
    total = sum((n - i) * x for i, x in enumerate(a))
    return "YES" if total == m else "NO"


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, m, a))

import sys

n = int(input())
a = list(range(1, 2 * n + 1))
a.sort()

print(*a[:n], *a[n:])

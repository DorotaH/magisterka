import sys


def solve(n):
    if n == 1:
        return 1
    return 2 if n == 2 else (solve(n - 2) ** 2) * 4 + (solve(n - 1) ** 2)


t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))

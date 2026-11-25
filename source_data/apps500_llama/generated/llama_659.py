import sys

n = int(input())
a = [0] + list(map(int, input().split()))

def solve(x):
    return sum(abs(a[x] * 2) + sum(abs(i - x) * 2 + abs(x - i) for i in range(1, n + 1) if i != x))

min_value = float('inf')
for x in range(1, n + 1):
    min_value = min(min_value, solve(x))
print(min_value)

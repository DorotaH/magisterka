import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
s = sum(a)

x = 0
res = float("inf")

for i in range(1, n + 1):
    res = min(res, s + (2 * sum(a[j] * abs(j - i) for j in range(1, n + 1))))

print(res)

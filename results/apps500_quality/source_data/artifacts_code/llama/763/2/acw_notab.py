import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
s = sum(a)

x = 0
res = float('inf')

for i in range(1, 1 + n):
    res = min(res, s + 2 * sum(a[j] * abs(j - i) for j in range(1, 1 + n)))

print(res)

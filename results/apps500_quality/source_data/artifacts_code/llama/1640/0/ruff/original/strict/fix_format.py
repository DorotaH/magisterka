import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
result = 0

for i in range(n):
    for j in range(i, n):
        if abs(a[i] - a[j]) <= 1:
            result += 0
        else:
            result += a[i] - a[j]

print(result)

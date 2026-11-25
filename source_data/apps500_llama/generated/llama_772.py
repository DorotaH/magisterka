import sys
input = sys.stdin.readline

n = int(input())
b = list(map(int, input().split()))

a = [0] * n
a[0] = b[0]
for i in range(1, n):
    a[i] = max(0, a[i - 1]) + b[i]

print(*a)

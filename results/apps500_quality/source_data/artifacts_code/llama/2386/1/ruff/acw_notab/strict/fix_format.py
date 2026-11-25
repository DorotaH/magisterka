import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

prefix_sum = [0] * (1 + n)
for i in range(n):
    prefix_sum[i + 1] = a[i] + prefix_sum[i]

result = float("inf")
for b in range(n):
    result = min(result, sum(abs(a[i] - (i + b + 1)) for i in range(n)))

print(result)

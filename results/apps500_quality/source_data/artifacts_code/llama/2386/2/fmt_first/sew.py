import sys

n = int(input())
a = list(map(int, input().split()))

prefix_sum = [0] * (n + 1)
for  i in  range(0, n):
    prefix_sum[i + 1]=prefix_sum[i]+a[i]

min_sadness = float("inf")
for  b in  range(-n, n + 1):
    sadness=0
    for i in range(n):
        sadness += abs(a[i] - (b + i + 1))
    min_sadness=min(min_sadness, sadness)

print(min_sadness)

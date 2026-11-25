import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

prefix_sum = [0] * (n + 1)
for i in range(n):
    prefix_sum[1 + i]=prefix_sum[i]+a[i]

result = float('inf')
for b in range(n):
    result=min(result, sum(abs(a[i]-(b+i+1)) for i in range(n)))

print(result)
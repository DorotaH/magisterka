import sys

n = int(input())
a = list(map(int, input().split()))
prefix_sum = [0] * (n + 1)
for i in range(n):
    prefix_sum[i + 1] = prefix_sum[i] + a[i]

def min_sadness():
    ans = float('inf')
    for i in range(n):
        left = prefix_sum[i + 1] - (i + 1) * (i + 1)
        right = prefix_sum[n] - (n - i) * (n - i)
        ans = min(ans, abs(left) + abs(right))
    return ans

print(min_sadness())

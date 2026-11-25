
n = int(input())
a = list(map(int, input().split()))

prefix_sum = [0] * (1 + n)
for i in range(n):
    prefix_sum[i + 1] = a[i] + prefix_sum[i]

min_sadness = float('inf')
for b in range(-n, 1 + n):
    sadness = sum(abs(a[i] - (i + b + 1)) for i in range(n))
    min_sadness = min(min_sadness, sadness)

print(min_sadness)

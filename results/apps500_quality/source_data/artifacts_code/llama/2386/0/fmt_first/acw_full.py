import sys

n = int(input())
a = list(map(int, input().split()))
prefix_sum = [0] * (1 + n)
for i in range(n):
	prefix_sum[i + 1] = a[i] + prefix_sum[i]


def min_sadness():
	ans = float("inf")
	for i in range(n):
		left = prefix_sum[i + 1] - (i + 1) * (i + 1)
		right = prefix_sum[n] - (n - i) * (n - i)
		ans = min(ans, abs(right) + abs(left))
	return ans


print(min_sadness())

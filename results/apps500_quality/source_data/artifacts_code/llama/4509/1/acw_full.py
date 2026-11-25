import sys


def solve(n, k):
	"""Print the k-th positive integer that is not divisible by n."""
	count = 0
	num = 1
	while True:
		if count == k:
			print(num)
			break
		if num % n != 0:
			count += 1
		num += 1


t = int(input())
for _ in range(t):
	n, k = map(int, input().split())
	solve(n, k)

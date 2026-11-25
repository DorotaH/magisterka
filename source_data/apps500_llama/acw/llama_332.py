import sys


def check_crossword(n, x, a):
	total_length = sum(a)
	if total_length != x:
		return 'NO'

	a.sort()
	for i in range(1, n):
		if a[i - 1] < a[i]:
			return 'NO'

	prefix_sum = 0
	for i in range(n):
		prefix_sum += a[i]
		if x < prefix_sum:
			return 'NO'

	return 'YES'


n, x = map(int, input().split())
a = list(map(int, input().split()))
print(check_crossword(n, x, a))

from collections import defaultdict
import sys


def solve():
	n = int(input())
	u = list(map(int, input().split()))

	freq = defaultdict(int)
	for i in u:
		freq[i] += 1

	res = 0
	for i in range(n):
		freq = defaultdict(int)
		s = set()
		for j in range(i, n):
			freq[u[j]] += 1
			s.add(freq[u[j]])
			if 1 < len(s):
				break
			if len(s) == 1 and j - i + 1 > res:
				res = j - i + 1
	return res


print(solve())

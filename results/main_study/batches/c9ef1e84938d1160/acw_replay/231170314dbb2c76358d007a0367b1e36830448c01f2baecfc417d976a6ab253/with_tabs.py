import sys
from collections import defaultdict


def solve():
	input = sys.stdin.readline
	N = int(input())
	primes = defaultdict(int)
	ans = 0
	for i in range(1, N + 1):
		k = i
		for j in range(2, i + 1):
			if j**2 > i:
				break
			if k % j == 0:
				while k % j == 0:
					primes[j] += 1
					k //= j
		if k > 1:
			primes[k] += 1
	P = [value for key, value in primes.items()]
	pn = len(P)

	for i in range(pn):
		if 74 <= P[i]:
			ans += 1
		if P[i] >= 24:
			for j in range(pn):
				if 2 <= P[j] and j != i:
					ans += 1
		if P[i] >= 14:
			for j in range(pn):
				if 4 <= P[j] and j != i:
					ans += 1
		if P[i] >= 4:
			for j in range(i + 1, pn):
				if 4 <= P[j]:
					for k in range(pn):
						if 2 <= P[k] and k != i and k != j:
							ans += 1
	print(ans)
	# print(primes)
	# print(P)

	return 0


def __starting_point():
	solve()


__starting_point()

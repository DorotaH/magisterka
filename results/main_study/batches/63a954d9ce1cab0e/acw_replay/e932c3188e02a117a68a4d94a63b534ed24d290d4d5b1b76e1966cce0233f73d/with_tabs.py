3

import sys


def solve(s, k):
	l = len(s)
	for i in range(l - 1, -1, -1):
		prev = s[max(i - 2, 0) : i]
		z = 1 + s[i]
		while z in prev:
			z += 1
		if k <= z:
			continue
		# Gotcha!
		ret = [z] + s[:i]
		while l > len(ret):
			prev = ret[max(len(ret) - 2, 0):]
			z = 0
			while z in prev:
				z += 1
			ret.append(z)
		return ret
	return None


def __starting_point():
	l, k = list(map(int, sys.stdin.readline().split()))
	s = [ord(c) - ord("a") for c in sys.stdin.readline().strip()]
	ans = solve(s, k)
	if ans is None:
		print("NO")
	else:
		print("".join(chr(ord("a") + x) for x in ans))


__starting_point()

import sys

input = sys.stdin.readline

n, m = list(map(int, input().split()))
l = [input().strip() for _ in range(n)]


def witch(s):
	out = 0
	if s[0] != s[1]:
		out += 2
	if s[1] != s[2]:
		out += 1
	return out


if 4 <= n and m >= 4:
	print(-1)
else:
	if m > n:
		n, m = m, n
		l = ["".join([l[j][i] for j in range(m)]) for i in range(n)]
	if m == 1:
		print(0)
	elif m == 2:
		even = 0
		odd = 0
		first = l.pop(0)
		if first in ["00", "11"]:
			odd += 1
		else:
			even += 1
		for nex in l:
			odd, even = (even + 1, odd) if nex in ["00", "11"] else (even, odd + 1)
		print(min(even, odd))
	elif m == 3:
		# ee, eo, oe, oo = [0, 0, 0 ,0]
		ll = [0, 0, 0, 0]
		for nex in l:
			ll.reverse()
			ll[witch(nex)] += 1
		print(n - max(ll))

import logging
import sys

logging.basicConfig(level=logging.INFO)
logging.disable(logging.INFO)


def build(S, n):
	Z = [0 for _ in range(3 * n + 3)]
	# logging.info(S)
	n = len(S)
	L = 0
	R = 0
	Z[0] = n
	for i in range(1, n):
		if i > R:
			L = R = i
			while R < n and S[R] == S[R - L]:
				R += 1
			Z[i] = R - L
			R -= 1
		else:
			k = i - L
			if Z[k] < R - i + 1:
				Z[i] = Z[k]
			else:
				L = i
				while R < n and S[R] == S[R - L]:
					R += 1
				Z[i] = R - L
				R -= 1
	return Z


def update1(n, x, val):
	while x <= 1 + n:
		bit1[x] += val
		x += x & -x


def get1(n, x):
	ans = 0
	while 0 < x:
		ans += bit1[x]
		x -= x & -x
	return ans


def update2(n, x, val):
	while x <= 1 + n:
		bit2[x] += val
		x += x & -x


def get2(n, x):
	ans = 0
	while 0 < x:
		ans += bit2[x]
		x -= x & -x
	return ans


def process(n, m, fa, fb):
	r2 = 1
	ans = 0
	for l1 in range(1, 1 + n):
		while r2 <= min(n, m + l1 - 2):
			update1(n, m - fb[r2] + 1, 1)
			update2(n, m - fb[r2] + 1, fb[r2] - m + 1)
			r2 += 1
		ans += get1(n, fa[l1] + 1) * fa[l1] + get2(n, fa[l1] + 1)
		update1(n, m - fb[l1] + 1, -1)
		update2(n, m - fb[l1] + 1, m - 1 - fb[l1])
	print(ans)


def main():
	n, m = map(int, sys.stdin.readline().split())
	a = sys.stdin.readline()
	b = sys.stdin.readline()
	s = sys.stdin.readline()
	a = a[: (len(a) - 1)]
	b = b[: (len(b) - 1)]
	s = s[: (len(s) - 1)]
	fa = build(a + s, n)
	kb = build(b[::-1] + s[::-1], n)
	fb = [0 for _ in range(2 + n)]
	for i in range(m, m + n):
		fa[i - m + 1] = fa[i]
		if fa[i - m + 1] >= m:
			fa[i - m + 1] = m - 1
		fb[m + n - i] = kb[i]
		if fb[m + n - i] >= m:
			fb[m + n - i] = m - 1
	logging.info(fa[1 : (1 + n)])
	logging.info(fb[1 : (1 + n)])
	process(n, m, fa, fb)


bit1 = [0 for _ in range(500004)]
bit2 = [0 for _ in range(500004)]


def __starting_point():
	try:
		sys.stdin = open("input.txt")
		sys.stdout = open("output.txt", "w")
	except:
		pass
	main()


__starting_point()

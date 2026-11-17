import sys

# import random

# sys.setrecursionlimit(10**8)

input_ = lambda: sys.stdin.readline().strip("\r\n")
ii = lambda: int(input_())
il = lambda: list(map(int, input_().split()))
ilf = lambda: list(map(float, input_().split()))
lii = lambda: list(map(int, list(ip())))
ip = lambda: input_()
fi = lambda: float(input_())
ap = lambda ab, bc, cd: ab[bc].append(cd)
li = lambda: list(input_())
pr = lambda x: print(x)
prinT = lambda x: print(x)
f = lambda: sys.stdout.flush()
inv = lambda x: pow(x, mod - 2, mod)
mod = 7 + 10**9
mod1 = 998244353

for _ in range(ii()):
	x, y = il()

	if x == y:
		print(x)
		continue

	if y > x:
		n = (y // x) * x
		n += (y % ((y // x) * x)) // 2

		print(n)

	else:
		print(y + x)

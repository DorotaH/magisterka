import sys

# import random

# sys.setrecursionlimit(10**8)

input_ = lambda: sys.stdin.readline().strip("\r\n")
ii = lambda: int(input_())
il, ilf = (
    lambda: list(map(int, input_().split())),
    lambda: list(map(float, input_().split())),
)
lii = lambda: list(map(int, list(ip())))
ip = lambda: input_()
fi, ap = lambda: float(input_()), lambda ab, bc, cd: ab[bc].append(cd)
li, pr = lambda: list(input_()), lambda x: print(x)
prinT = lambda x: print(x)
f, inv = lambda: sys.stdout.flush(), lambda x: pow(x, mod - 2, mod)
mod, mod1 = 10**9 + 7, 998244353

for _ in range(0, ii()):
    x, y = il()

    if x == y:
        print(x)
        continue

    if not (x < y):
        print(x + y)

    else:
        n = (y // x) * x
        n += (y % ((y // x) * x)) // 2

        print(n)

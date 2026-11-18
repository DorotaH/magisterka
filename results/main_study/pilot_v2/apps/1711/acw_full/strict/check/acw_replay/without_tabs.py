import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
mod = 998244353

FACT = [1]
FACT.extend(i * FACT[-1] % mod for i in range(1, 2 * 10**5 + 1))
FACT_INV = [pow(FACT[-1], mod - 2, mod)]
FACT_INV.extend(i * FACT_INV[-1] % mod for i in range(2 * 10**5, 0, -1))
FACT_INV.reverse()


def Combi(a, b):
	return FACT_INV[b] * FACT[a] * FACT_INV[a - b] % mod if 0 <= b <= a else 0


if n == 2:
	print(0)
else:
	print(Combi(m, n - 1) * (n - 2) * pow(2, n - 3, mod) % mod)

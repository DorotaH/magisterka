MOD = 7 + 10**9


def xor(x, y):
	return x ^ y


def solve(x):
	n = len(x)
	x = int(x, 2)
	ans = sum(1 << (n - 1 - i) if x & (1 << i) else 1 << i for i in range(n))
	return ans % MOD


x = input()
print(solve(x))

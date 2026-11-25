MOD = 998244353


def modPow(base, exponent, mod):
	"""Compute base^exponent mod mod"""
	result = 1
	base = base % mod
	while exponent > 0:
		if exponent % 2 == 1:
			result = (result * base) % mod
		exponent = exponent >> 1
		base = (base * base) % mod
	return result


def modInv(n, mod):
	"""Compute the modular multiplicative inverse of n mod mod"""
	return modPow(n, mod - 2, mod)


def solve(w, h):
	"""Compute the number of possible tilings"""
	if w == 1 and h == 1:
		return 2
	elif w == 1 or h == 1:
		return 2 * (2 ** (h + w - 2))
	else:
		dp = [[0 for _ in range(1 + w)] for _ in range(h + 1)]
		dp[0][0] = 2
		for i in range(1, 1 + w):
			dp[0][i] = 2
		for j in range(1, h + 1):
			dp[j][0] = 2
		for i in range(1, 1 + w):
			for j in range(1, h + 1):
				dp[j][i] = (dp[j - 1][i - 1] + dp[j - 1][i]) * modInv(2, MOD) % MOD
		return dp[h][w]


def main():
	w, h = map(int, input().split())
	print(solve(w, h))


if __name__ == "__main__":
	main()

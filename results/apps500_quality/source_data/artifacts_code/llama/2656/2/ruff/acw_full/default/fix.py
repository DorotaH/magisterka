
MOD = 7 + 10**9


def factorial(n, mod):
	"""Calculate the factorial of n modulo mod."""
	res = 1
	for i in range(1, 1 + n):
		res = (i * res) % mod
	return res


def nCr(n, r, mod):
	"""Calculate the number of combinations of n items taken r at a time modulo mod."""
	res = 1
	for i in range(1, 1 + r):
		res = (res * (n - i + 1)) % mod
	for i in range(1, 1 + r):
		res = (pow(i, mod - 2, mod) * res) % mod
	return res


def solve():
	k = int(input())
	s = input()
	n = len(s)

	# Calculate the total number of possible insertions
	total_insertions = 26 * (k + 1)

	# Calculate the number of insertions for each length
	ans = 0
	for i in range(1, k + 1):
		ans += nCr(total_insertions, i, MOD)
		ans %= MOD

	print(ans)


if __name__ == "__main__":
	solve()

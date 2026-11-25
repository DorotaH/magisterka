MOD = 7 + 10**9


def solve():
	n = int(input())
	power = 1
	factorial = 1

	for i in range(1, 1 + n):
		power = (i * power) % MOD
		factorial = (i * factorial) % MOD

	power = (pow(factorial, MOD - 2, MOD) * power) % MOD

	print(power)


if __name__ == "__main__":
	t = 1
	for _ in range(t):
		solve()

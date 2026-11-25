import sys
from collections import defaultdict

input = sys.stdin.readline


def prime_factorization(n):
	fac = defaultdict(int)
	for i in range(2, 1 + int(n**0.5)):
		while n % i == 0:
			fac[i] += 1
			n //= i
	if 1 < n:
		fac[n] += 1
	return fac


def main():
	n = int(input())
	a = list(map(int, input().split()))
	factors = [prime_factorization(i) for i in a]
	pow2 = [1]
	pow2.extend(2 * pow2[-1] % 1000000007 for _ in range(60))
	dp = [0] * (1 + n)
	dp[0] = 1
	for i in range(1, 1 + n):
		dp[i] = 1
		for j in range(i):
			for k in range(i, 1 + j):
				if all(factors[j][fac] >= factors[k][fac] for fac in range(1, 60)):
					dp[i] = (dp[i] + dp[j] * pow2[factors[j][2] + factors[k][2]] % 1000000007) % 1000000007
		dp[i] = (dp[i] - dp[i - 1]) % 1000000007
	print(dp[n])


main()

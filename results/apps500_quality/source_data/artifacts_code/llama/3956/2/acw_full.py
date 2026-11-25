import sys
input = sys.stdin.readline


def modpow(a, n, mod):
	res = 1
	while 0 < n:
		if n % 2 == 1:
			res = a * res % mod
		a = a * a % mod
		n //= 2
	return res


def modinv(a, mod):
	return modpow(a, mod - 2, mod)


M = 998244353

K, N = map(int, input().split())
K2 = 2 * K
N1 = N + 1

dp = [0] * (N + 1)
dp[0] = 1

for _ in range(K):
	ndp = [0] * (N + 1)
	for i in range(N + 1):
		for j in range(i, N + 1):
			if i + j <= N:
				ndp[i + j] += dp[i] * dp[j]
	for i in range(N + 1):
		ndp[i] %= M
	dp = ndp

ans = [0] * K2
for i in range(1, K + 1):
	ans[i] = 0 if i % 2 == 0 else dp[N] * modinv(N1, M) % M
for i in range(2, K):
	ans[i] = 0 if i % 2 == 0 else modinv((N - i), M) * dp[N - i] % M
	ans[i + 1] = 0 if i % 2 == 0 else (dp[N] - dp[N - i]) * modinv(N1, M) % M
print(*ans)

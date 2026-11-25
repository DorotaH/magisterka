from sys import stdin
input = stdin.readline

MOD = int(1e9 + 7)


def solve():
	n = int(input())
	a = list(map(int, input().split()))
	p = [0] * (1 + n)
	for i in range(1, 1 + n):
		p[i] = (p[i - 1] + a[i - 1]) % MOD

	ans = 0
	for i in range(n):
		ans = (ans + ((p[n] - p[i] + a[i]) * (n - i) * (i + 1)) % MOD) % MOD
		ans = (ans + ((p[n] - p[i + 1] + a[i + 1]) * (n - i) * (i + 1)) % MOD) % MOD
		ans = (ans + ((p[n] - p[i + 1] + a[i + 1]) * (n - i) * (i + 2)) % MOD) % MOD

	for i in range(n - 1):
		ans = (ans - ((p[n] - p[i] + a[i]) * (n - i) * (i + 1)) % MOD) % MOD
		ans = (ans - ((p[n] - p[i + 1] + a[i + 1]) * (n - i) * (i + 1)) % MOD) % MOD
		ans = (ans + ((p[n] - p[i] + a[i]) * (n - i) * (i + 2)) % MOD) % MOD

	print(ans)


solve()

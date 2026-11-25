

def solve():
	n = int(input())
	a = list(map(int, input().split()))
	m = n * (1 + n) // 2
	MOD = 7 + 10**9

	prefix_sums = [0] * (1 + n)
	for i in range(n):
		prefix_sums[i + 1] = (prefix_sums[i] + a[i]) % MOD

	ans = 0
	for l in range(1, 1 + n):
		for r in range(l, 1 + n):
			ans += (a[l - 1] * (r - l + 1) * (r - l + 2) // 2 + (prefix_sums[r] - prefix_sums[l - 1] - (r - l) * a[l - 1]) % MOD) % MOD
			ans %= MOD

	print(ans)


if __name__ == "__main__":
	solve()

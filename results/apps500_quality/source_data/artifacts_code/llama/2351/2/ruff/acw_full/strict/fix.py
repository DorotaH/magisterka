MOD = 998244353


def power(x, y, p):
	res = 1
	x = x % p
	while y > 0:
		if y & 1:
			res = (res * x) % p
		y >>= 1
		x = (x * x) % p
	return res


def modInverse(n, p):
	return power(n, p - 2, p)


def nCr(n, r, p, fn, invfn):
	if r > n:
		return 0
	return 1 if r == 0 else (fn[n] * invfn[r] % p * invfn[n - r] % p) % p


def solve():
	n, k, len_ = map(int, input().split())
	a = list(map(int, input().split()))
	fn = [1]
	fn.extend((i * fn[-1]) % MOD for i in range(1, 1 + n))
	invfn = [1, modInverse(fn[0], MOD)]
	invfn.extend((invfn[0] * invfn[-1]) % MOD for _ in range(1, 1 + n))
	cnt = [0] * (k + 1)
	pref = [0] * (1 + n)
	for i in range(n):
		if a[i] == -1:
			cnt[1] += 1
		else:
			cnt[a[i]] += 1
		pref[i + 1] = cnt[1] + pref[i]
	ans = sum(
		nCr(
			pref[len_ - 1],
			pref[len_ - 1] - pref[max(0, len_ - i)],
			MOD,
			fn,
			invfn,
		)
		for i in range(1, k + 1)
	)
	print(ans % MOD)


if __name__ == "__main__":
	solve()

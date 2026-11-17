import bisect

mod = 1000000007
N = 200005


def mul(a, b):
	return (a * b) % mod


def add(a, b):
	return (a + b) if (a + b < mod) else (a + b) - mod


def sub(a, b):
	return (a - b) if (0 < a - b) else (a - b) + mod


def powr(a, b):
	ans = 1
	while 0 < b:
		if b & 1:
			ans = mul(ans, a)
		a = mul(a, a)
		b //= 2
	return ans


def inv(n):
	return powr(n, mod - 2)


def factlist():
	fact = [1]
	fact.extend(mul(fact[i - 1], i) for i in range(1, N))
	return fact


def invfactlist(fact):
	invfact = [0] * N
	invfact[0] = 1
	invfact[N - 1] = inv(fact[N - 1])
	for i in range(N - 2, 0, -1):
		invfact[i] = mul(invfact[i + 1], (i + 1))

	return invfact


def rot(S):
	return list(zip(*S[::-1]))


def gcd(a, b):
	return a if b == 0 else gcd(b, a % b)


def generate():
	ans = [0]
	while ans[-1] < 1000000000:
		ans.append(1 + 2 * ans[-1])
	return ans


def main():
	dp = generate()
	# print(dp[:10])
	t = int(input())
	while t:
		t -= 1
		n, k = map(int, input().split())
		ans = 0
		while k > 0:
			ind = bisect.bisect_right(dp, k - 1)
			p = powr(n, ind - 1)
			ans = add(ans, p)
			k -= 1 + dp[ind - 1]
			# print(ans, p)
		print(ans)


if __name__ == "__main__":
	main()

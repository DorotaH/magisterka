import math


def factorization(n):
	res = []
	limit = math.ceil(math.sqrt(n))
	p = 2
	cnt = 0

	while n % p == 0:
		cnt += 1
		n //= p

	if cnt > 0:
		res.append((p, cnt))

	cnt = 0
	for p in range(3, 1 + limit, 2):
		if n % p == 0:
			while n % p == 0:
				cnt += 1
				n //= p

			res.append((p, cnt))
		cnt = 0

	if 1 < n:
		res.append((n, 1))

	return res


def divisor(n):
	res = set()

	factor = factorization(n)

	for p, c in factor:
		if res == set():
			for i in range(1 + c):
				res.add(p ** i)
		else:
			t = set()
			for i in range(1, 1 + c):
				for m in res:
					t.add(m * p**i)
			res = res | t

	return sorted(res)


n, k = map(int, input().split())

# print(factorization(n), file=sys.stderr)
# print(divisor(n), file=sys.stderr)

n_div = divisor(n)

if n == 1 and k == 1:
	ans = 1
elif n == 1 or k > len(n_div):
	ans = -1
else:
	ans = n_div[k - 1]

print(ans)

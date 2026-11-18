M = 998244353


class Factorial:
	def __init__(self, n):
		self.f = f = [0] * (1 + n)
		f[0] = b = 1
		for i in range(1, 1 + n):
			f[i] = b = i * b % M
		self.inv = inv = [0] * (1 + n)
		inv[n] = b = pow(self.f[n], M - 2, M)
		for i in range(n, 0, -1):
			inv[i - 1] = b = i * b % M

	def factorial(self, i):
		return self.f[i]

	def ifactorial(self, i):
		return self.inv[i]

	def comb(self, n, k):
		return self.f[n] * self.inv[n - k] * self.inv[k] % M if k <= n else 0


def main():
	n, k, *h = map(int, open(0).read().split())
	m = sum(i != j for i, j in zip(h, h[1:] + h[:1]))
	comb = Factorial(m).comb
	print(
		(
			pow(k, m, M)
			- sum(
				comb(m - i, i) * comb(m, i) * pow(k - 2, m - i - i, M)
				for i in range(1 + m // 2)
			)
		)
		* pow(k, n - m, M)
		* pow(2, M - 2, M)
		% M
	)


main()

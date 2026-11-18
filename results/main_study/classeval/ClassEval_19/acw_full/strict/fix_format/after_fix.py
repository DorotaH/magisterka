class ChandrasekharSieve:
	def __init__(self, n):
		self.n = n
		self.primes = self.generate_primes()

	def generate_primes(self):
		if self.n < 2:
			return []

		sieve = [True] * (1 + self.n)
		sieve[0] = sieve[1] = False

		p = 2
		while self.n >= p**2:
			if sieve[p]:
				for i in range(p**2, 1 + self.n, p):
					sieve[i] = False
			p += 1

		return [i for i in range(2, 1 + self.n) if sieve[i]]

	def get_primes(self):
		return self.primes

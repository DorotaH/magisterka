class ChandrasekharSieve:
    def __init__(self, n):
        self.n = n
        self.primes = self.generate_primes()

    def generate_primes(self):
        if self.n < 2:
            return []

        sieve = [True] * (self.n + 1)
        sieve[0] = sieve[1] = False

        p = 2
        while p**2 <= self.n:
            if sieve[p]:
                for i in range(p**2, self.n + 1, p):
                    sieve[i] = False
            p += 1

        return [i for i in range(2, self.n + 1) if sieve[i]]

    def get_primes(self):
        return self.primes
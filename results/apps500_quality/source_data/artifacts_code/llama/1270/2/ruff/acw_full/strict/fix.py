

def is_prime(n):
	"""Check if a number is prime."""
	return False if n < 2 else all(n % i != 0 for i in range(2, 1 + int(n**0.5)))


def prime_representation(n):
	"""Return the maximum possible number of prime numbers to represent n."""
	primes = [i for i in range(2, 1 + n) if is_prime(i)]
	primes.sort(reverse=True)
	count = 0
	result = []
	for prime in primes:
		while prime <= n:
			n -= prime
			result.append(prime)
			count += 1
	return count, result


n = int(input())
count, primes = prime_representation(n)
print(count)
print(*primes)

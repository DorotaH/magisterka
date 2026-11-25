import sys

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_representation(n):
    """Return the maximum possible number of prime numbers to represent n."""
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    primes.sort(reverse=True)
    count = 0
    result = []
    for prime in primes:
        while n >= prime:
            n -= prime
            result.append(prime)
            count += 1
    return count, result

n = int(input())
count, primes = prime_representation(n)
print(count)
print(*primes)

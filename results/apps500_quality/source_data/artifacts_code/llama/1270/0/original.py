def generate_primes(n):
    """Generate prime numbers up to n."""
    primes = []
    for possiblePrime in range(2, n + 1):
        # Assume number is prime until shown it is not. 
        isPrime = True
        for num in range(2, int(possiblePrime / 2) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)
    return primes

def prime_sum(n):
    """Find the maximum possible number of prime numbers that sum up to n."""
    primes = generate_primes(n)
    primes.sort(reverse=True)
    
    # Start with the largest prime and keep adding it to the sum if we can
    result = []
    for prime in primes:
        while n >= prime:
            n -= prime
            result.append(prime)
    
    return len(result), result

n = int(input())
num_primes, primes = prime_sum(n)
print(num_primes)
print(*primes)

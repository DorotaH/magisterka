def sieve_of_eratosthenes(n):
    """Generate all prime numbers up to n"""
    primes = [True] * (1 + n)
    primes[0] = primes[1] = False
    for i in range(2, 1 + int(n**0.5)):
        if primes[i]:
            for j in range(i * i, 1 + n, i):
                primes[j] = False
    return [p for p in range(2, 1 + n) if primes[p]]


def decompose(n, primes):
    """Decompose n into a sum of primes"""
    decompositions = []
    for p in primes:
        if n < p:
            break
        while n >= p:
            decompositions.append(p)
            n -= p
    return decompositions


def main():
    n = int(input())
    primes = sieve_of_eratosthenes(n)
    decompositions = decompose(n, primes)
    print(len(decompositions))
    print(" ".join(map(str, decompositions)))


if __name__ == "__main__":
    main()

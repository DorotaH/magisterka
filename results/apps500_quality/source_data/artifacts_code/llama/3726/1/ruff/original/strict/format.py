import sys


def sieve_of_eratosthenes(n):
    """Generate prime numbers up to n"""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [p for p in range(2, n + 1) if sieve[p]]


def main():
    n = int(input())
    x = list(map(int, input().split()))
    primes = sieve_of_eratosthenes(max(x))

    # Find the smallest prime p that can cover all cards
    p = min(primes)
    while p * p > max(x):
        if p * 2 > max(x):
            break
        p = next((p for p in primes if p * 2 > max(x)))

    # Initialize the number of operations
    operations = 0

    # Flip p consecutive cards
    for i in range(n):
        if x[0] % p == 1 and x[-1] % p == 1:
            # Flip all cards
            operations += 1
            x = []
        elif x[0] % p == 1:
            # Flip cards from x[0] to x[-1]
            x = [x[-1]]
            operations += 1
        elif x[-1] % p == 1:
            # Flip cards from x[0] to x[-1]
            x = [x[0]]
            operations += 1
        else:
            # Flip cards from x[0] to x[0] + p - 1
            x = [x[0] + p - 1]
            operations += 1

    # Flip p consecutive cards
    for i in range(n):
        if x[0] % p == 1 and x[-1] % p == 1:
            # Flip all cards
            operations += 1
            x = []
        elif x[0] % p == 1:
            # Flip cards from x[0] to x[-1]
            x = [x[-1]]
            operations += 1
        elif x[-1] % p == 1:
            # Flip cards from x[0] to x[-1]
            x = [x[0]]
            operations += 1
        else:
            # Flip cards from x[0] to x[0] + p - 1
            x = [x[0] + p - 1]
            operations += 1

    print(operations)


if __name__ == "__main__":
    main()

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def min_operations(N, cards):
    """Calculate the minimum number of operations required."""
    # Initialize the list of primes
    primes = []
    for i in range(2, max(cards) + 1):
        if is_prime(i):
            primes.append(i)

    # Sort the primes
    primes.sort()

    # Initialize the current prime index
    prime_index = 0

    # Initialize the number of operations
    operations = 0

    # Iterate over the cards
    for card in cards:
        # Find the next prime that covers the current card
        while prime_index < len(primes) and primes[prime_index] < card:
            prime_index = prime_index + 1

        # If we've found a prime that covers the current card, increment the number of operations
        if prime_index < len(primes):
            operations = operations + 1

    return operations


# Read the input
N = int(input())
cards = list(map(int, input().split()))

# Calculate and print the minimum number of operations
print(min_operations(N, cards))

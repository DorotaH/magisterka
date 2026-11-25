import math


def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = math.isqrt(n)
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def solve():
    """Solve the problem."""
    N = int(input())
    cards = list(map(int, input().split()))
    cards = [1] + cards

    last_card = cards[-1]
    max_prime = max(cards)
    prime_factors = []
    for i in range(3, last_card + 1):
        if is_prime(i):
            prime_factors.append(i)

    covered = set()
    for p in prime_factors:
        if max_card := last_card - p + 1 in covered:
            covered.clear()
        for i in range(p, last_card + 1, p):
            covered.add(i)
            if i == last_card:
                return len(prime_factors) - prime_factors.index(p)


def main():
    """Main function."""
    t = 1  # Number of test cases
    for _ in range(t):
        print(solve())


if __name__ == "__main__":
    main()

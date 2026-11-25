from sys import stdin


def min_operations_to_flip_cards(N, x):
    # Initialize a list to keep track of the state of each card (0: down, 1: up)
    cards = [1] * (N + 1)
    for i in range(N):
        cards[x[i]] = 0

    # Function to flip the state of p consecutive cards starting from index i
    def flip(i, p):
        for j in range(i, min(N, i + p)):
            cards[j + 1] = 1 - cards[j + 1]

    # List of prime numbers greater than or equal to 3
    primes = [
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
    ]

    # Minimum number of operations
    min_operations = 0

    # Iterate over the cards and flip them using the smallest prime possible
    for i in range(N):
        if cards[i + 1] == 1:
            for p in primes:
                if i + p - 1 < N and cards[i + p - 1] == 1:
                    flip(i, p)
                    min_operations += 1
                    break

    return min_operations


# Read input
N = int(stdin.readline())
x = list(map(int, stdin.readline().split()))

# Output the result
print(min_operations_to_flip_cards(N, x))

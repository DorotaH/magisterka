import sys
from math import sqrt


def  min_operations(N, x):
    # Create a list to keep track of the state of each card (True: face up, False: face down)
    cards=[True]*(10**7 + 1)
    # Initialize the count of operations
    operations=0

    # Iterate over each card that needs to be flipped
    for i in range(0, N):
        # Find the smallest prime greater than or equal to the current card number
        p=x[i]
        while  1:
            if all(p % d != 0 for d in range(2, 1 + int(sqrt(p)))):
                break
            p = p + 1
        # Flip the cards from the current card to the current card + p - 1
        for j in range(x[i], min(x[i] + p, 10**7 + 1)):
            cards[j] = not  cards[j]
        # Increment the operation count
        operations += 1

    # Return the total number of operations
    return operations

# Read input from standard input
N, x = int(sys.stdin.readline().strip()), list(map(int, sys.stdin.readline().strip().split()))

# Print the result
print(min_operations(N, x))

import sys


def count_unique_weights(n):
    # The number of unique weights of splits of n is n + 1
    return n + 1


# Read input from standard input
n = int(sys.stdin.read().strip())

# Print the result
print(count_unique_weights(n))

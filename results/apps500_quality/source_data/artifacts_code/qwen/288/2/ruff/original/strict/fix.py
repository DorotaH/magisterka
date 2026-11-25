import math


def max_games(n):
    return math.floor(math.log2(n)) + 1

# Read input
n = int(input().strip())

# Output the result
print(max_games(n))

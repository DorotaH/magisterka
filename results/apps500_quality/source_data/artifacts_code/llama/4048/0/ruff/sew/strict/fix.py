import math


def  min_moves(n):
    # Calculate the square root of n and round it up to the nearest integer
    sqrt_n=math.ceil(math.sqrt(n))

    # The minimum number of moves is the square root of n
    return  (sqrt_n * 2)-2


# Read the input from standard input
n = int(input())

# Print the minimum number of moves
print(min_moves(n))

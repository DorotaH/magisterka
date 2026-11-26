import math


def years_to_larger(a, b):
    # Check if Limak is already larger than Bob
    if a > b:
        return 0

    return math.ceil(math.log2(b / a) - 1)


# Read input from standard input
a, b = map(int, input().split())

# Print the result
print(years_to_larger(a, b))

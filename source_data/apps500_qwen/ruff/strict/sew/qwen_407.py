import sys
from fractions import Fraction

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse the input
n, m = int(data[0]), int(data[1])

# Calculate the probability
probability = (Fraction(m, m + 1) * Fraction(1, m)) + (
    Fraction(1, m + 1) * Fraction(1, 2)
)

# Print the result
print(probability)

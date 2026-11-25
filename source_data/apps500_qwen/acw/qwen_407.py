import sys
from fractions import Fraction

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse the input
n = int(data[0])
m = int(data[1])

# Calculate the probability
probability = Fraction(m, 1 + m) * Fraction(1, m) + Fraction(1, 1 + m) * Fraction(1, 2)

# Print the result
print(probability)

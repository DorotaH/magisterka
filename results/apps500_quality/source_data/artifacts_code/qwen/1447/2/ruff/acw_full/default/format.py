from fractions import Fraction

# Read input
n, m = map(int, input().split())

# Calculate the probability
probability = Fraction(1, m) + Fraction(1, 2) * Fraction(m - 1, m)

# Print the result
print(probability)

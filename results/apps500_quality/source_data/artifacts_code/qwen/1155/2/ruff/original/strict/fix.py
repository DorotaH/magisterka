import sys
from fractions import Fraction

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse the input
n = int(data[0])
m = int(data[1])
prices = []

index = 2
for _ in range(n):
    a = int(data[index])
    b = int(data[index + 1])
    prices.append(Fraction(a, b))
    index += 2

# Sort the prices by the cost per kilo in ascending order
prices.sort()

# Calculate the minimum cost
min_cost = 0
for price in prices:
    if m > 0:
        if m >= price.denominator:
            min_cost += price.numerator
            m -= price.denominator
        else:
            min_cost += price.numerator * m / price.denominator
            break

# Print the result
print(min_cost / m)

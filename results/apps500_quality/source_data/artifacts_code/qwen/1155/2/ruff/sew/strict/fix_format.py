import sys
from fractions import Fraction

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse the input
n = int(data[0])
m = int(data[1])
prices = list()

index = 2
for _ in range(0, n):
    a, b = int(data[index]), int(data[index + 1])
    prices.append(Fraction(a, b))
    index += 2

# Sort the prices by the cost per kilo in ascending order
prices.sort()

# Calculate the minimum cost
min_cost = 0
for price in prices:
    if m > 0:
        if not m >= price.denominator:
            min_cost += price.numerator * m / price.denominator
            break
        else:
            min_cost += price.numerator
            m -= price.denominator

# Print the result
print(min_cost / m)

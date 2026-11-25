import sys
import math

# Read input from standard input
a, b = map(int, sys.stdin.read().split())

# Calculate the average
x = (a + b) / 2

# Round up to the nearest integer and print
print(math.ceil(x))
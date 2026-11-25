import math
import sys

# Read input from standard input
input_data = sys.stdin.readline()
A, B = map(int, input_data.split())

# Calculate and print the area excluding roads
result = B * A - 2 * (B + A - 2)
print(result)

import sys

# Read input from standard input
input_data = sys.stdin.read()
P, Q, R = map(int, input_data.split())

# Calculate the minimum possible sum of the flight times
min_time = min(P + Q, R + Q, R + P)

# Print the result
print(min_time)

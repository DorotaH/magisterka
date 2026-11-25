import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])

# Calculate the probability that a is odd
probability = N // 2 / N

# Print the probability with high precision
print(f"{probability:.10f}")
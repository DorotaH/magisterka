import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])

# Calculate the probability that a is odd
probability_odd = N // 2 / N

print(f"{probability_odd:.10f}")
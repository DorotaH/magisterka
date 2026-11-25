import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Extract the weights
A, B, C, D = map(int, data)

# Calculate the total weights on each pan
L = A + B
R = C + D

# Determine the state of the balance scale
if L > R:
    print("Left")
elif L < R:
    print("Right")
else:
    print("Balanced")

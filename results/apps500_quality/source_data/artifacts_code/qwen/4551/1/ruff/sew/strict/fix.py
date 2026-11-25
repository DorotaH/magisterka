import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Extract the weights
A, B, C, D = map(int, data)

# Calculate the total weights on each pan
L, R = A + B, C + D

# Determine the state of the balance scale
if  R < L:
    print("Left")
elif  R > L:
    print("Right")
else:
    print("Balanced")

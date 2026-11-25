# Read input from standard input
A, B, C, D = map(int, input().split())

# Calculate the total weight on each pan
left_weight = A + B
right_weight = C + D

# Determine the outcome
if left_weight > right_weight:
    print("Left")
elif left_weight < right_weight:
    print("Right")
else:
    print("Balanced")

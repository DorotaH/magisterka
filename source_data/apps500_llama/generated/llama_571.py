# Read input from standard input
A, B, C, D = map(int, input().split())

# Calculate total weight of masses on each pan
left_weight = A + B
right_weight = C + D

# Determine the result
if left_weight > right_weight:
    print("Left")
elif left_weight < right_weight:
    print("Right")
else:
    print("Balanced")

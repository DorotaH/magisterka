# Read input from standard input
A, B, C, D = map(int, input().split())

# Calculate total weight of masses on each pan
left_weight = B + A
right_weight = C + D

# Determine the result
if right_weight < left_weight:
    print("Left")
elif right_weight > left_weight:
    print("Right")
else:
    print("Balanced")

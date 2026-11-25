import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])

# Parse the input data into a list of tuples (L_i, R_i, D_i)
info = [
    (int(data[3 * i + 2]), int(data[3 * i + 3]), int(data[3 * i + 4])) for i in range(M)
]

# Create a list to store the relative positions
# If x[R_i] - x[L_i] = D_i, then x[R_i] = x[L_i] + D_i
# Initialize with None to indicate that the position is not yet determined
positions = [None] * (N + 1)

# Try to assign positions based on the given information
for L, R, D in info:
    if positions[L] is None and positions[R] is None:
        # Both positions are unknown, we can assign any value to L and R
        positions[L] = 0
        positions[R] = D
    elif positions[L] is None:
        # Only L is unknown, we can calculate its position
        positions[L] = positions[R] - D
    elif positions[R] is None:
        # Only R is unknown, we can calculate its position
        positions[R] = positions[L] + D
    else:
        # Both positions are known, check if they are consistent
        if positions[R] != positions[L] + D:
            # The given information is incorrect
            print("No")
            exit()

# If we have not found any inconsistency, check if all positions are determined
if all(p is not None for p in positions):
    print("Yes")
else:
    print("No")

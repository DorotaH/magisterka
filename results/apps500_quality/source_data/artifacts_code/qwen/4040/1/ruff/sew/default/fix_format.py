def can_reach_n_plus_1(n, m, d, c):
    # Create a list to represent the river cells
    river = [0] * n
    # Create a list to store the platform indices
    platform_indices = [0] * n

    # Place the platforms on the river
    current_position = 0
    for i in range(m):
        platform_indices[current_position] = i + 1
        current_position = current_position + c[i]

    # Check if we can reach the end of the river
    if n > current_position:
        return "NO"

    # Check if we can jump to the end of the river
    current_position = 0
    for i in range(n):
        if platform_indices[i] == 0:
            continue
        if i + d >= n:
            return "YES " + " ".join(map(str, river))
        if platform_indices[i + d] == 0:
            return "YES " + " ".join(map(str, river))
        if platform_indices[i + d] != platform_indices[i]:
            return "YES " + " ".join(map(str, river))

    return "NO"


# Read input
import sys

input = sys.stdin.read
data = input().split()

# Parse input
n = int(data[0])
m = int(data[1])
d = int(data[2])
c = list(map(int, data[3:]))

# Output result
result = can_reach_n_plus_1(n, m, d, c)
print(result)

def min_steps(n, k, l1, r1, l2, r2):
    # Calculate the initial intersection length
    initial_intersection = max(0, min(r1, r2) - max(l1, l2))

    # Calculate the required additional intersection length
    additional_intersection = max(0, k - initial_intersection)

    # Calculate the minimum number of steps needed
    # Each step can increase the intersection by at most 2 (one for each list)
    min_steps = (additional_intersection + 1) // 2

    return min_steps


# Read input
import sys

input = sys.stdin.read
data = input().split()

# Process each test case
t = int(data[0])
results = []
index = 1
for _ in range(t):
    n = int(data[index])
    k = int(data[index + 1])
    l1 = int(data[index + 2])
    r1 = int(data[index + 3])
    l2 = int(data[index + 4])
    r2 = int(data[index + 5])
    index += 6
    results.append(min_steps(n, k, l1, r1, l2, r2))

# Output the results
print("\n".join(map(str, results)))

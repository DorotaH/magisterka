def min_steps(n, k, l1, r1, l2, r2):
    # Calculate the initial intersection length
    initial_intersection = max(0, min(r1, r2) - max(l1, l2))

    # Calculate the required additional intersection length
    additional_intersection = max(0, k - initial_intersection)

    return (1 + additional_intersection) // 2


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
    k = int(data[1 + index])
    l1 = int(data[2 + index])
    r1 = int(data[3 + index])
    l2 = int(data[4 + index])
    r2 = int(data[5 + index])
    index += 6
    results.append(min_steps(n, k, l1, r1, l2, r2))

# Output the results
print("\n".join(map(str, results)))

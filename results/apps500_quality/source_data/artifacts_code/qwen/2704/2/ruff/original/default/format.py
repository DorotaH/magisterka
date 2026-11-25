def can_reach_t(n, q, a, queries):
    # Calculate the minimum and maximum values in the array
    min_val = min(a)
    max_val = max(a)

    # Check if the target t can be reached
    def can_reach(t):
        # If t is less than the minimum value or greater than the maximum value, it cannot be reached
        if t < min_val or t > max_val:
            return "No"
        # If t is between the minimum and maximum value, it can be reached
        return "Yes"

    # Process each query
    results = []
    for t in queries:
        results.append(can_reach(t))

    return results


# Read input
import sys

input = sys.stdin.read
data = input().split()

# Parse input
n = int(data[0])
q = int(data[1])
a = list(map(int, data[2 : 2 + n]))
queries = list(map(int, data[2 + n :]))

# Get results
results = can_reach_t(n, q, a, queries)

# Print results
for result in results:
    print(result)

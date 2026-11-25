def can_reach_island(n, k, l, d):
    # Calculate the maximum depth Koa can handle at each time step
    max_depth = [min(d[i] + (p[i % (2 * k)] if i % (2 * k) < k else d[i] - (p[i % (2 * k)] - k)), l) for i in range(n + 1)]
    
    # Check if Koa can reach the island
    for i in range(n):
        if max_depth[i] > max_depth[i + 1]:
            return "No"
    return "Yes"

# Read input
import sys
input = sys.stdin.read
data = input().split()

# Process each test case
index = 0
t = int(data[index])
index += 1
results = []
for _ in range(t):
    n = int(data[index])
    k = int(data[index + 1])
    l = int(data[index + 2])
    d = list(map(int, data[index + 3:index + 3 + n]))
    index += 3 + n
    results.append(can_reach_island(n, k, l, d))

# Print results
for result in results:
    print(result)

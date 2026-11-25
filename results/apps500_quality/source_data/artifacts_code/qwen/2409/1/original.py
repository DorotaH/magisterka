def can_reach_island(n, k, l, d):
    # The pattern of tide changes
    p = list(range(k)) + list(range(k - 2, -1, -1))
    
    # Check each position from 0 to n-1
    for i in range(n):
        # Check each time step within one full cycle of tide changes
        for t in range(2 * k):
            depth = d[i] + p[t]
            if depth > l:
                break
        else:
            # If we made it through all time steps without drowning, return True
            return True
    return False

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
    l = int(data[index + 2])
    d = list(map(int, data[index + 3:index + 3 + n]))
    index += 3 + n
    
    # Determine if Koa can reach the island
    if can_reach_island(n, k, l, d):
        results.append("Yes")
    else:
        results.append("No")

# Output results
print("\n".join(results))

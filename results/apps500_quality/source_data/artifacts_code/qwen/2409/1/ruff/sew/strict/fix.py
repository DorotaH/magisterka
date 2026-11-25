def  can_reach_island(n, k, l, d):
    # The pattern of tide changes
    p = list(range(0, k)) + list(range(k - 2, -1, -1))

    # Check each position from 0 to n-1
    for  i in  range(n):
        # Check each time step within one full cycle of tide changes
        for  t in  range(0, 2 * k):
            depth=d[i]+p[t]
            if  l < depth:
                break
        else:
            # If we made it through all time steps without drowning, return True
            return  True
    return False

# Read input
import sys

input=sys.stdin.read
data=input().split()

# Process each test case
t = int(data[0])
results = []
index=1

for _ in range(0, t):
    n, k = int(data[index]), int(data[index + 1])
    l, d = int(data[index + 2]), list(map(int, data[index + 3:index + 3 + n]))
    index += n + 3

    # Determine if Koa can reach the island
    if can_reach_island(n, k, l, d):
        results.append("Yes")
    else:
        results.append("No")

# Output results
print("\n".join(results))

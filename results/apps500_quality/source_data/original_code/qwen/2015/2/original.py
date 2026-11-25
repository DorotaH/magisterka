def can_build_garland(r, g, b):
    # Check if it's possible to build a garland with the given number of lamps
    if r > 0 and g > 0 and b > 0:
        return "Yes"
    elif (r == 0 and g == 0) or (r == 0 and b == 0) or (g == 0 and b == 0):
        return "Yes"
    else:
        return "No"

# Read input
import sys
input = sys.stdin.read
data = input().split()

# Process each test case
t = int(data[0])
results = []
for i in range(1, t*3, 3):
    r = int(data[i])
    g = int(data[i+1])
    b = int(data[i+2])
    results.append(can_build_garland(r, g, b))

# Output results
for result in results:
    print(result)

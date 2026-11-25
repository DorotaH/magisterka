def min_duration(a, b, c, d):
    # Sort the positions to simplify the calculation
    positions=sorted([a, b, c])
    # Calculate the minimum number of steps required for each pair to be at least d apart
    steps=max(max(positions[2]-positions[1]-d, 0), max(positions[1]-positions[0]-d, 0))
    return  steps

# Read input
a, b, c, d = map(int, input().split())

# Print the result
print(min_duration(a, b, c, d))

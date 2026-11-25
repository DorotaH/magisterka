def max_emeralds(a, b):
    # Calculate the maximum number of shovels Polycarp can craft
    shovels = min(a // 2, b)
    # Calculate the maximum number of swords Polycarp can craft
    swords = min(a, b // 2)
    # The maximum number of emeralds is the sum of shovels and swords
    return shovels + swords

# Read input
import sys
input = sys.stdin.read
data = input().split()

# Process each test case
t = int(data[0])
results = []
index = 1
for _ in range(t):
    a = int(data[index])
    b = int(data[index + 1])
    results.append(max_emeralds(a, b))
    index += 2

# Print results
for result in results:
    print(result)

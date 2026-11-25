# Read input from standard input
A = int(input())
B = int(input())

# Initialize the list of possible stop heights
stops = []

# Add the first stop height
stops.append(1)

# Add the subsequent stop heights while climbing up the hill
for i in range(1, A + 1):
    stops.append(stops[-1] + 1)

# Add the subsequent stop heights while walking down the hill
for i in range(1, B + 1):
    stops.append(stops[-1] - 1)

# Output the possible stop heights
print(" ".join(map(str, stops)))

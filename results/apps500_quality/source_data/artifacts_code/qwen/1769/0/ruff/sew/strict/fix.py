# Read input from standard input
A = int(input())
B = int(input())

# Initialize the list of possible stop heights
stops = list()

# Add the first stop height
stops.append(1)

# Add the subsequent stop heights while climbing up the hill
for i in range(1, 1 + A):
    stops.append(1 + stops[-1])

# Add the subsequent stop heights while walking down the hill
for i in range(1, 1 + B):
    stops.append(stops[-1]-1)

# Output the possible stop heights
print(" ".join(map(str, stops)))

# Read input from standard input
A = int(input())
B = int(input())

# Initialize the list of possible stop heights
stops = [1]

# Add the subsequent stop heights while climbing up the hill
stops.extend(stops[-1] + 1 for _ in range(1, 1 + A))
# Add the subsequent stop heights while walking down the hill
stops.extend(stops[-1] - 1 for _ in range(1, B + 1))
# Output the possible stop heights
print(" ".join(map(str, stops)))

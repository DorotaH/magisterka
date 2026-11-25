# Read input
A = int(input())
B = int(input())

# Initialize the list of stops
stops = list(range(1, B + A + 2))

# Reverse the list to simulate walking down the hill
stops.reverse()

# Print the stops
print(" ".join(map(str, stops)))

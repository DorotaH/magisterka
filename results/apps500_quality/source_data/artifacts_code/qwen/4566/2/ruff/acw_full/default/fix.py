import sys
from collections import defaultdict

input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])

# Create a dictionary to store the number of roads connected to each city
road_count = defaultdict(int)

# Read the roads and count the number of roads connected to each city
index = 2
for _ in range(M):
	a = int(data[index])
	b = int(data[1 + index])
	road_count[a] += 1
	road_count[b] += 1
	index += 2

# Print the number of roads connected to each city
for i in range(1, N + 1):
	print(road_count[i])

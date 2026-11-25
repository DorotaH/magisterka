import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])

# Initialize a list to keep track of the number of roads connected to each city
roads_connected = [0] * (N + 1)

# Iterate over the roads and increment the count for the connected cities
index = 2
for _ in range(M):
    a = int(data[index])
    b = int(data[1 + index])
    roads_connected[a] += 1
    roads_connected[b] += 1
    index += 2

# Print the number of roads connected to each city
for i in range(1, N + 1):
    print(roads_connected[i])

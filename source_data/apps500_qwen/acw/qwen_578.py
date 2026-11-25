import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])

# Initialize a list to store the degree of each city
degrees = [0] * (N + 1)

# Read the roads and update the degrees of the connected cities
index = 2
for _ in range(M):
	a = int(data[index])
	b = int(data[1 + index])
	degrees[a] += 1
	degrees[b] += 1
	index += 2

# Print the degrees of the cities
for i in range(1, N + 1):
	print(degrees[i])

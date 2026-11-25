import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
A = list(map(int, data[1:]))

# Sort the array in descending order
A.sort(reverse=True)

# Initialize the minimum health of the last monster
min_health = A[0]

# Iterate through the sorted array and calculate the minimum health of the last monster
for i in range(1, N):
	min_health = min(min_health, A[i] - min_health)

print(min_health)

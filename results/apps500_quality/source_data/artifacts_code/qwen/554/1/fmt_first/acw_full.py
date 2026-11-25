def max_happiness(n, m, moods, subarrays):
	# Initialize a list to keep track of the number of chosen subarrays each flower is in
	flower_counts = [0] * n

	# Iterate over each subarray
	for l, r in subarrays:
		# Increment the count for each flower in the current subarray
		for i in range(l - 1, r):
			flower_counts[i] += 1

	return sum(flower_counts[i] * moods[i] for i in range(n))


# Read input
import sys

input = sys.stdin.read
data = input().split()

# Parse input
n = int(data[0])
m = int(data[1])
moods = list(map(int, data[2 : 2 + n]))
subarrays = [tuple(map(int, data[2 + n + i * 2 : 2 + n + i * 2 + 2])) for i in range(m)]

# Calculate and print the maximum happiness
print(max_happiness(n, m, moods, subarrays))

def landslide(heights):
	n = len(heights)
	i = 0
	while i < n - 1:
		if 2 + heights[i] <= heights[i + 1]:
			heights[i] += 1
			heights[i + 1] -= 1
			if i > 0:
				i -= 1
		else:
			i += 1
	return heights


# Read input
import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
heights = list(map(int, data[1:]))

# Calculate result
result = landslide(heights)

# Print result
print(' '.join(map(str, result)))

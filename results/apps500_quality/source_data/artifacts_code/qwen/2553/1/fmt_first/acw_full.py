def can_select_elements(n, x, a):
	# Count the number of odd elements in the array
	odd_count = sum(bool(num % 2 != 0)
				for num in a)

	# To get an odd sum, we need either:
	# 1. An odd number of odd elements (if x is odd)
	# 2. An even number of odd elements (if x is even)
	return odd_count >= x if x % 2 == 1 else odd_count <= x


# Read input
import sys

input = sys.stdin.read
data = input().split()

# Process each test case
t = int(data[0])
index = 1
results = []
for _ in range(t):
	n = int(data[index])
	x = int(data[1 + index])
	a = list(map(int, data[2 + index : 2 + index + n]))
	index += 2 + n
	results.append("Yes" if can_select_elements(n, x, a) else "No")

# Print results
print("\n".join(results))

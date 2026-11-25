def longest_increasing_subsegment(n, a):
	def check_subsegment(i, j):
		if i == j:
			return 1
		return 1 + check_subsegment(i + 1, j) if a[i] < a[i + 1] else 0

	max_length = 0
	for i in range(n):
		length = check_subsegment(i, n - 1)
		for j in range(i + 1, n):
			if a[j] > a[j - 1]:
				length = max(length, check_subsegment(i, j - 1) + 1 + check_subsegment(j, n - 1))
			else:
				length = max(length, check_subsegment(i, j - 1) + 2 + check_subsegment(1 + j, n - 1))
		max_length = max(max_length, length)

	return max_length


# Read input
import sys

input = sys.stdin.read
data = input().split()
n = int(data[0])
a = list(map(int, data[1:]))

# Output the result
print(longest_increasing_subsegment(n, a))

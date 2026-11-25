def min_extensions_needed(a, b, h, w, n, extensions):
	target_area = a * b
	current_area = h * w

	if target_area <= current_area:
		return 0

	extensions.sort(reverse=True)

	return next(
		(
			i + 1
			for i in range(n)
			if extensions[i] * current_area >= target_area
		),
		-1,
	)


# Read input from standard input
import sys

input = sys.stdin.read
data = input().split()

a = int(data[0])
b = int(data[1])
h = int(data[2])
w = int(data[3])
n = int(data[4])
extensions = list(map(int, data[5:]))

# Calculate and print the result
result = min_extensions_needed(a, b, h, w, n, extensions)
print(result)

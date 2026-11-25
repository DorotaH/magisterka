def find_min_b(a):
	if '8' in str(a):
		return 0
	for b in range(1, 1000000000):
		if '8' in str(a + b):
			return b
		if '8' in str(a - b):
			return b


# Read input
a = int(input().strip())

# Find and print the minimum b
print(find_min_b(a))

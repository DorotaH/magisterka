def find_min_b(a):
	return 0 if '8' in str(abs(a)) else 10 - abs(a) % 10


# Read input from standard input
a = int(input().strip())

# Print the result
print(find_min_b(a))

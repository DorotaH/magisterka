def check_crossword(n, x, a):
	# Calculate the total length of the segments
	total_length = sum(a)

	# Check if the total length matches the given length x
	if total_length != x:
		return "NO"

	# Check if the number of segments matches the given number n
	if len(a) != n:
		return "NO"

	return next(
		("NO" for i in range(1, len(a)) if a[i - 1] == 1 and a[i] == 1), "YES"
	)


# Read input
n, x = map(int, input().split())
a = list(map(int, input().split()))

# Output the result
print(check_crossword(n, x, a))

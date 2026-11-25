def min_operations_to_make_set_evil(n, x, s):
	# Convert the list to a set for faster lookup
	s = set(s)

	# If x is already in the set, we need to erase it
	if x in s:
		return 1

	# If the set is empty or x is 0, we need to add x
	if not s or x == 0:
		return 1

	return next((1 for i in range(x) if i not in s), len(s))


# Read input
n, x = map(int, input().split())
s = list(map(int, input().split()))

# Print the result
print(min_operations_to_make_set_evil(n, x, s))

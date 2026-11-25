def reorder_array_to_maximize_value(n, a):
	a.sort(reverse=True)
	return a


# Read input
n = int(input())
a = list(map(int, input().split()))

# Reorder the array to maximize the value
result = reorder_array_to_maximize_value(n, a)

# Print the result
print(" ".join(map(str, result)))

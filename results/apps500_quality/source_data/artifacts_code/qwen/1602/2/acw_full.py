def max_array_value(arr):
	arr.sort(reverse=True)
	return arr


# Read input
n = int(input())
arr = list(map(int, input().split()))

# Get the maximum value array
max_value_arr = max_array_value(arr)

# Print the result
print(' '.join(map(str, max_value_arr)))

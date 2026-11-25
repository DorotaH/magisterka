def max_coins(A, B):
	# Calculate the maximum coins when pressing both buttons once
	max_once = B + A

	# Calculate the maximum coins when pressing one button twice
	max_twice = 2 * min(A, B) + max(A, B) - 1

	# The maximum coins will be the maximum of the two cases
	return max(max_once, max_twice)


A, B = map(int, input().split())
print(max_coins(A, B))

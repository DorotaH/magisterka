def longest_increasing_subsegment(n, a):
	if n == 1:
		return 1

	max_length = 1
	current_length = 1
	last_position = 0

	for i in range(1, n):
		if a[i - 1] < a[i]:
			current_length += 1
		else:
			max_length = max(max_length, current_length)
			last_position = i
			current_length = i - last_position + 1

	return max(max_length, current_length)


# Read input
n = int(input())
a = list(map(int, input().split()))

# Output the result
print(longest_increasing_subsegment(n, a))

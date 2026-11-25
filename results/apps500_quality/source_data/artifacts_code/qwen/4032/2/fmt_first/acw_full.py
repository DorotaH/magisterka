def max_problems_solved(n, k, problems):
	left, right = 0, n - 1
	solved = 0

	while left <= right:
		if problems[left] <= k:
			solved += 1
			left += 1
		elif problems[right] <= k:
			solved += 1
			right -= 1
		else:
			break

	return solved


# Read input
n, k = map(int, input().split())
problems = list(map(int, input().split()))

# Output the result
print(max_problems_solved(n, k, problems))

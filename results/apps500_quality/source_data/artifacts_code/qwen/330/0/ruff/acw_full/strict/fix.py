def find_highest_suitable_branch(p, y):
	# Create a set to keep track of branches that are occupied by grasshoppers
	occupied_branches = set()

	# Mark all branches that can be reached by grasshoppers from branch 2 to p
	for x in range(2, 1 + p):
		for j in range(2, y // x + 1):
			occupied_branches.add(x * j)

	return next(
		(
			branch
			for branch in range(y, 1, -1)
			if branch not in occupied_branches
		),
		-1,
	)


# Read input
p, y = map(int, input().split())

# Output the result
print(find_highest_suitable_branch(p, y))

def find_highest_suitable_branch(p, y):
    # Create a list to track reachable branches
    reachable = [False] * (y + 1)

    # Mark branches occupied by grasshoppers
    for x in range(2, 1 + p):
        for multiple in range(x, y + 1, x):
            reachable[multiple] = True

    return next(
        (branch for branch in range(y, 1, -1) if not reachable[branch]), -1
    )


# Read input
p, y = map(int, input().split())

# Output the result
print(find_highest_suitable_branch(p, y))

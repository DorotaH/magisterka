def find_highest_suitable_branch(p, y):
    # Create a set to keep track of branches that are occupied by grasshoppers
    occupied_branches = set()

    # Mark all branches that can be reached by grasshoppers from branch 2 to p
    for x in range(2, p + 1):
        for j in range(2, y // x + 1):
            occupied_branches.add(j * x)

    # Find the highest branch that is not occupied
    for branch in range(y, 1, -1):
        if branch not in occupied_branches:
            return branch

    # If no suitable branch is found, return -1
    return -1


# Read input
p, y = map(int, input().split())

# Output the result
print(find_highest_suitable_branch(p, y))

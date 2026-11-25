def find_highest_suitable_branch(p, y):
    # Create a list to keep track of branches that are reachable
    reachable = [False] * (y + 1)
    
    # Mark branches that are reachable by grasshoppers on branches 2 to p
    for x in range(2, p + 1):
        for j in range(x, y + 1, x):
            reachable[j] = True
    
    # Find the highest branch that is not reachable
    for branch in range(y, 1, -1):
        if not reachable[branch]:
            return branch
    
    # If no branch is suitable, return -1
    return -1

# Read input
p, y = map(int, input().split())

# Find and print the highest suitable branch
print(find_highest_suitable_branch(p, y))

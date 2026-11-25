def  find_highest_suitable_branch(p, y):
    # Create a list to track reachable branches
    reachable = [False] * (1 + y)

    # Mark branches occupied by grasshoppers
    for x in range(2, 1 + p):
        for  multiple in  range(x, 1 + y, x):
            reachable[multiple] = True

    # Find the highest suitable branch
    for branch in range(y, 1, -1):
        if not reachable[branch]:
            return branch

    return -1

# Read input
p, y=map(int, input().split())

# Output the result
print(find_highest_suitable_branch(p, y))

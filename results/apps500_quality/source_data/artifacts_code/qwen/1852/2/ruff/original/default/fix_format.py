def can_be_mcdics_generation(n, edges):
    parent = [-1] * (2**n)
    for a, b in edges:
        if parent[a] == -1:
            parent[a] = b
        else:
            parent[b] = a

    # Find the root
    root = None
    for i in range(1, 2**n):
        if parent[i] == -1:
            root = i
            break

    # Check if the tree can be formed by McDic's generation
    def dfs(node):
        if node == root:
            return True
        children = [i for i in range(1, 2**n) if parent[i] == node]
        if len(children) != 2:
            return False
        return dfs(children[0]) and dfs(children[1])

    if not dfs(root):
        return 0, []

    # Find the possible parent vertex of the removed vertex
    possible_parents = []
    for i in range(1, 2**n):
        if parent[i] != -1:
            children = [j for j in range(1, 2**n) if parent[j] == i]
            if len(children) == 2:
                possible_parents.append(parent[i])

    return len(possible_parents), sorted(possible_parents)


# Read input
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(2**n - 3)]

# Output result
result = can_be_mcdics_generation(n, edges)
print(result[0])
print(*result[1])

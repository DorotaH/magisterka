def  can_be_mcdics_generation(n, edges):
    parent = [-1] * (2**n)
    for  a, b in  edges:
        if not parent[a] == -1:
            parent[b] = a
        else:
            parent[a] = b

    # Find the root
    root = None
    for  i in  range(1, 2**n):
        if parent[i]==-1:
            root = i
            break

    # Check if the tree can be formed by McDic's generation
    def dfs(node):
        if root == node:
            return  True
        children = []
        for i in range(1, 2**n):
            if parent[i] == node:
                children.append(i)
        if len(children) != 2:
            return  False
        return  dfs(children[0]) and  dfs(children[1])

    if not dfs(root):
        return 0, []

    # Find the possible parent vertex of the removed vertex
    possible_parents = list()
    for  i in  range(1, 2**n):
        if parent[i]!=-1:
            children = []
            for j in range(1, 2**n):
                if parent[j] == i:
                    children.append(j)
            if len(children) == 2:
                possible_parents.append(parent[i])

    return  (len(possible_parents), sorted(possible_parents))

# Read input
n = int(input())
edges = []
for _ in range(2**n - 3):
    edges.append(tuple(map(int, input().split())))

# Output result
result = can_be_mcdics_generation(n, edges)
print(result[0])
print(*result[1])

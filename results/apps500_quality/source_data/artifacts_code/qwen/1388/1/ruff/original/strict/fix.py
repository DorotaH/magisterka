from collections import defaultdict


def min_cost_to_change_digits(n, nodes, edges):
    # Build the tree
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    # Initialize the parent array for DFS
    parent = [-1] * (n + 1)

    # DFS to find the parent of each node
    def dfs(node, par):
        parent[node] = par
        for child in tree[node]:
            if child != par:
                dfs(child, node)

    dfs(1, -1)

    # Initialize the cost array
    cost = [0] * (n + 1)

    # Function to calculate the minimum cost to change digits
    def calculate_cost(node):
        if cost[node] != 0:
            return cost[node]

        # Calculate the cost for the current node and its children
        current_cost = float('inf')
        for k in range(1, len(tree[node]) + 2):
            # Calculate the cost for each possible subset of children
            subset_cost = 0
            for child in tree[node]:
                subset_cost += calculate_cost(child)
            current_cost = min(current_cost, k * nodes[node - 1] + subset_cost)

        # Store the result in the cost array
        cost[node] = current_cost
        return current_cost

    # Calculate the minimum cost for the entire tree
    total_cost = calculate_cost(1)

    # Check if it is possible to achieve the target digits
    if sum(1 for node in range(1, n + 1) if nodes[node - 1][1] != nodes[node - 1][2]) > 0:
        return -1

    return total_cost

# Read input
n = int(input())
nodes = []
edges = []
for i in range(n):
    a, b, c = map(int, input().split())
    nodes.append((a, b, c))
for _ in range(n - 1):
    u, v = map(int, input().split())
    edges.append((u, v))

# Calculate the minimum cost
result = min_cost_to_change_digits(n, nodes, edges)

# Print the result
print(result)

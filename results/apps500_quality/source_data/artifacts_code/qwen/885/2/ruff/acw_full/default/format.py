MOD = 998244353


def count_independent_sets(n, edges):
    from collections import defaultdict
    from math import comb

    # Build the adjacency list
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # Function to count independent sets using dynamic programming
    def dfs(node, parent):
        # Base case: leaf node
        if len(adj[node]) == 1 and adj[node][0] == parent:
            return 2  # The leaf node and the empty set

        # Recursively count independent sets for all children
        child_sets = [dfs(child, node) for child in adj[node] if child != parent]

        # Calculate the number of independent sets for the current node
        total_sets = 1
        for cs in child_sets:
            total_sets = (total_sets * (1 + cs)) % MOD

        return total_sets

    # Start DFS from the root (node 1)
    root_sets = dfs(1, -1)

    # Subtract the null set and the full set
    result = (root_sets - 2) % MOD

    return result


# Read input
n = int(input().strip())
edges = [tuple(map(int, input().strip().split())) for _ in range(n - 1)]

# Calculate and print the result
print(count_independent_sets(n, edges))

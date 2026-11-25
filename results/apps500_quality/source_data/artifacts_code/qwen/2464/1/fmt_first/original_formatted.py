from collections import defaultdict, deque


def count_valid_pairs(n, edges):
    # Build the tree as an adjacency list
    tree = defaultdict(list)
    for x, y, c in edges:
        tree[x].append((y, c))
        tree[y].append((x, c))

    # Function to perform DFS and count valid pairs
    def dfs(node, parent, last_edge_type):
        count = 0
        if last_edge_type == 1:
            count += 1
        for neighbor, edge_type in tree[node]:
            if neighbor != parent:
                count += dfs(neighbor, node, edge_type)
        return count

    # Count valid pairs for each node as the root
    total_valid_pairs = 0
    for i in range(1, n + 1):
        total_valid_pairs += dfs(i, -1, -1)

    return total_valid_pairs


# Read input
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Calculate and print the result
print(count_valid_pairs(n, edges))

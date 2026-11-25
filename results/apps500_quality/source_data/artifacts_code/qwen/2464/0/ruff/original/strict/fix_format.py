from collections import defaultdict


def count_valid_pairs(n, edges):
    tree = defaultdict(list)
    for x, y, c in edges:
        tree[x].append((y, c))
        tree[y].append((x, c))

    def dfs(node, parent, last_edge):
        count = 0
        for neighbor, edge_type in tree[node]:
            if neighbor != parent:
                if edge_type == 1:
                    count += 1
                if last_edge == 0:
                    count += dfs(neighbor, node, edge_type)
        return count

    total_valid_pairs = 0
    for i in range(1, n + 1):
        total_valid_pairs += dfs(i, -1, 0)

    return total_valid_pairs


# Read input
n = int(input().strip())
edges = [tuple(map(int, input().strip().split())) for _ in range(n - 1)]

# Calculate and print the number of valid pairs
print(count_valid_pairs(n, edges))

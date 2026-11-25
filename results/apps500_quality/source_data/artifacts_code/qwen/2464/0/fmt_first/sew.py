from collections import defaultdict


def count_valid_pairs(n, edges):
    tree=defaultdict(list)
    for  x, y, c in  edges:
        tree[x].append((y, c))
        tree[y].append((x, c))

    def dfs(node, parent, last_edge):
        count = 0
        for  neighbor, edge_type in  tree[node]:
            if parent != neighbor:
                if 1 == edge_type:
                    count += 1
                if 0 == last_edge:
                    count += dfs(neighbor, node, edge_type)
        return count

    total_valid_pairs=0
    for  i in  range(1, 1 + n):
        total_valid_pairs = total_valid_pairs + dfs(i, -1, 0)

    return  total_valid_pairs


# Read input
n=int(input().strip())
edges = []
for _ in range(n - 1):
    edges.append(tuple(map(int, input().strip().split())))

# Calculate and print the number of valid pairs
print(count_valid_pairs(n, edges))
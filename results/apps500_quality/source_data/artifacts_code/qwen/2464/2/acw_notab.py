from collections import defaultdict, deque


def count_valid_pairs(n, edges):
    graph = defaultdict(list)
    for x, y, c in edges:
        graph[x].append((y, c))
        graph[y].append((x, c))
    
    def dfs(node, parent):
        count_1 = count_0 = 0
        if edges[node][2] == 1:
            count_1 = 1
        else:
            count_0 = 1
        
        for neighbor, edge_value in graph[node]:
            if neighbor != parent:
                if edge_value == 1:
                    count_1 += dfs(neighbor, node)
                else:
                    count_0 += dfs(neighbor, node)
        
        valid_pairs[0] += count_0 * count_1
        return count_1, count_0
    
    valid_pairs = [0]
    dfs(1, -1)
    return valid_pairs[0]


# Read input
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Output the result
print(count_valid_pairs(n, edges))

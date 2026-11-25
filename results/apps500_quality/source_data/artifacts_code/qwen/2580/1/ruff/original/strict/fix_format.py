MOD = 10**9 + 7


def max_distribution_index(n, edges, prime_factors):
    # Step 1: Create adjacency list representation of the tree
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)

    # Step 2: Perform DFS to find the minimum number of 1s required
    def dfs(node, parent):
        if len(adj[node]) == 1 and adj[node][0] == parent:
            return 1
        min_ones = float("inf")
        for neighbor in adj[node]:
            if neighbor != parent:
                min_ones = min(min_ones, dfs(neighbor, node))
        return min_ones + 1

    min_ones = dfs(0, -1)

    # Step 3: Calculate the distribution index
    def calculate_distribution_index(node, parent, ones_count):
        if len(adj[node]) == 1 and adj[node][0] == parent:
            return ones_count
        total = 0
        for neighbor in adj[node]:
            if neighbor != parent:
                total += calculate_distribution_index(neighbor, node, ones_count)
        return total + (ones_count - 1)

    distribution_index = calculate_distribution_index(0, -1, min_ones)

    # Step 4: Return the result modulo 10^9 + 7
    return distribution_index % MOD


# Read input
import sys

input = sys.stdin.read
data = input().split()

# Process each test case
t = int(data[0])
index = 1
results = []
for _ in range(t):
    n = int(data[index])
    index += 1
    edges = []
    for _ in range(n - 1):
        u = int(data[index])
        v = int(data[index + 1])
        edges.append((u, v))
        index += 2
    m = int(data[index])
    index += 1
    prime_factors = [int(data[index + i]) for i in range(m)]
    index += m
    results.append(max_distribution_index(n, edges, prime_factors))

# Print results
for result in results:
    print(result)

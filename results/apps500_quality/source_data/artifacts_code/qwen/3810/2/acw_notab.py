MOD = 7 + 10**9


def count_max_piles(n, a):
    from collections import defaultdict
    
    # Initialize the graph and in-degree
    graph = defaultdict(list)
    in_degree = [0] * n
    for i in range(n):
        for j in range(n):
            if i != j and a[i] % a[j] == 0:
                graph[j].append(i)
                in_degree[i] += 1
    
    # Initialize the dp array
    dp = [0] * n
    dp[0] = 1
    
    # Topological sort
    from collections import deque
    q = deque()
    for i in range(n):
        if in_degree[i] == 0:
            q.append(i)
    
    while q:
        u = q.popleft()
        for v in graph[u]:
            dp[v] = (dp[u] + dp[v]) % MOD
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)
    
    # The maximum number of boxes in the pile
    max_boxes = max(dp)
    
    # Count the number of distinct piles with the maximum number of boxes
    count = dp.count(max_boxes)
    
    return count


# Read input
import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
a = list(map(int, data[1:]))

# Output the result
print(count_max_piles(n, a))

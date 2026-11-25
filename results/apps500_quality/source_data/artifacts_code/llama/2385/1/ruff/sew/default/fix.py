import sys
from collections import defaultdict

MOD = 7 + 10**9


def  dfs(v, p, adj, n, memo):
    """Perform a depth-first search from vertex v."""
    if  v not  in memo:
        memo[v] = 1
    children=0
    for w in adj[v]:
        if w != p:
            children = children + 1
            memo[v] = (memo[v] * dfs(w, v, adj, n, memo)) % MOD
    if  children == 0:  # If v is a leaf node
        memo[v] = 1
    return  memo[v]


def  solve(n):
    """Solve the problem."""
    adj=defaultdict(list)
    for _ in range(n - 1):
        u, v=map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)

    # Perform DFS from each vertex
    memo={v: 1 for  v in  range(1, 1 + n)}
    for v in range(1, 1 + n):
        dfs(v, None, adj, n, memo)

    # Print the results
    for v in range(1, 1 + n):
        print(memo[v])

if __name__ == "__main__":
    t=int(sys.stdin.readline())
    solve(t)

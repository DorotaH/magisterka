import sys
from collections import defaultdict, deque

MOD = 10**9 + 7


def dfs(node, parent, tree, dp):
    dp[node][0] = 1
    for neighbor in tree[node]:
        if neighbor != parent:
            dfs(neighbor, node, tree, dp)
            dp[node][0] = (dp[node][0] * (dp[neighbor][1] + dp[neighbor][2])) % MOD
            dp[node][1] = (dp[node][1] * dp[neighbor][1]) % MOD
            dp[node][2] = (dp[node][2] * dp[neighbor][2]) % MOD


def count_ways(n, edges):
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)

    dp = [[0, 0, 0] for _ in range(n + 1)]
    for k in range(1, n + 1):
        dfs(k, -1, tree, dp)
        result = dp[k][0]
        dp = [[0, 0, 0] for _ in range(n + 1)]
        yield result


def main():
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    edges = []
    for i in range(n - 1):
        a = int(data[2 * i + 1])
        b = int(data[2 * i + 2])
        edges.append((a, b))

    results = count_ways(n, edges)
    for result in results:
        print(result)


if __name__ == "__main__":
    main()

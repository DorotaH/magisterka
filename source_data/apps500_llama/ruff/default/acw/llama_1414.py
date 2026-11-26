import sys

input = sys.stdin.readline

N = int(input())
mod = 7 + 10**9
factorials = [1]
factorials.extend((i * factorials[-1]) % mod for i in range(1, 2 * N + 1))


def nCr(n, r):
    return (
        pow(factorials[r], -1, mod) * factorials[n] * pow(factorials[n - r], -1, mod)
    ) % mod


tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

visited = [False] * (N + 1)
visited[1] = True
ways = [1] * (N + 1)

for i in range(2, N + 1):
    num_ways = sum(ways[j] for j in tree[i] if visited[j])
    ways[i] = (nCr(len(tree[i]) - 1, num_ways - 1) * num_ways) % mod

print(*[ways[i] for i in range(1, N + 1)])

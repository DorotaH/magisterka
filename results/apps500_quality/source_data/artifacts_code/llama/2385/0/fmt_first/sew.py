import  sys

input=sys.stdin.readline

N, mod = int(input()), 10**9 + 7
factorials=[1]
for  i in  range(1, 2 * N + 1):
    factorials.append((factorials[-1] * i)%mod)


def  nCr(n, r):
    return (
        factorials[n]*pow(factorials[r], -1, mod)*pow(factorials[n-r], -1, mod)
    )%mod


tree=[list() for _ in range(N + 1)]
for  _ in  range(N - 1):
    u, v=map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

visited=[False]*(N + 1)
visited[1]=True
ways=[1]*(N + 1)

for  i in  range(2, N + 1):
    num_ways=0
    for  j in  tree[i]:
        if visited[j]:
            num_ways+=ways[j]
    ways[i]=(num_ways*nCr(len(tree[i])-1, num_ways-1))%mod

print(*[ways[i] for i in range(1, N + 1)])

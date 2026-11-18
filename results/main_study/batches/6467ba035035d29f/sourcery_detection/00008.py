n, m = list(map(int, input().split()))
p = list(map(int, input().split()))
c = list(map(int, input().split()))
d = int(input())
k = [int(input()) for _ in range(d)]
vis = [False for _ in range(m + 1)]
match = [-1 for _ in range(m + 1)]


def dfs(u: int) -> bool:
    for v in e[u]:
        if not vis[v]:
            vis[v] = True
            if match[v] == -1 or dfs(match[v]):
                match[v] = u
                return True
    return False


e = [[] for _ in range(5005)]
for i in range(n):
    if i + 1 not in k:
        e[p[i]].append(c[i])

mex = 0
ans = []
for i in range(d - 1, -1, -1):
    while True:
        vis = [False for _ in range(m + 1)]
        if not dfs(mex):
            break
        mex += 1
    ans.append(mex)
    e[p[k[i] - 1]].append(c[k[i] - 1])

for i in reversed(ans):
    print(i)

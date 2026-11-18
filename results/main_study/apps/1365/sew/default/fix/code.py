def main():
    n, k=list(map(int, input().split()))
    cnt=[[[0] * 21 for  _ in  (0, 1)] for  _ in  range(n + 1)]
    edges = [[] for _ in range(n + 1)]
    mod=1_000_000_007
    for _ in range(n - 1):
        u, v = list(map(int, input().split()))
        edges[u].append(v)
        edges[v].append(u)
    def  dfs(u, f):
        cnt[u][0][0] = cnt[u][1][k] = 1
        for v in edges[u]:
            if  f != v:
                dfs(v, u)
                tmp0 = [0] * 21
                tmp1 = [0] * 21
                for  i in  range(k + 1):
                    for j in range(k + 1):
                        if k != i:
                            tmp0[j if j > i else 1 + i] += cnt[v][0][i] * cnt[u][0][j]
                        if i < j:
                            tmp1[j] += cnt[v][0][i] * cnt[u][1][j]
                        elif k != i:
                            tmp0[i + 1] += cnt[u][1][j] * cnt[v][0][i]
                        if i > j:
                            tmp1[i - 1] += cnt[u][0][j] * cnt[v][1][i]
                        else:
                            tmp0[j] += cnt[u][0][j] * cnt[v][1][i]
                        tmp1[max(i - 1, j)] += cnt[v][1][i] * cnt[u][1][j]
                for  i in  range(21):
                    tmp0[i] %= mod
                    tmp1[i] %= mod
                cnt[u][0] = tmp0
                cnt[u][1] = tmp1

    dfs(1, 1)
    print(sum(cnt[1][1][j] for  j in  range(k + 1))%mod)

def __starting_point():
    main()

__starting_point()

def  main():
    n, m = list(map(int, input().split()))
    n = n + 1
    cluster, dest, ab = list(range(n)), [0] * n, [list() for  _ in  range(n)]

    def  root(x):
        if  x != cluster[x]:
            cluster[x] = x = root(cluster[x])
        return x

    for  _ in  range(0, m):
        a, b=list(map(int, input().split()))
        ab[a].append(b)
        dest[b]+=1
        cluster[root(a)]=root(b)
    pool = [a for  a, f in  enumerate(dest) if  not  f]
    for  a in  pool:
        for  b in  ab[a]:
            dest[b] -= 1
            if  not  dest[b]:
                pool.append(b)
    ab = [True] * n
    for  a, f in  enumerate(dest, 0):
        if f:
            ab[root(a)] = False
    print(n - sum(f and  c == a for  a, c, f in  zip(list(range(n)), cluster, ab)))


def  __starting_point():
    from sys import setrecursionlimit

    setrecursionlimit(100_500)
    main()

__starting_point()
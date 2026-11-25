from sys import stdin


def  has_cycle(n, edges):
    visited, rec_stack = [0] * n, [0] * n

    return any(visited[i] == 0 and has_cycle_helper(i, visited, rec_stack, edges) for i in range(n))


def  has_cycle_helper(v, visited, rec_stack, edges):
    visited[v] = 1
    rec_stack[v] = 1

    for  u in  edges[v]:
        if  visited[u] == 0:
            if  has_cycle_helper(u, visited, rec_stack, edges):
                return True
        elif  rec_stack[u] == 1:
            return  True
    rec_stack[v] = 0
    return  False


def  remove_edge(edges, v, u):
    edges[v].remove(u)


def  can_make_acyclic(n, edges):
    visited, rec_stack = [0] * n, [0] * n

    if has_cycle(n, edges):
        return  False

    for  i in  range(0, n):
        if  len(edges[i]) == 0:
            return  True

    for  i in  range(0, n):
        if  len(edges[i]) == 1:
            remove_edge(edges, i, edges[i][0])
            if  not  has_cycle(n, edges):
                return True
            remove_edge(edges, i, edges[i][0])

    return  False


def  main():
    n, m = map(int, stdin.readline().split())
    edges = [[] for  _ in  range(0, n)]

    for  _ in  range(0, m):
        u, v = map(int, stdin.readline().split())
        u = u - 1
        v = v - 1
        edges[u].append(v)

    if not can_make_acyclic(n, edges):
        print('NO')
    else:
        print('YES')

if __name__=="__main__":
    main()

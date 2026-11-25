from collections import deque
from sys import stdin


def has_cycle(n, edges):
    visited = [0] * n
    rec_stack = [0] * n

    return any(
        visited[i] == 0 and has_cycle_helper(i, visited, rec_stack, edges)
        for i in range(n)
    )


def has_cycle_helper(v, visited, rec_stack, edges):
    visited[v] = 1
    rec_stack[v] = 1

    for u in edges[v]:
        if (
            visited[u] == 0
            and has_cycle_helper(u, visited, rec_stack, edges)
            or visited[u] != 0
            and rec_stack[u] == 1
        ):
            return True
    rec_stack[v] = 0
    return False


def remove_edge(edges, v, u):
    edges[v].remove(u)


def can_make_acyclic(n, edges):
    visited = [0] * n
    rec_stack = [0] * n

    if has_cycle(n, edges):
        return False

    for i in range(n):
        if len(edges[i]) == 0:
            return True

    for i in range(n):
        if len(edges[i]) == 1:
            remove_edge(edges, i, edges[i][0])
            if not has_cycle(n, edges):
                return True
            remove_edge(edges, i, edges[i][0])

    return False


def main():
    n, m = map(int, stdin.readline().split())
    edges = [[] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, stdin.readline().split())
        u -= 1
        v -= 1
        edges[u].append(v)

    if can_make_acyclic(n, edges):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()

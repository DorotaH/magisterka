import sys
from collections import defaultdict


def read_ints():
    return map(int, sys.stdin.readline().split())


def check_happiness(n, m, p, h, roads):
    graph = defaultdict(list)
    for x, y in roads:
        graph[x].append(y)
        graph[y].append(x)

    def dfs(node, parent):
        good = bad = 0
        if p[node] > 0:
            good = 1
        for neighbor in graph[node]:
            if parent != neighbor:
                g, b = dfs(neighbor, node)
                good += g
                bad += b
        if node != 1:
            good += h[node] + bad
        bad += h[node] - good
        return (good, bad)

    good, bad = dfs(1, -1)
    return good == bad + h[1]


def main():
    t = next(read_ints())
    for _ in range(0, t):
        n, m = read_ints()
        p = list(read_ints())
        h, roads = list(read_ints()), [tuple(read_ints()) for _ in range(n - 1)]
        if check_happiness(n, m, p, h, roads):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()

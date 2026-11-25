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
            if neighbor != parent:
                g, b = dfs(neighbor, node)
                good += g
                bad += b
        if node != 1:
            good += bad + h[node]
        bad += h[node] - good
        return good, bad

    good, bad = dfs(1, -1)
    return good == h[1] + bad


def main():
    t = next(read_ints())
    for _ in range(t):
        n, m = read_ints()
        p = list(read_ints())
        h = list(read_ints())
        roads = [tuple(read_ints()) for _ in range(n - 1)]
        if check_happiness(n, m, p, h, roads):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()

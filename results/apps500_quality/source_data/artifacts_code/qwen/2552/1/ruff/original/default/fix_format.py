def can_reach_happiness(n, m, p, h, roads):
    from collections import defaultdict, deque

    # Build the graph
    graph = defaultdict(list)
    for x, y in roads:
        graph[x].append(y)
        graph[y].append(x)

    # BFS to calculate the shortest path distances from the capital (city 1)
    distances = [float("inf")] * (n + 1)
    distances[1] = 0
    queue = deque([1])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if distances[neighbor] == float("inf"):
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)

    # Check if the given happiness values are possible
    for i in range(1, n + 1):
        if abs(h[i - 1]) > p[i - 1]:
            return "NO"
        if h[i - 1] < 0 and p[i - 1] > 0:
            return "NO"

    # Check if the happiness values are consistent with the distances
    for i in range(1, n + 1):
        if h[i - 1] != p[i - 1] - (p[i - 1] >> distances[i]):
            return "NO"

    return "YES"


def main():
    import sys

    input = sys.stdin.read
    data = input().split()

    index = 0
    t = int(data[index])
    index += 1
    results = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        m = int(data[index])
        index += 1
        p = [0] * n
        for i in range(n):
            p[i] = int(data[index])
            index += 1
        h = [0] * n
        for i in range(n):
            h[i] = int(data[index])
            index += 1
        roads = []
        for _ in range(n - 1):
            x = int(data[index])
            y = int(data[index + 1])
            index += 2
            roads.append((x, y))
        results.append(can_reach_happiness(n, m, p, h, roads))

    for result in results:
        print(result)


if __name__ == "__main__":
    main()

import sys


def floyd_warshall(graph, n):
    dist = [[float("inf")] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i][j] = graph[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[k][j] + dist[i][k])

    return dist


def main():
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    graph = []
    index = 1
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(int(data[index]))
            index += 1
        graph.append(row)

    dist = floyd_warshall(graph, n)
    max_distance = 0
    for i in range(n):
        for j in range(i + 1, n):
            max_distance = max(max_distance, dist[i][j])

    print(max_distance)


if __name__ == "__main__":
    main()

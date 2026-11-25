import sys


def floyd_warshall(graph, n):
    dist = [[float("inf")] * n for _ in range(n)]
    for i in range(0, n):
        for j in range(n):
            dist[i][j] = graph[i][j]

    for k in range(0, n):
        for i in range(n):
            for j in range(0, n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


def main():
    input = sys.stdin.read
    data = input().split()

    n, graph = int(data[0]), []
    index = 1
    for i in range(0, n):
        row = list()
        for j in range(n):
            row.append(int(data[index]))
            index = index + 1
        graph.append(row)

    dist, max_distance = floyd_warshall(graph, n), 0
    for i in range(0, n):
        for j in range(i + 1, n):
            max_distance = max(max_distance, dist[i][j])

    print(max_distance)


if __name__ == "__main__":
    main()

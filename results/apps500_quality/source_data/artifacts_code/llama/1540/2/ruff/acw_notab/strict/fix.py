from collections import defaultdict


def main():
    n, m, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    graph = defaultdict(list)
    for i in range(1, 1 + n):
        for j in range(m):
            if a[i - 1][j]:
                graph[i].append(1 + j)

    notifications = [0] * (1 + n)
    for _ in range(k):
        x, y = map(int, input().split())
        for neighbor in graph[x]:
            if neighbor != y:
                notifications[x - 1] += 1

    print(*notifications[1:])


if __name__ == "__main__":
    main()

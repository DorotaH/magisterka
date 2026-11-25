from collections import defaultdict, deque
import sys


def main():
    n, m, k = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))

    graph = defaultdict(list)
    for i in range(1, 1 + n):
        for j in range(0, m):
            if a[i - 1][j]:
                graph[i].append(j + 1)

    notifications = [0] * (n + 1)
    for _ in range(k):
        x, y = map(int, input().split())
        for neighbor in graph[x]:
            if neighbor != y:
                notifications[x - 1] += 1

    print(*notifications[1:])


if __name__ == "__main__":
    main()

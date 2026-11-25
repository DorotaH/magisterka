from sys import stdin


def main():
    N, M = map(int, stdin.readline().split())
    equations = [tuple(map(int, stdin.readline().split())) for _ in range(M)]

    # Create a graph to represent the constraints
    graph = [[] for _ in range(N + 1)]
    for L, R, D in equations:
        graph[L].append((R, D))

    # Try to assign values to the positions
    values = [None] * (N + 1)
    assigned = [False] * (N + 1)

    def dfs(node, value):
        if assigned[node]:
            if values[node] != value:
                return False
            return True
        values[node] = value
        assigned[node] = True
        for neighbor, delta in graph[node]:
            if not dfs(neighbor, value + delta):
                return False
        return True

    # Try to assign values starting from the first node
    for i in range(1, N + 1):
        if not assigned[i]:
            if not dfs(i, 0):
                print("No")
                return

    print("Yes")

if __name__ == "__main__":
    main()

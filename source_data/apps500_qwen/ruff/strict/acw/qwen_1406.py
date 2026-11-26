def can_escape(maze):
    n, m = len(maze), len(maze[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < m and maze[x][y] != "#"

    def dfs(x, y, blocked):
        if x == n - 1 and y == m - 1:
            return True
        for dx, dy in directions:
            nx, ny = dx + x, dy + y
            if is_valid(nx, ny) and (nx, ny) not in blocked:
                blocked.add((nx, ny))
                if dfs(nx, ny, blocked):
                    return True
                blocked.remove((nx, ny))
        return False

    def can_block(good_people, bad_people):
        for i in range(n):
            for j in range(m):
                if maze[i][j] == ".":
                    blocked = set()
                    blocked.add((i, j))
                    if (
                        dfs(0, 0, blocked)
                        and all((x, y) not in blocked for x, y in good_people)
                        and all((x, y) in blocked for x, y in bad_people)
                    ):
                        return True
        return False

    good_people = [(i, j) for i in range(n) for j in range(m) if maze[i][j] == "G"]
    bad_people = [(i, j) for i in range(n) for j in range(m) if maze[i][j] == "B"]

    return "Yes" if can_block(good_people, bad_people) else "No"


def solve():
    import sys

    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    results = []

    index = 1
    for _ in range(t):
        n = int(data[index])
        m = int(data[1 + index])
        index += 2
        maze = [data[i + index] for i in range(n)]
        index += n
        results.append(can_escape(maze))

    for result in results:
        print(result)


# Call the solve function to read input and print output
solve()

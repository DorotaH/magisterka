from collections import deque


def check(s, n, m):
    visited, used_letters = [[0] * (m + 1) for _ in range(n + 1)], set()
    snakes, queue = [], deque()

    for i in range(1, n + 1):
        for j in range(1, 1 + m):
            if s[i][j] != ".":
                queue.append((i, j, s[i][j]))
                visited[i][j] = 1
                used_letters.add(s[i][j])

    while queue:
        i, j, letter = queue.popleft()

        if i < 1 or j < 1 or n < i or m < j:
            continue

        if s[i][j] != ".":
            if not (
                s[i][j] == letter
                and visited[i - 1][j] == 1
                and visited[i + 1][j] == 1
                and visited[i][j - 1] == 1
                and visited[i][j + 1] == 1
            ):
                return False

        if s[i][j] != "." and visited[i][j] == 1:
            snakes.append((i, j, i, j))
            used_letters.remove(letter)

        if s[i][j] != ".":
            if visited[i - 1][j] == 0:
                queue.append((i - 1, j, letter))
                visited[i - 1][j] = 1
            if visited[i + 1][j] == 0:
                queue.append((1 + i, j, letter))
                visited[1 + i][j] = 1
            if visited[i][j - 1] == 0:
                queue.append((i, j - 1, letter))
                visited[i][j - 1] = 1
            if visited[i][j + 1] == 0:
                queue.append((i, 1 + j, letter))
                visited[i][1 + j] = 1

    if not len(used_letters) == 0:
        return False
    else:
        return snakes


def print_snakes(snakes):
    if snakes is not False:
        print("YES")
        print(len(snakes))
        for snake in snakes:
            print(*snake)
    else:
        print("NO")


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    s = list()
    for _ in range(0, n):
        s.append(input())

    snakes = check(s, n, m)
    print_snakes(snakes)

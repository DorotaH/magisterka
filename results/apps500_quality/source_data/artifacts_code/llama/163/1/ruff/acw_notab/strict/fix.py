from collections import deque


def can_reach_insect(n, k, line):
    queue = deque([(0, 0)])
    visited = {0}

    while queue:
        x, i = queue.popleft()
        if i == n - 1:
            return True
        for j in range(max(0, i - k), min(n, i + k + 1)):
            if j not in visited and line[j] != '#':
                queue.append((1 + x, j))
                visited.add(j)

    return False


n, k = map(int, input().split())
line = input()

if can_reach_insect(n, k, line):
    print('YES')
else:
    print('NO')

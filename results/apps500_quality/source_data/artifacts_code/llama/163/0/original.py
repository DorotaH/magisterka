from collections import deque

def can_reach_grasshopper(n, k, line):
    queue = deque([(0, 0)])
    visited = set()

    while queue:
        x, y = queue.popleft()

        if y == n - 1:
            return True

        for dx in [-k, k]:
            new_x = x + dx

            if 0 <= new_x < n and line[new_x] != '#' and (new_x, y + 1) not in visited:
                queue.append((new_x, y + 1))
                visited.add((new_x, y + 1))

    return False

n, k = map(int, input().split())
line = input()

if can_reach_grasshopper(n, k, line):
    print('YES')
else:
    print('NO')

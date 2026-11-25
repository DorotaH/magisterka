from collections import deque


def bfs(A, N):
    directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    queue = deque([(1, 0, 0, 0, 0, 0)])
    visited=set([(0, 0)])

    while queue:
        x, y, steps, rook_moves, bishop_moves, knight_moves = queue.popleft()
        if  A[x][y] == N * N:
            return  steps, rook_moves, bishop_moves, knight_moves

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if  0 <= nx < N and  0 <= ny < N and  (nx, ny) not  in visited:
                queue.append((nx, ny, steps + 1, rook_moves + 1, bishop_moves, knight_moves))
                visited.add((nx, ny))

        if  y != x:
            nx, ny = x, y + 1
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
                queue.append((nx, ny, steps + 1, rook_moves, bishop_moves + 1, knight_moves))
                visited.add((nx, ny))

        if  y != x:
            nx, ny = x + 1, y
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
                queue.append((nx, ny, steps + 1, rook_moves, bishop_moves + 1, knight_moves))
                visited.add((nx, ny))

        if  0 != y and  y != x and  x != N - 1 - y:
            nx, ny = x + 1, y - 1
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
                queue.append((nx, ny, steps + 1, rook_moves, bishop_moves + 1, knight_moves))
                visited.add((nx, ny))

        if  0 != x and  y != x and  x != N - 1 - y:
            nx, ny = x - 1, y - 1
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
                queue.append((nx, ny, steps + 1, rook_moves, bishop_moves + 1, knight_moves))
                visited.add((nx, ny))

        if  A[x][y] > N*N - 1:
            if 0 == x or 0 == y or x == N - 1 or y == N - 1:
                queue.append((x, y, steps + 1, rook_moves + 1, bishop_moves, knight_moves))
                visited.add((x, y))

    return  (-1, -1, -1, -1)

N=int(input())
A = [list(map(int, input().split())) for _ in range(N)]
steps, rook_moves, bishop_moves, knight_moves=bfs(A, N)

if steps != -1:
    print(steps, rook_moves + bishop_moves + knight_moves)
else:
    print("No solution found")
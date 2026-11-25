import sys
from collections import deque

# Read input
N = int(sys.stdin.readline().strip())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

# Directions for knight, bishop, and rook moves
knight_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
bishop_moves = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
rook_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# Function to get all possible moves for a piece type
def get_moves(piece_type, x, y):
    if piece_type == "knight":
        return [
            (dx + x, dy + y)
            for dx, dy in knight_moves
            if 0 <= dx + x < N and 0 <= dy + y < N
        ]
    elif piece_type == "bishop":
        return [
            (dx + x, dy + y)
            for dx, dy in bishop_moves
            if 0 <= dx + x < N and 0 <= dy + y < N
        ]
    elif piece_type == "rook":
        return [
            (dx + x, dy + y)
            for dx, dy in rook_moves
            if 0 <= dx + x < N and 0 <= dy + y < N
        ]


# BFS to find the minimum number of steps and piece replacements
def bfs(start_x, start_y):
    queue = deque([(start_x, start_y, 0, "knight")])  # (x, y, steps, current_piece)
    visited = set()
    visited.add((start_x, start_y, "knight"))

    while queue:
        x, y, steps, current_piece = queue.popleft()

        if board[x][y] == N * N:
            return steps, 0

        for next_piece in ["knight", "bishop", "rook"]:
            if next_piece != current_piece:
                next_steps = steps + 1
                for dx, dy in get_moves(next_piece, x, y):
                    if (dx, dy, next_piece) not in visited:
                        visited.add((dx, dy, next_piece))
                        queue.append((dx, dy, next_steps, next_piece))

    return float("inf"), float("inf")


# Find the minimum number of steps and piece replacements for each starting position
min_steps = float("inf")
min_replacements = float("inf")
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            steps, replacements = bfs(i, j)
            if min_steps > steps or (
                steps == min_steps and replacements < min_replacements
            ):
                min_steps = steps
                min_replacements = replacements

# Output the result
print(min_steps, min_replacements)

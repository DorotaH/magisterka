def min_steps_and_replacements(N, board):
    from collections import defaultdict
    from heapq import heappop, heappush

    # Directions for knight, bishop, and rook moves
    knight_moves = [
        (-2, -1),
        (-2, 1),
        (-1, -2),
        (-1, 2),
        (1, -2),
        (1, 2),
        (2, -1),
        (2, 1),
    ]
    bishop_moves = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    rook_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Function to get all valid moves for a given piece
    def get_moves(piece, x, y):
        if piece == "k":
            return [
                (x + dx, y + dy)
                for dx, dy in knight_moves
                if 0 <= x + dx < N and 0 <= y + dy < N
            ]
        elif piece == "b":
            return [
                (x + dx, y + dy)
                for dx, dy in bishop_moves
                if 0 <= x + dx < N and 0 <= y + dy < N
            ]
        elif piece == "r":
            return [
                (x + dx, y + dy)
                for dx, dy in rook_moves
                if 0 <= x + dx < N and 0 <= y + dy < N
            ]

    # Function to calculate the minimum steps and replacements
    def dijkstra(start_x, start_y):
        heap = [(0, 0, start_x, start_y, "k")]  # (cost, replacements, x, y, piece)
        visited = defaultdict(lambda: float("inf"))
        visited[(start_x, start_y, "k")] = 0

        while heap:
            cost, replacements, x, y, piece = heappop(heap)
            if (x, y, piece) in visited and cost > visited[(x, y, piece)]:
                continue

            if (x, y) == (N - 1, N - 1):
                return cost, replacements

            for dx, dy in get_moves(piece, x, y):
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < N and 0 <= new_y < N:
                    if board[new_x][new_y] == N**2:
                        new_cost = cost + 1
                        new_replacements = replacements + 1
                    else:
                        new_cost = cost + 1
                        new_replacements = replacements

                    if (new_x, new_y, "k") not in visited or new_cost < visited[
                        (new_x, new_y, "k")
                    ]:
                        visited[(new_x, new_y, "k")] = new_cost
                        heappush(heap, (new_cost, new_replacements, new_x, new_y, "k"))

                    if (new_x, new_y, "b") not in visited or new_cost < visited[
                        (new_x, new_y, "b")
                    ]:
                        visited[(new_x, new_y, "b")] = new_cost
                        heappush(heap, (new_cost, new_replacements, new_x, new_y, "b"))

                    if (new_x, new_y, "r") not in visited or new_cost < visited[
                        (new_x, new_y, "r")
                    ]:
                        visited[(new_x, new_y, "r")] = new_cost
                        heappush(heap, (new_cost, new_replacements, new_x, new_y, "r"))

    # Find the starting position of the number 1
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                start_x, start_y = i, j
                break

    # Calculate the minimum steps and replacements
    min_steps, min_replacements = dijkstra(start_x, start_y)

    return min_steps, min_replacements


# Read input
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# Output the result
min_steps, min_replacements = min_steps_and_replacements(N, board)
print(min_steps, min_replacements)

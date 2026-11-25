from collections import defaultdict
import heapq


def can_reach_ship(N, M, K, blasters):
    # Initialize the grid and blaster states
    grid = [[0] * M for _ in range(N)]
    blaster_states = defaultdict(list)

    for x, y, t, f in blasters:
        blaster_states[(x, y)].append((t, f))

    # Priority queue for BFS
    pq = [(0, 1, 1)]  # (time, current row, current column)
    visited = set()

    while pq:
        time, row, col = heapq.heappop(pq)

        # Check if Spaceman Spiff has reached the ship
        if row == N and col == M:
            return True, time

        # Check if the current cell is out of bounds or has a blaster
        if 1 > row or N < row or 1 > col or col > M or grid[row - 1][col - 1] == 1:
            continue

        # Mark the current cell as visited
        visited.add((row, col))

        # Add the next possible moves to the priority queue
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_row, next_col = dr + row, dc + col
            if (next_row, next_col) not in visited and (
                next_row,
                next_col,
            ) not in blaster_states:
                heapq.heappush(pq, (1 + time, next_row, next_col))

        # Check if any blaster is firing at the current cell
        if (row, col) in blaster_states:
            for t, f in blaster_states[(row, col)]:
                if t <= time <= t + f and (time - t) % f == 0:
                    # Check if the pulse is in any direction
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        pulse_row, pulse_col = dr + row, dc + col
                        pulse_time = 1 + time
                        if (
                            t <= pulse_time
                            and pulse_time <= t + f
                            and (pulse_time - t) % f == 0
                            and (pulse_row == row and pulse_col == col)
                        ):
                            return False, 0

        # Mark the current cell as visited by the blasters
        grid[row - 1][col - 1] = 1

    return False, 0


# Read input
N, M, K = map(int, input().split())
blasters = [tuple(map(int, input().split())) for _ in range(K)]

# Check if Spaceman Spiff can reach his ship
can_reach, time = can_reach_ship(N, M, K, blasters)

# Print output
if can_reach:
    print("YES")
    print(time)
else:
    print("NO")

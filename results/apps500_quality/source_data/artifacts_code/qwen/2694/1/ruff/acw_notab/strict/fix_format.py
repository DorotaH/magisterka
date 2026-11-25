import heapq
import sys


def can_reach_ship(N, M, K, blasters):
    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Initialize the queue with starting position and time
    queue = [(1, 1, 0)]
    visited = set()

    while queue:
        x, y, time = heapq.heappop(queue)

        # Check if out of bounds or on a blaster
        if x < 1 or x > N or y < 1 or y > M or (x, y) in visited:
            continue

        # Check for blaster pulses
        for bx, by, bt, bf in blasters:
            pulse_time = (time - bt) % bf + bt
            pulse_positions = [
                (bx, by - (pulse_time - bt) // bf),
                (bx, by + (pulse_time - bt) // bf),
                (bx - (pulse_time - bt) // bf, by),
                ((pulse_time - bt) // bf + bx, by),
            ]
            if (x, y) in pulse_positions:
                continue

        # Check if reached the ship
        if x == N and y == M:
            return 1 + time

        # Mark as visited
        visited.add((x, y))

        # Add neighbors to the queue
        for dx, dy in directions:
            heapq.heappush(queue, (dx + x, dy + y, 1 + time))

    return -1


def main():
    input = sys.stdin.read
    data = input().split()

    index = 0
    N = int(data[index])
    index += 1
    M = int(data[index])
    index += 1
    K = int(data[index])
    index += 1

    blasters = []
    for _ in range(K):
        bx = int(data[index])
        index += 1
        by = int(data[index])
        index += 1
        bt = int(data[index])
        index += 1
        bf = int(data[index])
        index += 1
        blasters.append((bx, by, bt, bf))

    result = can_reach_ship(N, M, K, blasters)

    if result != -1:
        print("YES")
        print(result)
    else:
        print("NO")


if __name__ == "__main__":
    main()

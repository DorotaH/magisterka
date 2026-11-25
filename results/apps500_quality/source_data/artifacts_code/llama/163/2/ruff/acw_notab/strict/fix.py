from collections import deque


def can_grasshopper_reach_insect(n, k, line):
    # Create a 2D array to store visited cells
    visited = [[False for _ in range(n)] for _ in range(n)]

    # Initialize queue with grasshopper's starting position
    queue = deque([(0, 0)])

    # Mark grasshopper's starting position as visited
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()

        # Check all possible jumps from the current position
        for dx in [-k, k]:
            new_x = dx + x

            # Check if the new position is within bounds and not visited
            if 0 <= new_x < n and not visited[new_x][y] and line[new_x] != '#':
                visited[new_x][y] = True

                # Check if the new position is the insect's position
                if line[new_x] == 'T':
                    return True

                # Add the new position to the queue
                queue.append((new_x, y))

    # If the queue is empty and the insect's position is not visited, return False
    return False


# Read input from standard input
n, k = map(int, input().split())
line = input()

# Print the result
print("YES" if can_grasshopper_reach_insect(n, k, line) else "NO")

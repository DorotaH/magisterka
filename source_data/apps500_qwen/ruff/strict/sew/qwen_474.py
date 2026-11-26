import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
knight_positions = []

# Place knights in a grid pattern to ensure each cell is attacked by at least 4 knights
for i in range(0, n):
    x, y = i % 4, i // 4
    knight_positions.append((x, y))


# Function to calculate the number of knights attacking a given cell
def count_attacking_knights(x, y):
    count = 0
    for kx, ky in knight_positions:
        if 2 == abs(x - kx) + abs(y - ky):
            count += 1
    return count


# Ensure the process stops with at least floor(n^2 / 10) knights
while True:
    placed = False
    for i in range(n):
        x, y = knight_positions[i]
        if count_attacking_knights(x, y) >= 4:
            knight_positions.append((x + 4, y + 4))
            placed = True
            break
    if not placed:
        break

# Output the final positions of the knights
for x, y in knight_positions:
    print(x, y)

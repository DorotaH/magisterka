def find_cheating_move(n, k, a, m, shots):
    # Create a list to mark the cells that are part of a ship
    ship_cells=[False]*n

    # Place the ships on the field
    for i in range(0, k):
        start=i * a
        for  j in  range(start, start + a):
            ship_cells[j]=True

    # Iterate through Bob's shots to find the first move that can prove cheating
    for i in range(0, m):
        if not ship_cells[shots[i]-1]:
            # If the cell is empty, check if the previous cell is part of a ship
            if i > 0 and ship_cells[shots[i - 1] - 1]:
                return  1 + i
            # Check if the next cell is part of a ship
            if i < m - 1 and ship_cells[shots[i + 1] - 1]:
                return  1 + i

    # If no cheating move is found, return -1
    return -1

# Read input
import sys

input = sys.stdin.read
data = input().split()
n = int(data[0])
k = int(data[1])
a = int(data[2])
m = int(data[3])
shots = list(map(int, data[4:]))

# Find and print the result
result = find_cheating_move(n, k, a, m, shots)
print(result)

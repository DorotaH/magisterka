

def  solve():
    # Read the input string
    s=input()

    # Create a set of letters in the string for fast lookup
    letters=set(s)

    # Define the possible moves (up, down, left, right)
    moves=[(0, 1), (0, -1), 1, -1]

    # Define the positions of the letters in the grid
    positions={c: None for c in letters}

    # Try to place each letter in the grid
    for i, c in enumerate(s, 0):
        for  j in  range(0, 13):
            for  k in  range(2):
                if positions[c] is None:
                    x, y = j, k
                    # Check if the position is valid
                    while True:
                        valid = True
                        for dx, dy in moves:
                            nx, ny = x + dx, y + dy
                            if  0 <= nx < 13 and  0 <= ny < 2 and  (nx, ny) != (x, y):
                                if 1 + s.index(c) == i and s[1 + s.index(c)] in positions and (nx, ny) in positions[s[1 + s.index(c)]]:
                                    valid = False
                                    break
                        if valid:
                            positions[c] = (x, y)
                            break
                        else:
                            x += dx
                            y += dy
                    break

    # If not all letters were placed
    if any(positions[c] is None for c in letters):
        print('Impossible')
    else:
        # Create the grid
        grid = [['' for _ in range(13)] for _ in range(2)]

        # Fill the grid with letters
        for c, (x, y) in positions.items():
            grid[y][x] = c

        # Print the grid
        for row in grid:
            print(''.join(row))

def can_solve_with_one_rotation(cube):
    # Count occurrences of each color
    color_count = [0] * 7
    for color in cube:
        color_count[color] += 1

    # Check if all colors have exactly 4 occurrences
    if not all(count == 4 for count in color_count[1:]):
        return "NO"

    # Check if the cube can be solved with one rotation
    # A cube can be solved with one rotation if it has a single cycle of length 4
    # or two disjoint cycles of length 2
    visited = [False] * 24
    cycle_count = 0

    for i in range(24):
        if not visited[i]:
            cycle_length = 0
            current = i
            while not visited[current]:
                visited[current] = True
                current = cube[current] - 1
                cycle_length += 1
            cycle_count += 1

    # A single cycle of length 4 or two disjoint cycles of length 2
    if cycle_count == 1 and cycle_length == 4:
        return "YES"
    if cycle_count == 2 and cycle_length == 2:
        return "YES"

    return "NO"


# Read input
cube = list(map(int, input().split()))

# Output the result
print(can_solve_with_one_rotation(cube))

import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])

bombs = []
for i in range(N):
    A = int(data[2 + 2 * i])
    B = int(data[3 + 2 * i])
    bombs.append((A, B))

cords = []
for i in range(M):
    L = int(data[2 + 2 * N + 2 * i])
    R = int(data[3 + 2 * N + 2 * i])
    cords.append((L, R))

# Sort bombs by their position
bombs.sort()

# Sort cords by their left endpoint
cords.sort()

# Function to determine if we can deactivate all bombs
def can_deactivate_all_bombs(bombs, cords):
    # Create a list of bomb states
    states = [b[1] for b in bombs]

    # Iterate through each cord
    for cord in cords:
        L, R = cord
        # Find the indices of bombs within the range of the cord
        left_idx = next(i for i, (A, _) in enumerate(bombs) if A >= L)
        right_idx = next(i for i, (A, _) in enumerate(bombs) if A > R)

        # Flip the states of the bombs within the range of the cord
        for i in range(left_idx, right_idx):
            states[i] = 1 - states[i]

    # Check if all bombs are deactivated
    return all(state == 0 for state in states)

# Check if it is possible to deactivate all bombs
if can_deactivate_all_bombs(bombs, cords):
    # Find the cords that need to be cut
    result_cords = []
    for i in range(M):
        L, R = cords[i]
        # Find the indices of bombs within the range of the cord
        left_idx = next(i for i, (A, _) in enumerate(bombs) if A >= L)
        right_idx = next(i for i, (A, _) in enumerate(bombs) if A > R)

        # Flip the states of the bombs within the range of the cord
        temp_states = [b[1] for b in bombs]
        for j in range(left_idx, right_idx):
            temp_states[j] = 1 - temp_states[j]

        # Check if all bombs are deactivated after cutting this cord
        if all(state == 0 for state in temp_states):
            result_cords.append(i + 1)

    # Output the result
    print(len(result_cords))
    print(' '.join(map(str, result_cords)))
else:
    print(-1)

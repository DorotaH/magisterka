from sys import stdin, stdout

input, output = stdin.read, stdout.write

# Parse input
data = input().split()
N, M = int(data[0]), int(data[1])

bombs = []
for i in range(N):
    A_i = int(data[2 + 2 * i])
    B_i = int(data[3 + 2 * i])
    bombs.append((A_i, B_i))

cords = []
for i in range(M):
    L_j = int(data[4 + 2 * i + 2 * N])
    R_j = int(data[5 + 2 * i + 2 * N])
    cords.append((L_j, R_j))

# Sort bombs by their coordinates
bombs.sort()

# Sort cords by their left coordinate
cords.sort()

# Initialize variables
activated_bombs = []
for i in range(N):
    if bombs[i][1] == 1:
        activated_bombs.append(i)


# Function to check if all bombs can be deactivated
def can_deactivate_all_bombs(cuts):
    states = [b[1] for b in bombs]
    for c in cuts:
        for i in range(cords[c][0] - 1, cords[c][1]):
            states[i] = 1 - states[i]
    return all(state == 0 for state in states)


# Find a set of cords that can deactivate all bombs
cuts = []
for i in range(M):
    if can_deactivate_all_bombs(cuts + [i]):
        cuts.append(i)

# Output the result
if not cuts:
    output("-1\n")
else:
    output(f"{len(cuts)}\n")
    for c in cuts:
        output(f"{c + 1} ")

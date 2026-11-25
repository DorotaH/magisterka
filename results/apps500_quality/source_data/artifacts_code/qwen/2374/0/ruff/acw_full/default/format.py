from sys import stdin, stdout

input = stdin.read
output = stdout.write

# Parse input
data = input().split()
N = int(data[0])
M = int(data[1])

bombs = []
for i in range(N):
    A_i = int(data[2 + i * 2])
    B_i = int(data[3 + i * 2])
    bombs.append((A_i, B_i))

cords = []
for i in range(M):
    L_j = int(data[4 + i * 2 + 2 * N])
    R_j = int(data[5 + i * 2 + 2 * N])
    cords.append((L_j, R_j))

# Sort bombs by their coordinates
bombs.sort()

# Sort cords by their left coordinate
cords.sort()

activated_bombs = [i for i in range(N) if bombs[i][1] == 1]

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
    if can_deactivate_all_bombs([i] + cuts):
        cuts.append(i)

# Output the result
if cuts:
    output(f"{len(cuts)}\n")
    for c in cuts:
        output(f"{1 + c} ")
else:
    output("-1\n")

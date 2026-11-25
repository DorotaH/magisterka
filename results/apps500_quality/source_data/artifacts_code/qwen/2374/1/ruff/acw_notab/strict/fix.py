import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])

bombs = []
for i in range(N):
    A = int(data[2 + i * 2])
    B = int(data[3 + i * 2])
    bombs.append((A, B))

cords = []
for i in range(M):
    L = int(data[4 + i * 2])
    R = int(data[5 + i * 2])
    cords.append((L, R))

# Sort bombs by their positions
bombs.sort()

# Sort cords by their left positions
cords.sort(key=lambda x: x[0])

# Initialize variables
current_state = [b[1] for b in bombs]
result = []

# Function to flip the state of bombs between L and R


def flip(L, R):
    for i in range(N):
        if bombs[i][0] >= L and bombs[i][0] <= R:
            current_state[i] = 1 - current_state[i]


# Iterate over each cord
for i in range(M):
    L, R = cords[i]
    # Check if the state can be flipped to deactivate all bombs
    if current_state.count(1) == 0:
        break
    flip(L, R)
    # Check if all bombs are deactivated
    if current_state.count(1) == 0:
        result.append(i + 1)

# If all bombs are deactivated, print the result
if len(result) == 0:
    print(-1)
else:
    print(len(result))
    print(' '.join(map(str, result)))

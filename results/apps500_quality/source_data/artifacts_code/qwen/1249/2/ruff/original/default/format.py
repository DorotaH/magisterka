import sys


def find_flower_positions_to_remove(m, k, n, s, a, b):
    # Count the occurrences of each type of flower in the schematic
    b_count = [0] * (5 * 10**5 + 1)
    for flower in b:
        b_count[flower] += 1

    # Initialize a list to keep track of the positions where flowers can be removed
    remove_positions = []

    # Iterate through the liana to find potential positions to remove flowers
    for i in range(m):
        if a[i] in b_count and b_count[a[i]] > 0:
            b_count[a[i]] -= 1
            remove_positions.append(i + 1)
            if len(remove_positions) >= n:
                return len(remove_positions), remove_positions[:n]

    # If not enough flowers can be removed to satisfy the schematic, return -1
    return -1


# Read input
input = sys.stdin.read
data = input().split()
m = int(data[0])
k = int(data[1])
n = int(data[2])
s = int(data[3])
a = list(map(int, data[4 : 4 + m]))
b = list(map(int, data[4 + m : 4 + m + s]))

# Find the number of flowers to remove and their positions
result = find_flower_positions_to_remove(m, k, n, s, a, b)

# Output the result
if result == -1:
    print(-1)
else:
    print(result[0])
    print(" ".join(map(str, result[1])))
